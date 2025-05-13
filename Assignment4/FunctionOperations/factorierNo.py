def factorierNo(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    print("factorie no is:-", fact)


number = int(input("enter any Number"))
factorierNo(number)
