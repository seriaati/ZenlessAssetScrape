import json
from pathlib import Path

from zzz_asset_scrape import hoyowiki

data_path = Path("./data")
data_path.mkdir(exist_ok=True)

disc_icons = hoyowiki.get_disc_drive_icons()
with open(data_path / "disc_icons.json", "w") as f:
    json.dump(disc_icons, f, indent=4)
