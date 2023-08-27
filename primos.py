def primo (n):
    return(n*n+n+41)

def esPrimo(primo):
    for n in range(2,primo//2):
        if primo % n  == 0:
            print("NO es primo")

for div in range (1,100):
    print ("n es ", div)
    num=primo(div)
    print(num)
    esPrimo(num)