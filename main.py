from fastapi import FastAPI
import datetime, pytz, random

app = FastAPI()

STATUS_CODE = 200
NAME = "adelaja_qowiyyu"
TRACK = "backend"
GITHUB_REPO_URL = "https://github.com/adelajaOlamilekan/HNG10"
GITHUB_FILE_URL = "https://github.com/adelajaOlamilekan/HNG10/blob/main/task1/create_endpoint.py"
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@app.get("/api")
async def get_data(slack_name: str = NAME, track: str = TRACK):
    current_time_utc = datetime.datetime.now(pytz.utc)
    offset_minutes = random.randint(-2, 2)
    current_time_with_offset = current_time_utc + datetime.timedelta(minutes=offset_minutes)
    current_time_with_offset = current_time_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")

    user_data  = {
                    "slack_name": slack_name,
                    "current_day": weekday[datetime.datetime.today().weekday()],
                    "utc_time": current_time_with_offset,
                    "track": track,
                    "github_file_url": GITHUB_FILE_URL,
                    "github_repo_url": GITHUB_REPO_URL,
                    "status_code": STATUS_CODE
                }
    
    return user_data