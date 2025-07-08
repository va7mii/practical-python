# report.py
import csv
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        portdicts = parse_csv(f, select=['name','shares','price'], types=[str,int,float])
        portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
        return Portfolio(portfolio)


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as f:
        return dict(parse_csv(f, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change        = current_price - stock.price
        summary       = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_path, prices_path, fmt='txt'):
    # Read data files and create the report data        

    portfolio = read_portfolio(portfolio_path)
    prices    = read_prices(prices_path)

    # Generate the report data

    report = make_report_data(portfolio, prices)

    # Output the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    
def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
    


