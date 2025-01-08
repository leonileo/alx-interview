#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x <= 0:
        return None
    
    max_n = max(nums)
    
    # Step 1: Precompute prime numbers using the Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    
    # Step 2: Count primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    # Step 3: Simulate the game for each round
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 1:  # Odd count -> Maria wins
            maria_wins += 1
        else:  # Even count -> Ben wins
            ben_wins += 1
    
    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
