def factorial(n): 
    if n>=1:
        fact=n*factorial(n-1)
        return fact
    else:
        fact=1
        return fact
if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)
