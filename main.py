


from fastapi import FastAPI



from datetime import datetime

app = FastAPI()

STATUS_CODE = 200
NAME = "adelaja_qowiyyu"
TRACK = "backend"
GITHUB_REPO_URL = "https://github.com/adelajaOlamilekan/HNG10"
GITHUB_FILE_URL = "https://github.com/adelajaOlamilekan/HNG10/blob/main/main.py"
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@app.get("/api")
async def get_data(slack_name: str = NAME, track: str = TRACK):
    current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    user_data  = {
                    "slack_name": slack_name,
                    "current_day": weekday[datetime.today().weekday()],
                    "utc_time": current_time_utc,
                    "track": track,
                    "github_file_url": GITHUB_FILE_URL,
                    "github_repo_url": GITHUB_REPO_URL,
                    "status_code": STATUS_CODE
                }
    
    return user_data