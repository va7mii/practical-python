names = ['Elwood', 'Jake', 'Curtis']

for i, name in enumerate(names):
    print(f"No. {i}, {name:>5s}")
    
# with open(filename) as f:
#     for lineno, line in enumerate(f,start=1)

# Points example
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]

for num, (x,y) in enumerate(points):
    print(f'No. {num:10d} {x:<5d} {y:<3d}')
    
# Zip example (useful for dictionaries)
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)

d = dict(zip(columns, values))