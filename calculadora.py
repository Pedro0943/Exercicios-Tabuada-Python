
n1 = int(input("Digite valor x: "))
n2 = int(input(("Digite valor y: ")))

produto = n1 * n2

quociente = n1 / n2

operacao = input("Digite * ou  / ")

if operacao == "*":
    print(n1,"*",n2,"=",produto)
elif operacao == "/":
    print(n1,"/",n2,"=",quociente)