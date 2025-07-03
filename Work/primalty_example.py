from collections import Counter
import math

primalty = Counter()

def is_prime(number):
    
    # 1, 0 are neither prime nor composite, so do negatives
    
    if number > 1:
        start = 1
        end = math.sqrt(number)
        
        # Assume prime until we find counterexample
        is_prime = True
        
        for divisor in (2, end+1):
            if (number % divisor == 0):
                is_prime = False
        
        if (is_prime):
            return 'prime'
        else:
            return 'composite'
            
    else:
        return 'neither'




numbers = [int(math.tan(x)) for x in range(1,100)]

# Iterate through numbers
for index, num in enumerate(numbers):
    primalty[is_prime(num)] += 1

print(primalty)

        
        