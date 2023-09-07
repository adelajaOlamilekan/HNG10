from fastapi import FastAPI
import datetime, pytz, random

app = FastAPI()

STATUS_CODE = 200
NAME = "adelaja_qowiyyu"
TRACK = "backend"
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@app.get("/api")
async def get_data(slack_name: str | None = NAME, track: str | None = TRACK, status_code: int | None = 200):
    current_time_utc = datetime.datetime.now(pytz.utc)
    offset_minutes = random.randint(-2, 2)
    current_time_with_offset = current_time_utc + datetime.timedelta(minutes=offset_minutes)
    current_time_with_offset = current_time_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")

    user_data  = {
                    "slack_name": slack_name,
                    "current_day": weekday[datetime.datetime.today().weekday()],
                    "utc_time": current_time_with_offset,
                    "track": track,
                    "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                    "github_repo_url": "https://github.com/username/repo",
                    "status_code": status_code
                }
    
    return user_data