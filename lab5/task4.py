# import json
# import csv
# import os
# import sys

# def json_to_csv(json_file):
#     json_path = os.path.abspath(json_file)
#     json_name = os.path.splitext(os.path.basename(json_path))[0]
#     with open(json_file, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     csv_name = f"{json_name}.csv"
#     csv_path = os.path.join(os.path.dirname(json_path), csv_name)
#     with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         if isinstance(data, list):
#             if len(data) > 0:
#                 writer.writerow(data[0].keys())
#                 for item in data:
#                     writer.writerow(item.values())
#         elif isinstance(data, dict):
#             writer.writerow(data.keys())
#             writer.writerow(data.values())

#     print(f"CSV файл успешно создан: {csv_path}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Использование: python json2csv.py example.json")
#         sys.exit(1)

#     json_file = sys.argv[1]
#     json_to_csv(json_file)
import json
import csv
import os
import sys

def json_to_csv(json_file):
    csv_filename = os.path.splitext(json_file)[0] + '.csv'
    with open(json_file, 'r') as f:
        data = json.load(f)
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if isinstance(data, list):
                headers = list(data[0].keys())
                writer.writerow(headers)
                for item in data:
                    writer.writerow(item.values())
            else:
                headers = list(data.keys())
                writer.writerow(headers)
                writer.writerow(data.values())

    print(f"CSV файл успешно создан: {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
        sys.exit(1)

    json_file = sys.argv[1]

    if not os.path.exists(json_file):
        print(f"Файл {json_file} не найден.")
        sys.exit(1)

    json_to_csv(json_file)