from os import environ, path
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

    # Config fail
    if path.isfile("config.txt"):
        # Loen kasutaja eelistused
        with open("config.txt", "r", encoding="UTF-8") as fail:
            failisisu = fail.readlines()
        # Vajadusel uuendan vaadeldavaid kursuseid kasutaja eelistustele vastavalt
        vaadeldavate_kursuste_list = []
        for kursuse_id in failisisu[0].strip().split(", "):
            vaadeldavate_kursuste_list.append(int(kursuse_id))
            moodle_api.vaadeldavad_kursused = vaadeldavate_kursuste_list
        if moodle_api.vaadeldavad_kursused != moodle_api.kursuste_id_list:
            moodle_api.kalendri_info = moodle_api.hangi_kalendri_info(moodle_api.vaadeldavad_kursused)
    else:
        print("Config faili, pole, loon selle")

        #Lisan vaadeldavad kursused
        rida_kursused = ""
        for kursuse_id in moodle_api.kursuste_id_list:
            rida_kursused += str(kursuse_id) + ", "
        rida_kursused = rida_kursused[:-2]

        with open("config.txt", "w", encoding="UTF-8") as fail:
            failisisu = f"{rida_kursused}"
            fail.write(failisisu)
    
    # Saadan ülesanded Todoist-i
    for sundmus in moodle_api.kalendri_info:
        ulesande_nimi = sundmus[0]
        ulesande_kursus = moodle_api.kursuste_info[sundmus[1]][1]

        todoist_api.loo_kaart(ulesande_nimi)



    


if __name__ == "__main__":
    main()