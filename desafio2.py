def winsSaldo (wins, defeats):
    saldoVitorias = wins - defeats
    return saldoVitorias

def elo (saldoVitorias):
    if saldoVitorias < 11:
        nivel = "Ferro"
    elif saldoVitorias < 21:
        nivel = "Bronze"
    elif saldoVitorias < 51:
        nivel = "Prata"
    elif saldoVitorias < 81:
        nivel = "Ouro"
    elif saldoVitorias < 91:
        nivel = "Diamante"
    elif saldoVitorias < 101:
        nivel = "Lendário"
    elif saldoVitorias > 100:
        nivel = "Imortal"
    return nivel



while True: # comando para que o valor inserido em experiencia seja um intenger, se for outro comando vai solicitar o dado de novo
    try:
           wins = int (input("Entre com o total de vitorias: "))
           break
    except ValueError:
          print ("O valor inserido no campo experiência dever ser um valor númerico.") 

while True: # comando para que o valor inserido em experiencia seja um intenger, se for outro comando vai solicitar o dado de novo
    try:
           defeats = int (input ("Entre com o total de derrotas: "))
           break
    except ValueError:
          print ("O valor inserido no campo experiência dever ser um valor númerico.") 


saldoVitorias = winsSaldo (wins, defeats)
nivel = elo (saldoVitorias)


print (f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")