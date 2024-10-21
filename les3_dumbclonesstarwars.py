import json
import csv
from io import TextIOWrapper

with open("in.json", "r") as in_file:
    data: str = json.load(in_file)


def filtration(data) -> str:
    for entry in data:
        phone: str = entry.get('phoneNumber', '')
        user_agent: str = entry.get('userAgent', '')
        if (phone.startswith('+1') or phone.startswith('1')) and '4.0 Safari' in user_agent:
            yield {
                'name': entry.get('name', ''),
                'address': entry.get('address', ''),
                'email': entry.get('email', '')
            }


def writer() -> str:
    with open("out.csv", "w", newline='') as out_file:
        fieldnames: list[str] = ['name', 'address', 'email']
        writer: str = csv.DictWriter(out_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in filtration(data):
            writer.writerow(item)


filtration(data)
writer()
