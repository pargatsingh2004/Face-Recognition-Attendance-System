
# 🎯 Face Recognition Attendance System

### Automated Attendance Management Using Python, OpenCV & Machine Learning

A Python-based **Face Recognition Attendance System** that automates attendance recording using computer vision and machine learning.

The system captures facial images through a webcam, trains a face recognition model, identifies registered individuals, and records attendance automatically in CSV files.

This project demonstrates practical applications of **Python, OpenCV, Machine Learning, Computer Vision, and Data Processing**.

---

## 📌 Project Overview

Traditional attendance systems require manual entry, which can be time-consuming and prone to errors.

The Face Recognition Attendance System provides an automated solution using facial recognition technology.

The application uses:

- Haar Cascade Classifier for face detection
- LBPH (Local Binary Patterns Histograms) for face recognition
- OpenCV for webcam integration and image processing
- NumPy for numerical operations
- Pandas for attendance data management
- CSV files for storing attendance records

## ✨ Features

- Real-time face detection using a webcam
- Face dataset collection for registered users
- Face recognition using the LBPH algorithm
- Training a facial recognition model
- Automatic attendance recording
- Date and time tracking
- CSV-based attendance management
- Recognition confidence threshold
- Unknown face detection
- Simple command-line interface
- Local processing without cloud services

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| OpenCV | Face detection and recognition |
| Machine Learning | LBPH face recognition |
| Haar Cascade | Facial detection |
| NumPy | Numerical computation |
| Pandas | Attendance data processing |
| CSV | Attendance storage |
| VS Code | Development environment |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
Face-Recognition-Attendance-System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── haarcascade_frontalface_default.xml
│
├── src/
│   ├── collect_faces.py
│   ├── train_model.py
│   └── recognize_attendance.py
│
├── dataset/
│   └── (Collected face images)
│
├── trainer/
│   └── trainer.yml
│
├── attendance/
│   └── (Generated attendance CSV files)
│
└── user_map.csv
```

**Note:** The dataset, trained model, user mapping, and attendance files may be generated locally. They should not contain real personal data in a public repository.

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/pargatsingh2004/Face-Recognition-Attendance-System.git
```

### 2. Navigate to the Project

```bash
cd Face-Recognition-Attendance-System
```

### 3. Create a Virtual Environment

Python 3.11 is recommended.

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
```

### 4. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Example `requirements.txt`:

```text
numpy==1.26.4
pandas==2.2.3
opencv-contrib-python==4.10.0.84
Pillow==10.4.0
```

`opencv-contrib-python` is required because the application uses the OpenCV LBPH face recognizer.

## 🚀 How to Run the Project

Start the main application:

```bash
python main.py
```

The application provides access to the face collection, model training, and attendance recognition workflows.

### Step 1: Collect Face Images

```bash
python src/collect_faces.py
```

- Connect a working webcam.
- Register the individual.
- Capture facial images.
- Store the collected images in the dataset folder.

### Step 2: Train the Recognition Model

```bash
python src/train_model.py
```

The application trains an LBPH face recognition model using the collected facial images.

The trained model is stored in:

```text
trainer/trainer.yml
```

### Step 3: Recognize Faces and Mark Attendance

```bash
python src/recognize_attendance.py
```

The system:

1. Opens the webcam.
2. Detects faces in video frames.
3. Compares detected faces against the trained model.
4. Identifies recognized individuals.
5. Records attendance with date and time.
6. Saves attendance records in CSV format.

## 🧠 Machine Learning Algorithm

### LBPH — Local Binary Patterns Histograms

LBPH is a traditional computer vision face recognition algorithm.

It works by:

1. Converting face images into grayscale.
2. Extracting local texture patterns.
3. Generating histograms representing facial features.
4. Comparing extracted features with trained samples.
5. Predicting the closest matching identity.

### Why LBPH?

- Suitable for educational computer vision projects
- Relatively lightweight
- Can run on a CPU
- Does not require GPU acceleration
- Supports local face recognition

**Limitations:** Recognition accuracy can be affected by lighting, camera quality, face angle, and changes in appearance. LBPH is not a deep learning algorithm and does not provide built-in anti-spoofing protection.

## 📊 Attendance Management

The application stores attendance information in CSV format.

An example attendance record:

| Name | Date | Time | Status |
|------|------|------|--------|
| Student A | 2026-10-30 | 09:15:20 | Present |
| Student B | 2026-10-30 | 09:17:35 | Present |

The example above is illustrative; actual CSV columns depend on the implementation.

## 🔐 Privacy and Security

Facial images and biometric identifiers are sensitive personal data.

Recommended precautions:

- Collect explicit consent before registering faces.
- Do not upload real student face images to public repositories.
- Keep attendance records and identity mappings private.
- Restrict access to the trained recognition model.
- Delete stored biometric data when no longer needed.
- Use the system for authorized attendance purposes only.

## 🧪 Troubleshooting

### ModuleNotFoundError: No module named 'cv2'

Install OpenCV:

```bash
python -m pip install opencv-contrib-python
```

### ModuleNotFoundError: No module named 'pandas'

```bash
python -m pip install pandas
```

### Camera Not Opening

- Check whether the webcam is connected.
- Allow camera access in Windows settings.
- Close other applications using the webcam.

### LBPH Recognizer Not Available

Make sure `opencv-contrib-python` is installed.

```bash
python -c "import cv2; print(hasattr(cv2.face, 'LBPHFaceRecognizer_create'))"
```

Expected output:

```text
True
```

### Model Not Found

Collect face images and train the recognition model before starting attendance recognition.

## 🔮 Future Enhancements

- Flask-based web dashboard
- Student registration and management
- SQLite or MySQL database integration
- Attendance reports and analytics
- Excel and PDF report export
- Deep learning-based face recognition
- Liveness detection
- Role-based administrator login
- Attendance search and filtering
- Email attendance notifications
- Recognition accuracy evaluation
- Responsive web interface

## 🎓 Learning Outcomes

This project provides practical experience in:

- Python programming
- Computer vision
- Image processing
- Machine learning fundamentals
- OpenCV development
- Facial detection and recognition
- CSV file operations
- Real-time webcam processing
- Git and GitHub version control

## 👨‍💻 Author

**Pargat Singh**

Computer Science Engineering | Python Developer | Data Science & Machine Learning Enthusiast

GitHub: [pargatsingh2004](https://github.com/pargatsingh2004)

## 🔗 GitHub Repository

[Face Recognition Attendance System](https://github.com/pargatsingh2004/Face-Recognition-Attendance-System)

## 📄 License

No license has been specified yet. Add a `LICENSE` file if you want to define how others may use, modify, and distribute this project.

---

⭐ If you find this project useful, consider giving the repository a star!
