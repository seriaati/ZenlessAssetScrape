from typing import Any

import requests


def get_agent_data() -> dict[str, Any]:
    url = "https://api.dotgg.gg/cgfw/getgacha?game=zenless&type=characters"
    data = requests.get(url).json()
    result: dict[str, Any] = {}
    for agent in data:
        result[agent["id"]] = {
            "id": agent["id"],
            "name": agent["name"],
            "full_name": agent["fullName"],
            "icon_url": f"https://static.dotgg.gg/zenless/{agent['icon']}",
            "faction": agent["faction"],
            "element": agent["element"][0],
            "beta": True if agent["rarity"] == "0" else False,
        }
    return result
