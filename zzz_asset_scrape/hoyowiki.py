from typing import Any

import requests
from fake_useragent import UserAgent

ua = UserAgent()


def get_disc_drives() -> dict[str, Any]:
    url = "https://sg-wiki-api.hoyolab.com/hoyowiki/zzz/wapi/get_entry_page_list"
    headers = {
        "Origin": "https://wiki.hoyolab.com",
        "Referer": "https://wiki.hoyolab.com/",
        "X-Rpc-Language": "en-us",
        "X-Rpc-Wiki_app": "zzz",
        "User-Agent": ua.random,
    }
    payload = {
        "menu_id": "12",
        "page_num": 1,
        "page_size": 30,
    }
    data = requests.post(url, headers=headers, json=payload).json()
    return data["data"]


def get_disc_drive_icons() -> dict[str, str]:
    disc_drives = get_disc_drives()["list"]
    result: dict[str, str] = {}
    for drive in disc_drives:
        result[drive["name"]] = drive["icon_url"]
    return result
