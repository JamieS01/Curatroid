import requests
import configparser
import time

class IGDBClient:

    def __init__(self, config_path="config.ini"):

        self.config_path = config_path
        self.session = requests.Session()
        self.access_token = None
        self.client_id = None
        
        self.load_credentials()

    def load_credentials(self):

        config = configparser.ConfigParser()
        config.read(self.config_path)

        self.client_id = config['IGDB']['client_ID']
        client_secret = config['IGDB']['client_secret']

        self.access_token = self.get_access_token(client_secret)

    def get_access_token(self, client_secret):

        url = "https://id.twitch.tv/oauth2/token"

        params = {
            "client_id": self.client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }

        response = self.session.post(url, params=params)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to authenticate to IGDB. Status: {response.status_code} {response.text}")

        return response.json()["access_token"]
    
    def query_game(self, game_name, fields="*",limit_per_game=1):

        fields_clause = ", ".join(fields)

        url = "https://api.igdb.com/v4/games"

        headers = {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {self.access_token}"
        }

        data = f'search "{game_name}"; fields {fields_clause}; limit {limit_per_game};'

        response = self.session.post(url, headers=headers, data=data)

        if response.status_code != 200:
            print(f"Warning: Failed to fetch data for {game_name}")
            return None

        return response.json()