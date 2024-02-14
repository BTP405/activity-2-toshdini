def is_prime(num):
    """
    This function takes a pramater and returns boolean answer
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
def getPrimeNumbers(n):
    return [num for num in range(2, n+1) if is_prime(num)]

def main():
    print(getPrimeNumbers(250))
    
if __name__ == "__main__":
    main()