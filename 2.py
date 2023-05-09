placa = input("Digite a placa do veículo: ")
valor_litro = float(input("Digite o valor do litro do combustível: "))
km_60 = float(input("Digite a quantidade de quilômetros rodados a 60 KM/H: "))
km_80 = float(input("Digite a quantidade de quilômetros rodados a 80 KM/H: "))
km_100 = float(input("Digite a quantidade de quilômetros rodados a 100 KM/H: "))
km_120 = float(input("Digite a quantidade de quilômetros rodados a 120 KM/H: "))
km_140 = float(input("Digite a quantidade de quilômetros rodados a 140 KM/H: "))


comb_60 = km_60 / 30.7  
comb_80 = km_80 / 26.8
comb_100 = km_100 / 22.4
comb_120 = km_120 / 18.1
comb_140 = km_140 / 14.5


comb_total = comb_60 + comb_80 + comb_100 + comb_120 + comb_140


vel_media = (60*km_60 + 80*km_80 + 100*km_100 + 120*km_120 + 140*km_140) / (km_60 + km_80 + km_100 + km_120 + km_140)


custo_total = comb_total * valor_litro


print("Placa do veículo: ", placa)
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Velocidade média ponderada da viagem: {vel_media:.1f}km/h.")
print(f"Consumo total: {comb_total:.4f} litros.")
