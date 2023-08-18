# ynab-bob

Converts Butterfield Bank exported CSV files into YNAB import format.
All CSV files in the script folder will be parsed, except those beginning with "YNAB_".
New files will be created for each in the format "YNAB_(Account Number)_(First Transaction Date)_(Last Transaction Date).CSV".
In the case of credit card files, (Account Number) will be "CC_XXXX", where XXXX are the last 4 digits of the credit card.
Regular and Credit Card export formats (current and historical) supported.
