Unique Product Category Extractor

This project provides a Python script for processing a retail transaction CSV file. It reads the dataset, extracts all unique product categories using a set, and counts the number of distinct customers associated with each category. The script demonstrates practical use of CSV handling, basic data cleaning, and Python data structures.

Features

Reads a CSV file containing retail transaction data

Extracts all unique product categories

Counts distinct customers per category

Handles missing or empty fields gracefully

Outputs categories in sorted order

File Structure
project/
    extract_unique_categories.py
    sample_data.csv (optional)
    README.md

Requirements

Python 3.7 or higher

No external libraries are required. The script uses only standard Python modules.

Usage

Place your CSV file in the project directory.

Update the filename variable in extract_unique_categories.py if necessary.

Run the script:

python extract_unique_categories.py


The script will print:

The number of unique product categories

A sorted list of categories

The number of distinct customers per category

CSV Format

The script expects a CSV file containing at least the following columns:

transaction_id

customer_id

product_category

amount

Column names should match exactly unless modified in the code.

Example Output
Unique product categories count: 12
Unique product categories (sorted):
- Books
- Clothing
- Electronics
...

Distinct customer counts per category:
- Books: 47
- Clothing: 93
- Electronics: 132
...

Purpose

This project serves as a basic example of data processing using Python. It is suitable for learning, teaching, or demonstration of fundamental data handling techniques.
