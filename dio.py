nome = input('Informe seu nome:')
nivel_xp = int(input("Qual o nivel do seu XP?:"))
dados_heroi = (nome,nivel_xp)

print("o heroi de nome", nome, "esta no nivel", nivel_xp)

if nivel_xp <=1000:
    print("XP de Ferro")
elif nivel_xp >1001:
    print("XP de Bronze")
elif nivel_xp <=2000:
    print("XP de Bronze")
elif nivel_xp >=2001:
    print("XP Prata Ouro")
elif nivel_xp <=5000:
    print("XP Prata Ouro")
elif nivel_xp >=5001:
    print("XP Platina Diamante")
elif nivel_xp <=8000:
    print("XP Platina Diamante")
elif nivel_xp >=8001:
    print("XP Ascendente")
elif nivel_xp <=9000:
    print('XP Ascendente')
else:
    print('_')

    
