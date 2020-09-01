# CSVScale
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin to multiply all values in a CSV file by a constant.

The plugin accepts as input a TXT file of keyword-value pairs:
csvfile: Input CSV file
constant: The scaling factor

The output CSV file will then be the input CSV file scaled by the constant.
