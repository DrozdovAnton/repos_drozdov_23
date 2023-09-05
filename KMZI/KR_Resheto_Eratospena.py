def resheto_eratosphena(N):

    primes = [i for i in range(N + 1)]
    primes[0] = primes[1] = 0

    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1

    return [i for i in primes if i != 0]

