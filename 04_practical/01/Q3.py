def countDown(n):
    if n <= 0:
        return
    print(n)
    countDown(n - 1)

countDown(5)