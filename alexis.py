def nuke(n: int):
    """
    Recursive function that calls itself n times.
    print 10**n lists of n elements.
    """
    a = []
    for i in range(10):
        if n > 1:
            a.append(nuke(n - 1))
        else:
            a.append(i)
    return a


print(nuke(10))
