# Automated Attendance System using Computer Vision

## 📌 Overview
This project is an automated attendance system using Computer Vision and Python. The system captures and stores student images along with their details in a database. It then recognizes students using facial recognition and marks their attendance in a CSV file. At the end of the day, an attendance report is sent to faculty via email.

## ⚙️ Features
- 📷 **Face Recognition**: Identifies students using OpenCV and a trained model.
- 📊 **Attendance Tracking**: Marks attendance in a CSV file.
- 🖼️ **Image Storage**: Stores student images in the database.
- 📧 **Email Report**: Sends daily attendance reports to faculty.
- 🖥 **Web Interface**: Allows interaction through a web-based interface.

## 🛠️ Tech Stack
- **Python** 🐍
- **OpenCV** 👁️ (For face detection & recognition)
- **Dlib** 📏 (Facial feature extraction)
- **Flask** 🌐 (Web interface)
- **Pandas** 📊 (For attendance data handling)
- **Smtplib** 📩 (For email functionality)

## 🏆 How It Works
1. **Student Registration**: Capture student images and store in the database.
2. **Face Recognition**: Detect and recognize students using the camera.
3. **Mark Attendance**: Automatically update `attendance.csv` when a student is recognized.
4. **Email Report**: Generate a report and send it to faculty at the end of the day.

