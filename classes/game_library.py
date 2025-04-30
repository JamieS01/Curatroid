import os
import csv
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import filedialog

class GameLibrary:

    def __init__(self, frontend, use_default=True):

        if not frontend:
            raise ValueError("You must specify a valid frontend.")
        
        self.frontend = frontend
        self.games = []
        self.gamelist_path = self.get_gamelist_path(use_default)
        self.parse_gamelist()

    def get_gamelist_path(self, use_default):
        
        home = os.path.expanduser("~")

        if use_default:
            if self.frontend == "Launchbox":
                return os.path.join(home, "Launchbox", "Metadata", "Files.xml")
            else:
                raise ValueError(f"No default gamelist for {self.frontend}")
        else:
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename(title=f"Select {self.frontend} game list")
            root.destroy()

            if not path:
                raise ValueError("No file selected.")
            return path
    
    def parse_gamelist(self):

        if not self.gamelist_path:
            raise ValueError("No gamelist path provided.")
        
        if self.frontend == "Launchbox":
            
            try:
                tree = ET.parse(self.gamelist_path)
            except (FileNotFoundError, ET.ParseError) as e:
                raise ValueError(f"Failed to parse gamelist: {e}")
            
            root = tree.getroot()

            for game in root.findall("File"):
                self.games.append({
                    "gameName": game.findtext("GameName", default=None),
                    "fileName": game.findtext("FileName", default=None),
                    "platform": game.findtext("Platform", default=None),
                    "metadata": {}
                })

        else:
            raise ValueError("Could not parse gamelist due to invalid frontend.")
        
    def export_metadata(self):

        if not self.games:
            raise ValueError("No games in game list")
        
        with open('meta.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)

            all_keys = set()
            for game in self.games:
                all_keys.update(game.keys())
            
            # Write the header row with all keys
            writer.writerow(all_keys)
            
            # Write each game's values in the order of the header keys
            for game in self.games:
                writer.writerow([game.get(key, "") for key in all_keys])
