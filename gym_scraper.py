import csv
import os
import typing
from datetime import datetime

import requests
from dotenv import load_dotenv
from lxml import etree

load_dotenv()

URL: str = os.environ["GYM_URL"]
XPATH: str = os.environ["GYM_DATA_XPATH"]

def get_data() -> str:
    content: bytes = requests.get(URL, timeout=5).content
    parsed_html: etree._Element = etree.HTML(content)
    res: list[etree._Element] = parsed_html.xpath(XPATH)
    return res[0].text.split(" ")[0]

def get_datetime() -> str:
    return datetime.now().isoformat(sep=" ", timespec="seconds")

def write_data(data: str, now: str) -> None:
    with open("gym_data.csv", "a") as f:
        writer: csv._writer = csv.writer(f)
        writer.writerow([now, data])

def main() -> int:
    data = get_data()
    now = get_datetime()
    write_data(data, now)
    return 0

if __name__ == "__main__":
    exit(main())
