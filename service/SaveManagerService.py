import xml.etree.ElementTree as et
import os
from pathlib import Path
from model.FarmSave import FarmSave
from datetime import datetime

class SaveManager:

    def __init__(self):
        self.save_path = Path(os.getenv('APPDATA'))/ 'StardewValley' / 'Saves'
    
    def get_all_saves(self):
        saves_found = []

        if not self.save_path.exists():
            return saves_found

        for folder in self.save_path.iterdir():
            if folder.is_dir():
                save_file  = folder / folder.name

                if save_file.exists():
                    data = self._parse_save_file(save_file)

                    if data:
                        saves_found.append(data)
        return saves_found
    
    def _parse_save_file(self, file_path):
        try:
            tree = et.parse(file_path)
            root = tree.getroot()
            player = root.find('player')

            if player is not None:
                return FarmSave(player.findtext('name'),
                                player.findtext('farmName'),
                                int(player.findtext('money')),
                                datetime.fromtimestamp(os.path.getmtime(file_path)),
                                str(file_path.parent))
        except Exception as e:
            print(f"Erro ao ler {file_path.name}: {e}")
        return None