# Unique Product Category Extractor

A Python mini project that processes a retail transaction CSV file to extract all unique product categories and count distinct customers for each category. This project demonstrates practical data cleaning, CSV handling, and use of Python data structures.

## Features

- Reads and processes a retail transaction CSV file  
- Extracts unique product categories using a set  
- Counts distinct customers per category  
- Handles missing or empty fields safely  
- Outputs categories in sorted order  
- Uses only standard Python libraries

## Project Structure

```
project/
    extract_unique_categories.py
    sample_data.csv (optional)
    README.md
```

## Requirements

- Python 3.7 or higher  
- No external packages required

## CSV Format

The script expects a CSV file with the following columns:

- transaction_id  
- customer_id  
- product_category  
- amount  

If your column names differ, you may adjust the code accordingly.

## How to Use

1. Place your CSV file in the project directory.  
2. Update the `filename` variable inside `extract_unique_categories.py` if needed.  
3. Run the script:

```
python extract_unique_categories.py
```

4. The script will print:
   - Total number of unique product categories  
   - A sorted list of all categories  
   - The number of distinct customers per category  

## Example Output

```
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
```

## Purpose

This project is designed to demonstrate core data processing techniques in Python, including CSV parsing, data validation, and the use of sets and dictionaries. It is suitable for learners and anyone exploring basic data engineering tasks.
