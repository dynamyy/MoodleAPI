# MoodleGet
convenient way to get data through Moodle's API

## Setup
Install the package using pip:<br>
pip install MoodleGet

Now you can open your project and import the MoodleAPI class<br>
from MoodleGet import MoodleAPI


### Initialising the class
url = "https://yourMoodle/webservice/rest/server.php"<br>
token = your Moodle's API token<br>
moodle = MoodleAPI(url, token)

## Available methods

#### .call(function, data, params)
Send a post request to Moodle through their API system. Returns the response from Moodle in json format
|argument|expected type|required|default value|
|:------:|:-----------:|:------:|:-----------:|
|function|string       |yes     |-            |
|data    |dict         |no      |{"wstoken": self.token,<br>"wsfunction": function,<br>"moodlewsrestformat": "json"}|
|params|dict|no|{}|

#### .get_courses()
Find all the courses that the user can see.

Returns a tuple (courses_dict, course_id_list), where

courses_dict is a dictionary, where keys are the course id-s and every key has a list set to it's value. The list contains [course's code, course's name in a readable way]

course_id_list is a list that has all the course's id-s as it's elements for convenient access

#### .get_calendar_events(courses_list)
Finds all the calendar events in Moodle calendar in the time period now until 3 weeks from now.<br>
Returns a list of the events, where every element of the list is another list containing: [event_id, name, events_course_id, exercise_type, event_starttime]
|argument    |expected type|required|default value|
|:----------:|:-----------:|:------:|:-----------:|
|courses_list|list         |yes     |-            |

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.