# mortgage.py
#
# Exercise 1.


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_months_left = 12

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    if extra_months_left > 0:
        total_paid -= 1000
        extra_months_left -= 1

print('Total paid', total_paid)
