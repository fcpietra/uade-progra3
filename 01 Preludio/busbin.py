def busbin(T, ini, fin, x):
    print("vector", T, "inicio", ini, "fin", fin, "elemento", x)
    if(ini == fin):
        if(T[ini]==x):
            return ini
        else:
            return -1
    else:
        mid = (ini+fin)//2
        if(x < T [mid]):
            return busbin(T, ini, mid-1, x)
        else:
            return busbin(T, mid+1, fin, x)

##TEST
print(busbin([26,28,36,64,67,102], 0, 3, 64))

    