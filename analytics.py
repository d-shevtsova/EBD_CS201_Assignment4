import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

# читаємо файли
sales = []

with open("global_sales.csv", "r") as sales_file:
    reader = csv.DictReader(sales_file)
    for row in reader:
        sales.append(row)
with open("regional_tariffs.json", "r") as file:
    tariffs = json.load(file)
# очистка від помилок

# обчислення нет-профіту

# новий датасет сlean_sales_upd

# cумарний профіт по категоріях

# сер профіт, фільтр, сортування у топ -> у json

# dataFrame

# стовпчаста діаграма