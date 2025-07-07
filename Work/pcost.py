#!/usr/bin/env python3

# pcost.py

import report
import csv

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''

    portfolio = report.read_portfolio(filename)
    return sum(s.shares * s.price for s in portfolio)


def main(args):
    if len(args) == 2:
        filename = args[1]
        print(portfolio_cost(filename))
    else:
        filename = input('Enter a filename:')
    
if __name__ == '__main__':
    import sys
    main(sys.argv)


