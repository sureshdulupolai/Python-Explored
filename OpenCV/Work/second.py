"""
os.makedirs(save_folder, exist_ok=True) → Ensure folder exists, otherwise create it.
cv2.VideoCapture(0) → Start webcam (0 = laptop, 1 = external).
cv2.VideoWriter_fourcc(*'XVID') → Define codec for saving video.
out.write(frame) → Save each captured frame into the video file.
cv2.waitKey(1) → Wait 1 ms and check for key press (here 'q' to stop).
Release resources → Always release webcam and video writer to avoid file corruption or webcam lock.
"""

import cv2
import os

# Folder jahan video save karna hai
save_folder = "videos"
# Agar folder exist nahi karta, toh create kar do
os.makedirs(save_folder, exist_ok=True)

# File ka naam aur path define karo
video_path = os.path.join(save_folder, "my_webcam_video.avi")

# Webcam start karo: 0 => laptop webcam, 1 => external webcam
webcam = cv2.VideoCapture(0)

# Webcam se frame size get karo
frame_width = int(webcam.get(3))   # width of the frame
frame_height = int(webcam.get(4))  # height of the frame
fps = 20  # frames per second (smoothness of video)

# VideoWriter initialize karo
# 'XVID' codec use kiya for .avi video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter arguments: (filename, codec, fps, frame size)
out = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

while True:
    # Webcam se ek frame capture karo
    ret, frame = webcam.read()
    # Agar frame capture nahi hua, loop break karo
    if not ret:
        break

    # Frame display karo window me
    cv2.imshow("Webcam", frame)

    # Captured frame ko video file me save karo
    out.write(frame)

    # Stop recording agar 'q' press ho
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and video writer resources
webcam.release()  # Free the webcam
out.release()     # Close the video file properly
cv2.destroyAllWindows()  # Close all OpenCV windows

# Print the saved video path
print(f"Video saved at: {video_path}")
