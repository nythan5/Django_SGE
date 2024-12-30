import requests

class Notify:

    def __init__ (self):
        self.__base_url = "https://webhook.site"

    def send_event(self,data):
        requests.post(
            url=f'{self.__base_url}/83c22238-8574-45db-a1d0-50c72ea6ef02',
            json=data,
        )

        