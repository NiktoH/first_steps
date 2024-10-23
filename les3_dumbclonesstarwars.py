import json
import csv
from typing import Dict, List, Generator


def read_json_file() -> List[Dict]:
    with open("in.json", "r") as in_file:
        data = json.load(in_file)
    return data


def filtration_users(data: List[Dict]) -> Generator[Dict[str, str], None, None]:
    for entry in data:
        phone: str = entry.get('phoneNumber', '')
        user_agent: str = entry.get('userAgent', '')
        if (phone.startswith('+1') or phone.startswith('1')) and '4.0 Safari' in user_agent:
            yield {
                'name': entry.get('name', ''),
                'address': entry.get('address', ''),
                'email': entry.get('email', '')
            }


def write_to_csv_file() -> None:
    with open("out.csv", "w", newline='') as out_file:
        fieldnames: List[str] = ['name', 'address', 'email']
        writer: Dict[str] = csv.DictWriter(out_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in filtration_users(read_json_file()):
            writer.writerow(item)


filtration_users(read_json_file())
write_to_csv_file()
