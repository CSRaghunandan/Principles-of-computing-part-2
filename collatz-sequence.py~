
def collatz(num, count):
    """
    Given n, repeatedly perform n = f(n) where
    f(n) = n / 2 if n is even
    f(n) = 3 * n + 1 is n is odd
    Return number of iterations of this redution
    """
    if num == 1:
        return count
    elif (num % 2) == 0:
        return collatz(num / 2, count + 1)
    else:
        return collatz(3 * num + 1, count + 1)
    
print collatz(5, 0)
