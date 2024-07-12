import json
from pathlib import Path
from typing import Any

from zzz_asset_scrape import dotgg, hoyowiki

data_path = Path("./data")
data_path.mkdir(exist_ok=True)

data_lite_path = Path("./data/lite")
data_lite_path.mkdir(exist_ok=True)


def write_data(filename: str, data: Any):
    with open(data_path / filename, "w") as f:
        json.dump(data, f, indent=4)
    with open(data_lite_path / filename, "w") as f:
        json.dump(data, f)


disc_icons = hoyowiki.get_disc_drive_icons()
write_data("disc_icons.json", disc_icons)

w_engine_icons = hoyowiki.get_w_engine_icons()
write_data("w_engine_icons.json", w_engine_icons)

agent_data = dotgg.get_agent_data()
write_data("agent_data.json", agent_data)
