#input é uma função que permite perguntar algo ao usuário
#nome = input("Qual é seu nome?")
#print("Olá,", nome, ". Tudo bem com você?")
#print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
print("Tipo da var a:", type(a)) #tipo inteiro (numeros inteiros)
print("Tipo da var b:", type(b)) #tipo float (numeros reais)
print("Tipo da var c:", type(c)) #tipo string (alfanumérico)
print("Tipo da var d:", type(d)) #tipo boolean (true ou false)


a = 20
print("a:",a)
b = "São Paulo"
print("b:",b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))


a = input("Informe um número:")
b = input("Informe outro número:")
print("a:",a, "b:", b)
print("Tipo da var a:", type(a))
print("Tipo da var b:", type(b))
c = a + b #concatenou as strings de a e b
print("c:", c)
print("Tipo da var c:", type(c))
d = int(a)
print("d:",d)
print("Tipo da var d:", type(d))


a = int(input("Informe um número:"))
b = int(input("Informe outro número:"))
print("a:",a, "b:", b)
print("Tipo da var a:", type(a))
print("Tipo da var b:", type(b))
c = a + b #soma os inteiros
print("c:", c)
print("Tipo da var c:", type(c))


a = float(input("Informe um número:"))
b = float(input("Informe outro número:"))
print("a:",a, "b:", b)
print("Tipo da var a:", type(a))
print("Tipo da var b:", type(b))
c = a + b #somou os reais com "."
print("c:", c)
print("Tipo da var c:", type(c))