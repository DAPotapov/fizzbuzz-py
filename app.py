for cur in range(1, 101):
    result = ""
    if cur % 3 == 0:
        result = result + 'fizz'
    if cur % 5 == 0:
        result = result + 'buzz'
    if cur % 3 and cur % 5:
        result = cur
    print(result)

