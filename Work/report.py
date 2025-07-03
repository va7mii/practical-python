# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

portfolio = []



def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
            
            # Testing with f-strings
            print(f'{row[0]:>10s} {nshares:^10d} {price:>10.2f}')
            print('%5d %-5d %10d' % (1,2,3))
            
            holding = (row[0],int(row[1]), float(row[2]))
            portfolio.append(holding)
    return total_cost

total_cost = portfolio_cost('Data/portfolio.csv')

pprint(portfolio)
