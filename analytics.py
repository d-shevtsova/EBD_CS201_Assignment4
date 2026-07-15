import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

from matplotlib import colors

# читаємо файли
sales = []

with open("global_sales.csv", "r") as sales_file:
    reader = csv.DictReader(sales_file)
    for row in reader:
        sales.append(row)
with open("regional_tariffs.json", "r") as file:
    tariffs = json.load(file)
# очистка від помилок
for sale in sales:
    if sale["quantity"] == "N/A":
        sale["quantity"] = 0
    else:
        sale["quantity"] = int(sale["quantity"])

    if sale["revenue"] == "N/A":
        sale["revenue"] = 0.0
    else:
        sale["revenue"] = float(sale["revenue"])
for region in tariffs.keys():
    if tariffs[region] == "N/A":
        tariffs[region] = 0
# обчислення нет-профіту
for sale in sales:
    tariff = tariffs.get(sale["region"])
    sale["net_profit"] = round(sale["revenue"]-sale["revenue"] * tariff/100,2)
# новий датасет сlean_sales_upd
filename = list(sales[0].keys())
with open("cleaned_sales_updated.csv", "w", newline="") as cleaned:
    smth = csv.DictWriter(cleaned, filename)
    smth.writeheader()
    smth.writerows(sales)
# cумарний профіт по категоріях
category = {}

for sale in sales:
    cat=sale["product_category"]
    if cat not in category:
        category[cat] = 0
    category[cat] +=sale["net_profit"]
# сер профіт, фільтр, сортування у топ -> у json
avr = (sum(category.values())/len(category))
top = dict(filter(lambda x: x[1]>avr, category.items()))
top = dict(sorted(top.items(), key=lambda x: x[1], reverse=True))
with open("top_categoty.json", "w") as top_categoty:
    json.dump(top, top_categoty, indent=4)
# dataFrame
df = pd.DataFrame(list(category.items()), columns=["category", "net_profit"])
print(df)
# стовпчаста діаграма
colors = ["red","orange","yellow","green","blue","purple","pink","brown"]
plt.figure(figsize = (10,6))
plt.bar(df["category"], df["net_profit"],color = colors)
plt.title("Top Categories")
plt.xlabel("Category")
plt.ylabel("Net Profit")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()