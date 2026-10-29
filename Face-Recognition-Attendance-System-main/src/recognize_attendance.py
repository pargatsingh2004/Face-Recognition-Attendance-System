
import cv2
import pandas as pd
import os
import csv
from datetime import datetime


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "trainer",
    "trainer.yml"
)

user_map_path = os.path.join(
    BASE_DIR,
    "user_map.csv"
)

cascade_path = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)

today = datetime.now().strftime("%Y-%m-%d")

attendance_dir = os.path.join(
    BASE_DIR,
    "attendance"
)

attendance_path = os.path.join(
    attendance_dir,
    f"attendance_{today}.csv"
)


# ============================================================
# CHECK REQUIRED FILES
# ============================================================

if not os.path.exists(model_path):
    print("ERROR: Model file not found:")
    print(model_path)
    exit()

if not os.path.exists(user_map_path):
    print("ERROR: user_map.csv not found:")
    print(user_map_path)
    exit()

if not os.path.exists(cascade_path):
    print("ERROR: Haar Cascade file not found:")
    print(cascade_path)
    print()
    print("Please place:")
    print("haarcascade_frontalface_default.xml")
    print("inside the main project folder.")
    exit()


# ============================================================
# FACE RECOGNIZER
# ============================================================

recognizer = cv2.face.LBPHFaceRecognizer_create()

print("Loading model from:")
print(model_path)

recognizer.read(model_path)


# ============================================================
# LOAD USER NAMES
# ============================================================

name_dict = {}

with open(user_map_path, "r", newline="", encoding="utf-8") as f:

    for row in csv.reader(f):

        if len(row) >= 2:

            try:
                user_id = int(row[0])
                name = row[1].strip()

                name_dict[user_id] = name

            except ValueError:
                # Ignore invalid rows
                continue


print("Loaded users:")

for user_id, name in name_dict.items():
    print(f"ID {user_id} -> {name}")


# ============================================================
# FACE DETECTOR
# ============================================================

print("Loading Haar Cascade from:")
print(cascade_path)

face_detector = cv2.CascadeClassifier(cascade_path)

if face_detector.empty():

    print("ERROR: Haar Cascade could not be loaded.")
    print(cascade_path)

    exit()


# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("ERROR: Could not open webcam.")
    print("Please check that your camera is connected and available.")

    exit()


attendance = {}

print()
print("Face Recognition Attendance System Started")
print("------------------------------------------")
print("Press ESC to exit")


# ============================================================
# FACE RECOGNITION LOOP
# ============================================================

while True:

    ret, frame = cap.read()

    if not ret:

        print("ERROR: Could not read frame from webcam.")
        break


    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )


    status_msg = ""


    # ========================================================
    # PROCESS DETECTED FACES
    # ========================================================

    for (x, y, w, h) in faces:

        face_region = gray[y:y+h, x:x+w]

        id_, confidence = recognizer.predict(face_region)

        label = "Unknown"


        # ====================================================
        # RECOGNITION
        # ====================================================

        if confidence < 75:

            name = name_dict.get(
                id_,
                "Unknown"
            )


            if name != "Unknown":

                label = f"{name} ({round(confidence, 1)})"


                today = datetime.now().strftime(
                    "%Y-%m-%d"
                )

                now = datetime.now().strftime(
                    "%H:%M:%S"
                )


                key = f"{name}_{today}"


                # ==========================================
                # MARK ATTENDANCE
                # ==========================================

                if key not in attendance:

                    attendance[key] = [
                        name,
                        today,
                        now
                    ]

                    status_msg = (
                        f"Attendance Marked: {name}"
                    )

                else:

                    status_msg = (
                        f"Recognized: {name}"
                    )


        # ====================================================
        # DRAW FACE BOX
        # ====================================================

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )


        # ====================================================
        # DISPLAY NAME
        # ====================================================

        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )


    # ========================================================
    # DISPLAY STATUS
    # ========================================================

    if status_msg:

        cv2.putText(
            frame,
            status_msg,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )


    # ========================================================
    # EXIT MESSAGE
    # ========================================================

    cv2.putText(
        frame,
        "Press ESC to Exit",
        (10, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )


    # ========================================================
    # SHOW CAMERA
    # ========================================================

    cv2.imshow(
        "Face Recognition Attendance",
        frame
    )


    key = cv2.waitKey(1) & 0xFF


    if key == 27:
        break


# ============================================================
# RELEASE CAMERA
# ============================================================

cap.release()

cv2.destroyAllWindows()


# ============================================================
# SAVE ATTENDANCE
# ============================================================

os.makedirs(
    attendance_dir,
    exist_ok=True
)


new_df = pd.DataFrame(
    list(attendance.values()),
    columns=[
        "Name",
        "Date",
        "Time"
    ]
)


if os.path.exists(attendance_path):

    try:

        old_df = pd.read_csv(
            attendance_path
        )

    except Exception:

        old_df = pd.DataFrame(
            columns=[
                "Name",
                "Date",
                "Time"
            ]
        )


    final_df = pd.concat(
        [
            old_df,
            new_df
        ],
        ignore_index=True
    )


    final_df = final_df.drop_duplicates(
        subset=[
            "Name",
            "Date"
        ],
        keep="first"
    )


    final_df.to_csv(
        attendance_path,
        index=False
    )


else:

    new_df.to_csv(
        attendance_path,
        index=False
    )


print()
print("==========================================")
print("Attendance saved successfully!")
print("File:", attendance_path)
print("==========================================")

