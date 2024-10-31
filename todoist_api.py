from requests import post

class TodoistAPI:
    def __init__(self, url, token):
        self.token = token
        self.url = url

    def loo_kaart(self, pealkiri:str, kirjeldus:str, sildid:list):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        data = {
            "content": pealkiri,
            "description": kirjeldus,
            "project_id": "2342580103",
            "labels": sildid
        }

        vastus = post(self.url, headers=headers, json=data)
        if vastus.status_code == 200:
            print("Kaart lisatud")
        else:
            print(f"ei saand ühendust todoistiga: {vastus.text}")