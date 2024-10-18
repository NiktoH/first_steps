import json
import csv


with open("in.json", "r") as in_file:
    data = json.load(in_file)


def check_gen(data):
    for entry in data:
        phone = entry.get('phoneNumber', '')
        user_agent = entry.get('userAgent', '')
        if (phone.startswith('+1') or phone.startswith('1')) and '4.0 Safari' in user_agent:
            yield {
                'name': entry.get('name', ''),
                'address': entry.get('address', ''),
                'email': entry.get('email', '')
            }


with open("out.csv", "w", newline='') as out_file:
    fieldnames = ['name', 'address', 'email']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in check_gen(data):
        writer.writerow(item)
