from dataclasses import dataclass
from datetime import datetime
import os

@dataclass
class FarmSave:

    player_name: str
    farm_name: str
    money: int
    last_played: datetime
    folder_path:str

    @property
    def save_id(self) -> str:

        return os.path.basename(self.folder_path)
    
    def to_dict(self):
        return {
            "player": self.player_name,
            "farm": self.farm_name,
            "money": f"G$ {self.money:,}",
            "last_played": self.last_played.strftime("%d/%m/%Y %H:%M")
        }