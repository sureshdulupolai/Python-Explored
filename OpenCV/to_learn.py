# ==============================
# 📘 OPENCV COMPLETE PRACTICE ROADMAP for VS Code
# Author: Suresh Polai
# Goal: Master OpenCV for MediaPipe & AI projects
# ==============================

# =========================================
# 🟩 DAY 1: IMAGE & VIDEO BASICS
# =========================================
# 1. Install OpenCV: pip install opencv-python
# 2. Read an image -> cv2.imread()
# 3. Display an image -> cv2.imshow()
# 4. Save an image -> cv2.imwrite()
# 5. Capture video/webcam -> cv2.VideoCapture(0)
# 6. Show video frames in loop
# 7. Break loop on key press -> cv2.waitKey(1)
# 8. Release camera -> cap.release(), cv2.destroyAllWindows()

# =========================================
# 🟩 DAY 2: IMAGE OPERATIONS
# =========================================
# 1. Resize -> cv2.resize()
# 2. Crop -> img[y1:y2, x1:x2]
# 3. Flip -> cv2.flip(img, 1)
# 4. Rotate -> cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 5. Color Conversion -> cv2.cvtColor(img, cv2.COLOR_BGR2RGB / GRAY)

# =========================================
# 🟩 DAY 3: DRAWING & TEXT
# =========================================
# 1. Draw Line -> cv2.line(img, start, end, color, thickness)
# 2. Draw Rectangle -> cv2.rectangle(img, pt1, pt2, color, thickness)
# 3. Draw Circle -> cv2.circle(img, center, radius, color, thickness)
# 4. Draw Text -> cv2.putText(img, "Hello", position, font, size, color, thickness)
# 5. Practice combining shapes + text overlays

# =========================================
# 🟩 DAY 4: IMAGE FILTERS
# =========================================
# 1. Convert to grayscale -> cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2. Gaussian Blur -> cv2.GaussianBlur(img, (5,5), 0)
# 3. Median Blur -> cv2.medianBlur(img, 5)
# 4. Bilateral Filter -> cv2.bilateralFilter(img, 9,75,75)
# 5. Edge Detection -> cv2.Canny(img, 100, 200)

# =========================================
# 🟩 DAY 5: CONTOURS & SHAPE DETECTION
# =========================================
# 1. Threshold image -> cv2.threshold()
# 2. Find contours -> cv2.findContours()
# 3. Draw contours -> cv2.drawContours()
# 4. Get contour area -> cv2.contourArea()
# 5. Get bounding box -> cv2.boundingRect()
# 6. Detect shapes (triangle, square, circle)

# =========================================
# 🟩 DAY 6: MASKING & BITWISE OPERATIONS
# =========================================
# 1. Create mask -> cv2.inRange()
# 2. Bitwise AND, OR, NOT, XOR
# 3. Apply mask on image -> cv2.bitwise_and()
# 4. Background removal using mask

# =========================================
# 🟩 DAY 7: FACE DETECTION (HAARCASCADE)
# =========================================
# 1. Load cascade -> cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 2. Detect faces -> detectMultiScale()
# 3. Draw rectangles around faces
# 4. Detect eyes or smile (optional)

# =========================================
# 🟩 DAY 8: ADVANCED DETECTION
# =========================================
# 1. DNN module for object detection
# 2. Pretrained models (Caffe, TensorFlow)
# 3. Practice detecting people/objects in video

# =========================================
# 🟩 DAY 9: MEDIAPIPE INTEGRATION (START)
# =========================================
# 1. Install -> pip install mediapipe
# 2. Import -> import mediapipe as mp
# 3. Hand detection example
# 4. FaceMesh detection example
# 5. Pose detection example
# 6. Use cv2.flip(img,1) for selfie view
# 7. Draw landmarks using mp.solutions.drawing_utils

# =========================================
# 🟩 DAY 10: MINI PROJECTS (APPLY KNOWLEDGE)
# =========================================
# ✅ Hand Gesture Volume Control (Hand + OpenCV)
# ✅ Face Landmark Tracker (FaceMesh)
# ✅ Pose-based Workout Counter
# ✅ Background Remover (Mask + MediaPipe)
# ✅ Gesture Controlled Mouse (Advanced)

# =========================================
# 🟩 EXTRA PRACTICE IDEAS
# =========================================
# - Draw FPS (Frames per second) on live video
# - Save output video using cv2.VideoWriter()
# - Add custom overlays (logo, frame)
# - Integrate with Django or React (live stream processing)
