numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue
    is_primed = True
    for i in range(2,num):
        if num % i == 0:
            is_primed = False
            break
    if is_primed:
        primes.append(num)
    else:
        not_primes.append(num)
print('primes: ',primes)
print('not_primes: ',not_primes)




