portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

records = []  # Initial empty list

# Use .append() to add more items
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))

d = {
    'a' : 10,
    'b' : 9,
    'c' : 8,
}

# Test existance of key

key = 'd'

if key in d:
    print('yes')
else:
    print('no')

# Composite keys

holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}

print(holidays[1,1])

# Sets
tech_stocks = {"ibm", "aapl"}

names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

# Convert to Set
unique = set (names)


unique.add('CAT')
unique.remove('YHOO')
print(unique)

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
print(s1 | s2)              # Set union { 'a', 'b', 'c', 'd' }
print(s1 & s2)                   # Set intersection { 'c' }
print(s1 - s2)              # Set difference { 'a', 'b' }

