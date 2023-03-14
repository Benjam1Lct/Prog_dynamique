
def fibonacciDyn(n):
    if n == 1 or n == 2:
        return 1
    stockage = [None] * (n + 1)
    stockage[1], stockage[2] = 1,1
    for i in range(3, n + 1):
        stockage[i] = stockage[i - 1] + stockage[i - 2]
    return stockage[n]

print(fibonacciDyn(7))