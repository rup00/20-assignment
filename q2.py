
def check_prime(num):
  for n in range(2,num):
    if num % n == 0:
      print(num,"is not prime")
      break
  else:
      print(num,"is prime")

check_prime(9)