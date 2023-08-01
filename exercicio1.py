'''
Elabore um progroma que pergunte ao aluno suas 3 notas escolares.
O programa deverá calcular a média das 3 notas inseridas e exibir esta média.
'''

nota1 = float(input("Qual foi sua nota do primeiro bimestre?"))
nota2 = float(input("E do segundo bimestre?"))
nota3 = float(input("E a do terceiro bimestre?"))

somadasnotas = nota1 + nota2 + nota3
mediadasnotas = somadasnotas / 3
print("Parabéns mestre, a sua média é:", mediadasnotas)