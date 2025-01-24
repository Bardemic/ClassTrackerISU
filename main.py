from send_text import send_Text
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.classes.iastate.edu/api/courses/search"
payload = {
    "courseId": "228",
    "department": "COMS - Computer Science",
    "academicPeriodId": "ACADEMIC_PERIOD-2025Spring",
    "openSeats": False,
}
headers = {
    "Content-Type": "application/json"
}

response = (requests.post(url, json=payload, headers=headers)).json()

print(response.keys())

sections = response["data"][0]["sections"]

for section in sections:
    if(section["openSeats"]):
        print(section["number"])
    

#send_Text(os.environ.get("NUMBER_TO"), "COMS 2280", "A")