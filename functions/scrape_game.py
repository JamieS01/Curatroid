import time
from classes.game_library import GameLibrary
from classes.igdb_client import IGDBClient
from tqdm import tqdm

def scrape_game(library,igdb_client,fields=["*"],rate=4, max_retries=3):
    
    games = library.games
    last_request_time = 0

    for game in tqdm(games, desc="Scraping game metadata with IGDB"):
        retries = 0
        response = {}
        search_name = game["gameName"].split('(')[0].strip()

        while retries <= max_retries:

            current_time = time.time()
            wait_time = (1 / rate) - (current_time - last_request_time)

            if wait_time > 0:
                time.sleep(wait_time) 

            try:
                response = igdb_client.query_game(game_name=search_name, fields=fields)
                metadata = response[0]
                last_request_time = time.time()
                break

            except Exception as e:
                retries += 1
                if retries > max_retries:
                    print(f"Failed to fetch metadata for {search_name} after {max_retries} retries.")
                    break
        
        for key, value in metadata.items():
            game[f"{key}"] = value