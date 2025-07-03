import os


try:
    fp = open('Data/portfolio.csv', 'rt')
    print(fp.read())
    Rai
except ValueError as exc:
    print("caught exception", exc)

finally:
    print("okay")
    fp.close()


