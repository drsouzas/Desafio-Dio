nome = input ("Digite o nome do seu herói: ") # inserindo nome do heroi
while True: # comando para que o valor inserido em experiencia seja um intenger, se for outro comando vai solicitar o dado de novo
    try:
           experienciaTotal = int(input ("Digite a experiência adquirida do seu herói até o momento: "))
           break
    except ValueError:
          print ("O valor inserido no campo experiência dever ser um valor númerico.") 

if experienciaTotal <= 1000:
    nivel = "Ferro"
elif experienciaTotal <= 2000:
        nivel = "Bronze"
elif experienciaTotal <= 5000:
        nivel = "Prata"
elif experienciaTotal  <= 7000:
        nivel = "Ouro"
elif experienciaTotal <= 8000:
        nivel = "Platina"
elif experienciaTotal  <= 9000:
        nivel = "Ascendente"
elif experienciaTotal  <= 10000:
        nivel = "Imortal"
elif experienciaTotal > 1000:
        nivel = "Radiante"

print (f'O Herói de nome {nome} está no nível de {nivel}.')