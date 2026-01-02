the main purpose of the project is to recognize a face that already exists on its database and enter the respectives names ,timestamps to a google sheet. since i cant upload my personel credentials i will tell you how to link google sheets to the project. ( process below)

📊 Google Sheets Setup for Attendance Logging
This project logs attendance automatically into a Google Sheet.
For security reasons, Google API credentials are NOT included in this repository.
Follow the steps below to set it up on your own system.

🔹 Step 1: Create a Google Sheet

Go to https://sheets.google.com

Click Blank

Rename the sheet to:

attendance


In Row 1, add headers:

Name | Time


Close the sheet (it auto-saves)

🔹 Step 2: Create a Google Cloud Project

Open https://console.cloud.google.com/

Click Select a project → New Project

Project name:

Face-Attendance


Click Create

Select the project once created

🔹 Step 3: Enable Google Sheets API

In Google Cloud Console:

Go to APIs & Services → Library

Search for:

Google Sheets API


Click it → Enable

🔹 Step 4: Create Service Account Credentials

Go to APIs & Services → Credentials

Click Create Credentials → Service Account

Service account name:

attendance-bot


Click Create and Continue

Skip roles → Click Done

🔹 Step 5: Generate JSON Key File

Open the created service account

Go to Keys tab

Click Add Key → Create new key

Select JSON

Download the file

Rename it to:

credentials.json


Place it inside the project folder:

face-attendance/credentials.json


⚠ Do NOT upload this file to GitHub

🔹 Step 6: Share Google Sheet with Service Account

Open your attendance Google Sheet

Click Share

Copy the client_email from credentials.json
(looks like: attendance-bot@project-id.iam.gserviceaccount.com)

Paste it into Share

Give Editor access

Click Done

🔹 Step 7: Install Required Python Libraries

Run the following command in the project folder:

pip install gspread oauth2client deepface opencv-python numpy pandas tensorflow tf-keras openpyxl

🔹 Step 8: Run the Project
python attendance.py

What happens:

Camera opens automatically

Faces are matched with images in students/ folder

Attendance is written directly to Google Sheet

Duplicate entries are avoided (one entry per student per session)

🔐 Security Note

credentials.json is ignored from GitHub

Each user must create their own credentials

This prevents misuse of Google APIs
