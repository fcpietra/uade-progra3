def busbin(T, ini, fin, x):
    if(ini == fin):
        if(T[ini]==x):
            return ini
        else:
            return -1
    else:
        mid = (ini+fin)//2
        if(x < T [mid]):
            return busbin(T, ini, mid - 1, x)
        else:
            return busbin(T, mid, fin, x)

print(busbin([26,28,36,64], 0, 3, 64))
    