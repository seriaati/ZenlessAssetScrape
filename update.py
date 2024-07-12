import json
from pathlib import Path

from zzz_asset_scrape import hoyowiki

data_path = Path("./data")
data_path.mkdir(exist_ok=True)

disc_icons = hoyowiki.get_disc_drive_icons()
with open(data_path / "disc_icons.json", "w") as f:
    json.dump(disc_icons, f, indent=4)

w_engine_icons = hoyowiki.get_w_engine_icons()
with open(data_path / "w_engine_icons.json", "w") as f:
    json.dump(w_engine_icons, f, indent=4)
