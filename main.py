from os import environ
from moodle_api import MoodleAPI
from todoist_api import TodoistAPI


def main():
    # Andmed Moodlega ühendamiseks
    token_moodle = environ["MOODLE_TOKEN"]
    token_trello = environ["TRELLO_TOKEN"]
    API_key_trello = environ["TRELLO_API_KEY"]
    token_todoist = environ["TODOIST_API_TOKEN"]
    url = "https://moodle.ut.ee/webservice/rest/server.php"
    funktsioon = "core_calendar_get_calendar_upcoming_view"
    
    # Loon suhtluse API-dega
    moodle_api = MoodleAPI(url, token_moodle)
    todoist_api = TodoistAPI("https://api.todoist.com/rest/v2/tasks", token_todoist)


if __name__ == "__main__":
    main()