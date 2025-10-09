"""
pip install mediapipe

mp.solutions.hands → Hands detection
Hands() parameters
static_image_mode=False → continuous video frames
max_num_hands=2 → detect 2 hands maximum
min_detection_confidence=0.5 → threshold for detection
mp_draw.draw_landmarks → draw points & connections on detected hands
"""

import cv2
import mediapipe as mp
import csv
import os

# ===== Save folder =====
save_folder = "videos"
os.makedirs(save_folder, exist_ok=True)
csv_file = os.path.join(save_folder, "face_landmarks.csv")

# ===== Mediapipe Face Mesh =====
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

face_mesh = mp_face.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5
)

# ===== Webcam =====
cap = cv2.VideoCapture(0)

# ===== CSV setup =====
header = ["frame"]
for i in range(468):
    header += [f"x{i}", f"y{i}", f"z{i}"]

with open(csv_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_draw.draw_landmarks(
                frame, face_landmarks, mp_face.FACEMESH_TESSELATION,
                landmark_drawing_spec=mp_draw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_draw.DrawingSpec(color=(0,255,0), thickness=1)
            )

            # ===== Extract landmarks =====
            landmarks_row = [frame_count]
            for lm in face_landmarks.landmark:
                landmarks_row += [lm.x, lm.y, lm.z]

            # Save to CSV
            with open(csv_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(landmarks_row)

            # ===== Summary example (print key features) =====
            nose_tip = face_landmarks.landmark[1]
            left_eye_inner = face_landmarks.landmark[133]
            right_eye_inner = face_landmarks.landmark[362]

            print(f"Frame {frame_count}: Nose Tip({nose_tip.x:.3f},{nose_tip.y:.3f},{nose_tip.z:.3f})")
            print(f"Left Eye Inner({left_eye_inner.x:.3f},{left_eye_inner.y:.3f},{left_eye_inner.z:.3f})")
            print(f"Right Eye Inner({right_eye_inner.x:.3f},{right_eye_inner.y:.3f},{right_eye_inner.z:.3f})")
    
    cv2.imshow("Face Scan", frame)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Face landmarks saved at {csv_file}")


# import cv2
# import mediapipe as mp
# import os

# # ====== Folder to save video ======
# save_folder = "videos"
# os.makedirs(save_folder, exist_ok=True)
# video_path = os.path.join(save_folder, "hands_face_lowlight.avi")

# # ====== Initialize Mediapipe ======
# mp_hands = mp.solutions.hands
# mp_face = mp.solutions.face_mesh
# mp_draw = mp.solutions.drawing_utils

# hands = mp_hands.Hands(static_image_mode=False,
#                        max_num_hands=2,
#                        min_detection_confidence=0.5)
# face_mesh = mp_face.FaceMesh(static_image_mode=False,
#                              max_num_faces=1,
#                              min_detection_confidence=0.5)

# # ====== Initialize Webcam ======
# cap = cv2.VideoCapture(0)

# # Optional: set webcam resolution
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# # ====== Video Writer ======
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# fps = 20
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Enhance brightness/contrast for low-light
#     frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=30)  # alpha = contrast, beta = brightness

#     # Flip frame horizontally for selfie view
#     frame = cv2.flip(frame, 1)

#     # Convert BGR to RGB
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # ====== Hands Detection ======
#     hand_results = hands.process(rgb_frame)
#     if hand_results.multi_hand_landmarks:
#         for hand_landmarks in hand_results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#     # ====== Face Detection ======
#     face_results = face_mesh.process(rgb_frame)
#     if face_results.multi_face_landmarks:
#         for face_landmarks in face_results.multi_face_landmarks:
#             mp_draw.draw_landmarks(frame, face_landmarks, mp_face.FACEMESH_TESSELATION,
#                                    landmark_drawing_spec=mp_draw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
#                                    connection_drawing_spec=mp_draw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))

#     # Show frame
#     cv2.imshow("Hands & Face Detection (Low-light)", frame)

#     # Save frame to video
#     out.write(frame)

#     # Stop on 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"Video saved at: {video_path}")
