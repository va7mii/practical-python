# fileparse.py
#
# Exercise 3.3


import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV file into a list of records
    '''
    
    # Checking for valid conditions
    if (select and has_headers==False):
            raise RuntimeError("select argument requires column headers")
    
   
    rows = csv.reader(file, delimiter=delimiter)
    
    

    
    if has_headers:
        # Read the file headers
        headers = next(rows)
    
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
        
    

    
    records = []
    for rowno, row in enumerate(rows,start=1):
        if not row:    # Skip rows with no data
            continue
        
        try:
            # Fitler the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
                
            # Filter types
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            
            
            # Headers checking
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f"Row {rowno}: couldn't convert {row}")
                print(f"Row {rowno}: Reason {e}")
                
            

    return records


