import os
import csv
from datetime import datetime

def process_csv(in_filename):

    is_cc = False   # is credit card CSV
    ynab_csv = []
    ynab_csv.append(["Date", "Payee", "Memo", "Outflow", "Inflow"])

    try:
        with open(in_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                match line_count:
                    case 0:
                        if row[0] == "Card No":
                            is_cc = True
                        
                        if is_cc:
                            out_filename = "YNAB_CC_" + row[1][-4:] + ".csv"
                        else:
                            out_filename = "YNAB_" + row[0] + ".csv"
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        if is_cc:
                            pass
                        else:
                            trans_date = datetime.strptime(row[0], '%d %b %Y')
                            trans_date_string = trans_date.strftime('%m/%d/%Y')
                            ynab_csv.append([trans_date_string, row[2].strip(), row[2].strip(), row[3], row[4]])                                    
                    case _:
                        if is_cc:
                            trans_date = datetime.strptime(row[1], '%d %b %Y')
                            trans_date_string = trans_date.strftime('%m/%d/%Y')
                            
                            outflow = ''
                            inflow = ''

                            if row[3].strip() == "Dr":
                                outflow = row[4]
                            else:
                                inflow = row[4]
                            
                            ynab_csv.append([trans_date_string, row[2].strip(), row[2].strip(), outflow, inflow])

                        else:                        
                            trans_date = datetime.strptime(row[0], '%d %b %Y')
                            trans_date_string = trans_date.strftime('%m/%d/%Y')
                            ynab_csv.append([trans_date_string, row[2].strip(), row[2].strip(), row[3], row[4]])
                
                line_count += 1

    except:
        print(f'Error reading file {in_filename}')

    try:
        with open(out_filename, mode='w', newline='', encoding='utf-8') as ynab_csv_file:
            ynab_writer = csv.writer(ynab_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in ynab_csv:
                ynab_writer.writerow([line[0], line[1], line[2], line[3], line[4]])
        print(f'Input: {in_filename} Output: {out_filename}')
    except:
        print(f'Error writing file {out_filename}')

file_count = 0

for file in os.listdir():
    if file.endswith('.csv') and not file.startswith('YNAB_'):
        process_csv(file)
        file_count =+ 1

print(f'{file_count} files processed.')