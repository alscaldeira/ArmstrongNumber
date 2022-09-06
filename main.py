number = str(input("Digite algum valor: "))
result = 0

for n in number:
    result += pow(int(n), 3)

if result == int(number):
    print("O valor " + number + " e numero de armstrong. O valor da formula foi: " + str(result))
else:
    print('O valor ' + number + " nao e numero de armstrong. O valor da formula foi: " + str(result))