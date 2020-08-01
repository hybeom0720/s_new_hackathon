import csv, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, "App", "DataBase", "MemberDataBase.csv")


with open(TEMP_DIR, newline='', encoding = "euc-kr") as csvfile:
    csv_data = list(csv.reader(csvfile))

print(csv_data)