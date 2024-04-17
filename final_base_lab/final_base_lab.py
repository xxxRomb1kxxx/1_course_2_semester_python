import csv
import os
import random

class CSVProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_csv()

    def load_csv(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data

    def show(self, output_type='top', num_rows=5, separator=','):
        if output_type == 'bottom':
            data_to_show = self.data[-num_rows:]
        elif output_type == 'random':
            data_to_show = random.sample(self.data, num_rows)
        else:
            data_to_show = self.data[:num_rows]

        for row in data_to_show:
            print(separator.join(row.values()))

    def info(self):
        header = self.data[0]
        num_rows = len(self.data) - 1
        num_cols = len(header)
        print(f"Number of rows x columns: {num_rows}x{num_cols}")

        print("Field Name\tQty\tType")
        for field in header:
            non_empty_count = sum(1 for row in self.data[1:] if row[field])
            field_type = type(self.data[1][field]).__name__
            print(f"{field}\t{non_empty_count}\t{field_type}")

    def del_nan(self):
        self.data = [row for row in self.data if all(row.values())]

    def make_ds(self):
        learning_data = random.sample(self.data, int(0.7 * len(self.data)))
        testing_data = [row for row in self.data if row not in learning_data]

        os.makedirs("workdata/Learning", exist_ok=True)
        os.makedirs("workdata/Testing", exist_ok=True)

        with open("workdata/Learning/train.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(learning_data)

        with open("workdata/Testing/test.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(testing_data)

if __name__ == "__main__":
    processor = CSVProcessor("Titanic.csv")
    processor.show(output_type='top', num_rows=5)
    print("/////////////////////////")
    processor.info()
    processor.del_nan()
    processor.make_ds()
