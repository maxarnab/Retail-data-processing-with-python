import csv
from collections import defaultdict

filename = 'sample_101_new_retail_data.csv'   # change path if needed

unique_categories = set()               # will store all unique product categories
category_customers = defaultdict(set)   # maps category -> set of distinct customer_ids

with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Use the expected CSV column names; guard against missing keys
        category = (row.get('Product_Category') or '').strip()
        customer = (row.get('Customer_ID') or '').strip()

        if not category:
            continue  # skip rows without a category

        unique_categories.add(category)  # add category to set (keeps only unique values)

        if customer:                     # only add non-empty customer ids
            category_customers[category].add(customer)

# Printing number of unique categories and the sorted list
print("Unique product categories count:", len(unique_categories))
print("Unique product categories (sorted):")
for c in sorted(unique_categories):
    print("-", c)

# printing number of distinct customers per category
print("\nDistinct customer counts per category:")
for c in sorted(unique_categories):
    print(f"- {c}: {len(category_customers[c])} distinct customer(s)")

#THANK YOU