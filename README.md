# bob-ynab

Converts Butterfield Bank exported CSV files into YNAB import format.
All CSV files in the script folder will be parsed, except those beginning with "YNAB_".
New files will be created for each, and named based on account number within the CSV.
Regular and Credit Card export formats supported.