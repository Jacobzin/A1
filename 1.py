import math


nome=input("Qual seu nome? ")
peso=float(input("Qual seu peso? "))
ingerida=float(input("Quantos litros de agua ingeriu hoje? "))

ideal=0.035*(peso)
ingerir=ideal-ingerida

idealc=math.ceil(ideal)
ingerirc=math.ceil(ingerir)
ingeridac=math.ceil(ingerida)

print(f"Nome do funcionario: {nome}.")
print(f"Peso do funcionario: {peso}.")
print(f"A quantidade de agua ingerida foi {ingeridac}.")
print(f"A quantidade ideal de agua a ingerir é {idealc}")
if ingerirc>=0:
    print(f"“Continue focado em se hidratar por hoje, ainda faltam {ingerirc} litros! Você consegue!”")
elif ingerirc<0:
    print(f"Parabéns, você atingiu a meta de hidratação diária")
