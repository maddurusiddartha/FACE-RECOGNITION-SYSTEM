import cv2
from deepface import DeepFace
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ---------------------- GOOGLE SHEET SETUP ----------------------
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your sheet by name
sheet = client.open("attendance").sheet1  # replace "Attendance" with your sheet name

# ---------------------- LOAD KNOWN FACES ----------------------
KNOWN_FACES_DIR = "known_faces"
known_faces = {}
for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        name = os.path.splitext(filename)[0]
        path = os.path.join(KNOWN_FACES_DIR, filename)
        known_faces[name] = path

# Keep track of students already marked to avoid duplicates
marked_students = set()

# ---------------------- START CAMERA ----------------------
cap = cv2.VideoCapture(0)

print("Starting face recognition. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    for student_name, img_path in known_faces.items():
        try:
            result = DeepFace.verify(frame, img_path, enforce_detection=False)
            if result["verified"] and student_name not in marked_students:
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")

                # Append to Google Sheet
                sheet.append_row([student_name, date_str, time_str])
                print(f"Marked {student_name} at {date_str} {time_str}")
                marked_students.add(student_name)

        except Exception as e:
            pass  # ignore errors for unmatched faces

    # Display the camera (optional, can remove)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
