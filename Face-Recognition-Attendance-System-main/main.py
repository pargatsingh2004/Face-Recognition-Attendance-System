
import os
import sys
import subprocess


# ============================================================
# FACE RECOGNITION ATTENDANCE SYSTEM
# MAIN FILE
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)


# ============================================================
# FILE PATHS
# ============================================================

COLLECT_FILE = os.path.join(
    SRC_DIR,
    "collect_faces.py"
)

TRAIN_FILE = os.path.join(
    SRC_DIR,
    "train_model.py"
)

RECOGNIZE_FILE = os.path.join(
    SRC_DIR,
    "recognize_attendance.py"
)

CASCADE_FILE = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

TRAINER_FILE = os.path.join(
    BASE_DIR,
    "trainer",
    "trainer.yml"
)

USER_MAP_FILE = os.path.join(
    BASE_DIR,
    "user_map.csv"
)


# ============================================================
# COLORS / DISPLAY
# ============================================================

def clear_screen():

    subprocess.run(
        "cls" if os.name == "nt" else "clear",
        shell=True,
        check=False
    )


def header():

    print("=" * 60)
    print("       FACE RECOGNITION ATTENDANCE SYSTEM")
    print("=" * 60)
    print()


# ============================================================
# CHECK FILES
# ============================================================

def check_project():

    required_files = [
        COLLECT_FILE,
        TRAIN_FILE,
        RECOGNIZE_FILE,
        CASCADE_FILE
    ]

    missing = []

    for file in required_files:

        if not os.path.exists(file):
            missing.append(file)


    if missing:

        print("ERROR: Required files are missing:")
        print()

        for file in missing:
            print("  -", file)

        print()
        return False


    return True


# ============================================================
# RUN PYTHON FILE
# ============================================================

def run_file(file_path):

    print()
    print("=" * 60)
    print("Running:")
    print(file_path)
    print("=" * 60)
    print()


    result = subprocess.run(
        [sys.executable, file_path],
        cwd=BASE_DIR
    )


    if result.returncode != 0:

        print()
        print("=" * 60)
        print("ERROR: Program stopped.")
        print("=" * 60)

        return False


    return True


# ============================================================
# COLLECT FACE DATA
# ============================================================

def collect_faces():

    clear_screen()
    header()

    print("FACE DATA COLLECTION")
    print("-" * 60)
    print()
    print("The webcam will open.")
    print("Enter the student ID and name.")
    print("The system will collect face images.")
    print()


    input("Press ENTER to start...")


    return run_file(
        COLLECT_FILE
    )


# ============================================================
# TRAIN MODEL
# ============================================================

def train_model():

    clear_screen()
    header()

    print("TRAINING FACE RECOGNITION MODEL")
    print("-" * 60)
    print()


    if not os.path.exists(DATASET_DIR):

        print("ERROR: Dataset folder does not exist.")
        print()
        print("First collect face data.")
        print()

        input("Press ENTER to continue...")

        return False


    return run_file(
        TRAIN_FILE
    )


# ============================================================
# START ATTENDANCE
# ============================================================

def start_attendance():

    clear_screen()
    header()

    print("STARTING FACE RECOGNITION ATTENDANCE")
    print("-" * 60)
    print()


    if not os.path.exists(TRAINER_FILE):

        print("ERROR: Trained model not found:")
        print(TRAINER_FILE)
        print()
        print("Please train the model first.")
        print()

        input("Press ENTER to continue...")

        return False


    if not os.path.exists(USER_MAP_FILE):

        print("ERROR: user_map.csv not found:")
        print(USER_MAP_FILE)
        print()
        print("Please collect face data first.")
        print()

        input("Press ENTER to continue...")

        return False


    return run_file(
        RECOGNIZE_FILE
    )


# ============================================================
# COMPLETE SETUP
# ============================================================

def complete_setup():

    clear_screen()
    header()

    print("COMPLETE SETUP")
    print("-" * 60)
    print()
    print("This will perform:")
    print()
    print("1. Face data collection")
    print("2. Model training")
    print("3. Face recognition attendance")
    print()


    choice = input(
        "Continue? (Y/N): "
    ).strip().lower()


    if choice != "y":

        return


    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    clear_screen()
    header()

    print("STEP 1/3 - COLLECT FACE DATA")
    print("-" * 60)
    print()

    if not run_file(COLLECT_FILE):

        input(
            "\nPress ENTER to return to menu..."
        )

        return


    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    clear_screen()
    header()

    print("STEP 2/3 - TRAIN MODEL")
    print("-" * 60)
    print()


    if not run_file(TRAIN_FILE):

        input(
            "\nPress ENTER to return to menu..."
        )

        return


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    clear_screen()
    header()

    print("STEP 3/3 - START ATTENDANCE")
    print("-" * 60)
    print()


    run_file(
        RECOGNIZE_FILE
    )


    print()
    print("=" * 60)
    print("COMPLETE PROCESS FINISHED")
    print("=" * 60)

    input(
        "\nPress ENTER to return to menu..."
    )


# ============================================================
# VIEW PROJECT STATUS
# ============================================================

def project_status():

    clear_screen()
    header()

    print("PROJECT STATUS")
    print("-" * 60)
    print()


    files = {
        "Haar Cascade": CASCADE_FILE,
        "Dataset": DATASET_DIR,
        "User Map": USER_MAP_FILE,
        "Trained Model": TRAINER_FILE,
        "Attendance Folder": os.path.join(
            BASE_DIR,
            "attendance"
        )
    }


    for name, path in files.items():

        if os.path.exists(path):

            print(f"[OK]      {name}")
            print(f"          {path}")

        else:

            print(f"[MISSING] {name}")
            print(f"          {path}")

        print()


    input(
        "Press ENTER to return to menu..."
    )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    if not check_project():

        print()
        input(
            "Press ENTER to exit..."
        )

        return


    while True:

        clear_screen()
        header()

        print("1. Collect Face Data")
        print("2. Train Face Recognition Model")
        print("3. Start Attendance")
        print("4. Complete Setup + Start Attendance")
        print("5. Check Project Status")
        print("6. Exit")
        print()


        choice = input(
            "Enter your choice: "
        ).strip()


        # ----------------------------------------------------
        # OPTION 1
        # ----------------------------------------------------

        if choice == "1":

            collect_faces()

            input(
                "\nPress ENTER to return to menu..."
            )


        # ----------------------------------------------------
        # OPTION 2
        # ----------------------------------------------------

        elif choice == "2":

            train_model()

            input(
                "\nPress ENTER to return to menu..."
            )


        # ----------------------------------------------------
        # OPTION 3
        # ----------------------------------------------------

        elif choice == "3":

            start_attendance()

            input(
                "\nPress ENTER to return to menu..."
            )


        # ----------------------------------------------------
        # OPTION 4
        # ----------------------------------------------------

        elif choice == "4":

            complete_setup()


        # ----------------------------------------------------
        # OPTION 5
        # ----------------------------------------------------

        elif choice == "5":

            project_status()


        # ----------------------------------------------------
        # OPTION 6
        # ----------------------------------------------------

        elif choice == "6":

            clear_screen()

            print("=" * 60)
            print("Thank you for using Face Recognition")
            print("Attendance System")
            print("=" * 60)

            break


        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print()
            print("Invalid choice.")

            input(
                "Press ENTER to continue..."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()
