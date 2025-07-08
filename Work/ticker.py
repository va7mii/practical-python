# ticker.py

import csv
import report
import tableformat
from follow import follow
import time


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(datapath, logpath, fmt):
    portfolio = report.read_portfolio(datapath)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )
    
    

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt') # Testing
