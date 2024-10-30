#from moodle import Moodle, Mdl
#from moodle.core.webservice import BaseWebservice
from os import environ
from requests import post

class MoodleAPI:
    def __init__(self, url, token):
        self.url = url
        self.token = token
    
    # Kutsub Moodle'i API-d kindla argumendiga vastavalt küsitavale infole
    def call(self, funktsioon, data):
        argumendid = {
            "wstoken": self.token,
            "wsfunction": funktsioon,
            "moodlewsrestformat": "json"
        }

        vastus = post(self.url, params=argumendid, data=data)
        if vastus.status_code == 200:
            vastus2 = vastus.json()
        else:
            vastus2 = f"Kutse ebaõnnestus, status code f{vastus.status_code}"

        return vastus2

    # Leiab ja prindib kõik viimatised kursused Moodle'is
    def hangi_kursused(self):
        kursuste_list = self.call("core_course_get_recent_courses", {})
        for kursus in kursuste_list:
            id = kursus["id"]
            nimi = kursus["fullname"]
            kood = kursus["shortname"]
            print(nimi, id)

    # Leiab ja prindib kõik Moodle'i kalendri sündmused
    def hangi_kalendri_info(self):
        data = {
            "options[userevents]": 1,
            "options[siteevents]": 1,
            "options[timestart]": 1730255400,
            "options[timeend]": 1732069800,
            "events[courseids][0]": 7550,
            "events[courseids][1]": 1755,
            "events[courseids][2]": 12774,
            "events[courseids][3]": 10892,
            "events[courseids][4]": 500,
            "events[courseids][5]": 8434
        }
        moodle_vastus = self.call("core_calendar_get_calendar_events", data)
        sundmused = moodle_vastus["events"]
        for sundmus in sundmused:
            print(sundmus["name"])



def main():
    # Andmed Moodlega ühendamiseks
    token = environ["MOODLE_TOKEN"]
    url = "https://moodle.ut.ee/webservice/rest/server.php"
    funktsioon = "core_calendar_get_calendar_upcoming_view"

    moodle_api = MoodleAPI(url, token)

    # Proovin kutsuda call funktsiooni, et saada mingigi vastus Moodlelt
    try:
        moodle_api.hangi_kalendri_info()
        #moodle_api.hangi_kursused()
    except Exception as viga:
        print(f"Error: {viga}")

if __name__ == "__main__":
    main()