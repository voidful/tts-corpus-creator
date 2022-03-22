import requests
from requests.compat import urljoin


class AndroidTTS:

    def __init__(self, server_address):
        self.server_address = server_address

    def __call__(self, text, outfile, lang='en_US'):
        data = {'phrase': text, 'language': lang}
        response = requests.get(urljoin(self.server_address, 'tts.wav'), params=data)
        with open(f'{outfile}.wav', "wb") as f_out:
            f_out.write(response.content)
