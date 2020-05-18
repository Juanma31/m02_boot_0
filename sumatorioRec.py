
def sumatorio(n):
    if n!=0:
        return n+sumatorio(n-1)
    else:
        return 0

print(sumatorio(4))

def factorial(n):
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1
    
print(factorial(5))