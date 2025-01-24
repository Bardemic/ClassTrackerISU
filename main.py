from send_text import send_Text
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

sections_awaiting = {"C", "D", "F"}

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

sections = response["data"][0]["sections"]

tracker = 0
while True:
    tracker += 1
    for section in sections:
        if(section["number"] in sections_awaiting and section["openSeats"]):
            send_Text(os.environ.get("NUMBER_TO"), "COMS 2280", section["number"])
    print(f"amount of times ran: {tracker}")
    time.sleep(60) #Checks every 60 seconds, will have a better system in the future if I add a website idk
    
