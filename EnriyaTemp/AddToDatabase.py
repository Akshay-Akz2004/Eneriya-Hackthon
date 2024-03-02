
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facegaurd-attendx-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Abhinav",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Gautham",
            "major": "Electrical",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Saurav",
            "major": "Robotics",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "123456":
        {
            "name": "Akshay",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)