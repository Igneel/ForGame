def perfectSquare(x):
    return (int(x**0.5))**2 == x
    
def factorizeFerma(n):
    x = int(n ** 0.5) + 1
    while x*x <= n: 
        x+=1
    while not perfectSquare(x * x - n):
        x += 1
    y = int((x * x - n) ** 0.5)
    a = x - y
    b = x + y
    return a, b

n=0x52a99e249ee7cf3c0cbf963a009661772bc9cdf6e1e3fbfc6e44a07a5e0f894457a9f81c3ae132ac5683d35b28ba5c324243

a, b = factorizeFerma(n)
print(a, b)