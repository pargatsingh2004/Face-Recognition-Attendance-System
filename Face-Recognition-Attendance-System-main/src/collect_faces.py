
import cv2
import os


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ============================================================
# HAAR CASCADE PATH
# ============================================================

cascade_path = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)


# ============================================================
# CHECK HAAR CASCADE
# ============================================================

if not os.path.exists(cascade_path):

    print("ERROR: Haar Cascade file not found:")
    print(cascade_path)
    print()
    print("Please place:")
    print("haarcascade_frontalface_default.xml")
    print("inside the main project folder.")

    exit()


face_detector = cv2.CascadeClassifier(
    cascade_path
)


if face_detector.empty():

    print("ERROR: Haar Cascade could not be loaded:")
    print(cascade_path)

    exit()


print("Haar Cascade loaded successfully.")


# ============================================================
# USER INFORMATION
# ============================================================

user_id = input("Enter user id (numeric): ")

try:
    user_id = int(user_id)

except ValueError:

    print("ERROR: User ID must be a number.")

    exit()


user_name = input("Enter user name: ").strip()


if not user_name:

    print("ERROR: User name cannot be empty.")

    exit()


# ============================================================
# DATASET DIRECTORY
# ============================================================

dataset_dir = os.path.join(
    BASE_DIR,
    "dataset"
)

user_dir = os.path.join(
    dataset_dir,
    f"user_{user_id}"
)


os.makedirs(
    user_dir,
    exist_ok=True
)


# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0)


if not cap.isOpened():

    print("ERROR: Could not open webcam.")

    exit()


print()
print("Starting face collection...")
print(f"User ID: {user_id}")
print(f"User Name: {user_name}")
print()
print("Look at the camera.")
print("Move your face slightly so different positions are captured.")
print("Press ESC to stop.")
print()


count = 0


# ============================================================
# FACE COLLECTION
# ============================================================

while True:

    ret, frame = cap.read()

    if not ret:

        print("ERROR: Could not read camera frame.")

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


    for (x, y, w, h) in faces:

        count += 1


        face_image = gray[
            y:y + h,
            x:x + w
        ]


        image_path = os.path.join(
            user_dir,
            f"{count}.jpg"
        )


        cv2.imwrite(
            image_path,
            face_image
        )


        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )


        cv2.putText(
            frame,
            f"{user_name} - {count}/100",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )


        break


    cv2.putText(
        frame,
        f"Images: {count}/100",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )


    cv2.putText(
        frame,
        "Press ESC to Exit",
        (10, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )


    cv2.imshow(
        "Face Collection",
        frame
    )


    key = cv2.waitKey(1) & 0xFF


    if key == 27:

        break


    if count >= 100:

        print()
        print("100 face images collected successfully.")
        break


# ============================================================
# RELEASE CAMERA
# ============================================================

cap.release()

cv2.destroyAllWindows()


# ============================================================
# SAVE USER MAPPING
# ============================================================

user_map_path = os.path.join(
    BASE_DIR,
    "user_map.csv"
)


# Read existing users if available
users = {}


if os.path.exists(user_map_path):

    with open(
        user_map_path,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue


            parts = line.split(",", 1)


            if len(parts) == 2:

                try:

                    existing_id = int(
                        parts[0].strip()
                    )

                    existing_name = parts[1].strip()

                    users[existing_id] = existing_name

                except ValueError:

                    continue


# Add/update current user
users[user_id] = user_name


# Write user_map.csv
with open(
    user_map_path,
    "w",
    encoding="utf-8",
    newline=""
) as f:

    for uid, name in sorted(users.items()):

        f.write(
            f"{uid},{name}\n"
        )


print()
print("==========================================")
print("Face collection completed!")
print(f"User ID   : {user_id}")
print(f"User Name : {user_name}")
print(f"Images    : {count}")
print(f"Dataset   : {user_dir}")
print(f"User Map  : {user_map_path}")
print("==========================================")

