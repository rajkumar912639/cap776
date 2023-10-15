# A function to check if a number is prime or not
def is_prime(n):
  # Edge cases
  if n <= 1:
    return False
  if n == 2:
    return True
  # Check for divisibility by 2
  if n % 2 == 0:
    return False
  # Check for divisibility by odd numbers from 3 to sqrt(n)
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  # If no divisor found, the number is prime
  return True

# A loop to print all prime numbers up to 100
for i in range(1, 101):
  if is_prime(i):
    print(i)
