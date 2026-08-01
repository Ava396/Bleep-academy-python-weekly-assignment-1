# Q2. Generate prime numbers between 1 and 100 using list comprehension.

primes = [num for num in range(2, 101)
          if all(num % i != 0 for i in range(2, num))]

print("Prime numbers from 1 to 100:")
print(primes)