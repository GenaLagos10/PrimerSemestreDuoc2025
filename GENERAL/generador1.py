def genera_pares(limite):

    num=1

    while num<limite:
        yield num*2
        num=num+1

devuelvePares=genera_pares(10)

for i in devuelvePares:

    print(i)