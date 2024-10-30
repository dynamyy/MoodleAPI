from moodle import Moodle, Mdl
from moodle.core.webservice import BaseWebservice
import os
from requests import get, post

def main():
    # Andmed Moodlega ühendamiseks
    token = os.environ["MOODLE_TOKEN"]
    url = "https://moodle.ut.ee/webservice/rest/server.php"
    funktsioon = "core_calendar_get_calendar_upcoming_view"

    # Proovin kutsuda call funktsiooni, et saada mingigi vastus Moodlelt
    try:
        vastus = hangi_kalendri_info(url, token)
        #print(vastus)
    except Exception as viga:
        print(f"Error: {viga}")



# Leiab ja prindib kõik Moodle'i kalendri sündmused
def hangi_kalendri_info(url, token):
    moodle_vastus = call(url, token, "core_calendar_get_calendar_events")
    sundmused = moodle_vastus["events"]
    for sundmus in sundmused:
        print(sundmus["name"])


# Leiab ja prindib kõik viimatised kursused Moodle'is
def hangi_kursused(url, token):
    kursuste_list = call(url, token, "core_course_get_recent_courses")
    for kursus in kursuste_list:
        id = kursus["id"]
        nimi = kursus["fullname"]
        kood = kursus["shortname"]
        print(nimi, id)



# Kutsub Moodle'i API-d kindla argumendiga vastavalt küsitavale infole
def call(url, token, funktsioon):
    argumendid = {
        "wstoken": token,
        "wsfunction": funktsioon,
        "moodlewsrestformat": "json"
    }
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
        #"eventid":["7550", "1755", "12774", "10892", "500", "8434"],
    }

    vastus = post(url, params=argumendid, data=data)
    if vastus.status_code == 200:
        vastus2 = vastus.json()
    else:
        vastus2 = f"Kutse ebaõnnestus, status code f{vastus.status_code}"

    return vastus2

if __name__ == "__main__":
    main()