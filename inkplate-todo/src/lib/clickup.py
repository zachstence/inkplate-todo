import urequests
import json

from config import config
from task import Task

API_TOKEN = config["clickup"]["apiToken"]
LIST_ID = config["clickup"]["listId"]

HEADERS = { "Authorization": API_TOKEN }

def get_tasks() -> list[Task]:
    response = urequests.get(f"https://api.clickup.com/api/v2/list/{LIST_ID}/task", headers=HEADERS)
    raw_tasks = json.loads(response.text)["tasks"]
    
    tasks = [_convert_task(raw_task) for raw_task in raw_tasks]
    return tasks

def _convert_task(raw_task: dict) -> Task | None:
    id = raw_task["id"]
    complete = False # TODO By default, I don't think clickup will return tasks that are done
    title = raw_task["name"]

    if id is None or complete is None or title is None:
        print(f"Failed to convert clickup task {raw_task}")
        return None

    return Task(id, False, title)
