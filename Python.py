menu="""
Bienvenidos al convertor de monedas 💰😎

1. PESOS COLOMBIANOS 💛💙❤
2. PESOS ARGENTINOS 💙🤍💙
3. PESOS MEXICANOS 💚🤍❤
4. NUEVOS SOLES ❤🤍❤
Elige una opción 
"""
opción= int(input(menu))
if opción==1:
	valor=str(input('Ingresa un valor en dólares:'))
	valor_dólar=(3681.20)
	valor_dólar=float(valor_dólar)
	valor_pesos=int(valor)*valor_dólar
	valor_pesos=round(valor_pesos, 2)
	valor_pesos=str(valor_pesos)
	print('El valor en pesos colombianos es: $',valor_pesos,'🇨🇴')
if opción==2:
	valor=str(input('Ingresa un valor en dólares:'))
	valor_dólar=(71.84)
	valor_dólar=float(valor_dólar)
	valor_pesosarg=int(valor)*valor_dólar
	valor_pesosarg=round(valor_pesosarg, 2)
	valor_pesosarg=str(valor_pesosarg)
	print('El valor en pesos argentinos es: $',valor_pesosarg,'🇦🇷')	
if opción==3:
	valor=str(input('Ingresa un valor en dólares:'))
	valor_dólar=(22.28)
	valor_dólar=float(valor_dólar)
	valor_pesosmex=int(valor)*valor_dólar
	valor_pesosmex=round(valor_pesosmex, 2)
	valor_pesosmex=str(valor_pesosmex)
	print('El valor en pesos mexicanos es: $',valor_pesosmex,'🇲🇽')
if opción==4:
	valor=str(input('Ingresa un valor en dólares:'))
	valor_dólar=(3.62)
	valor_dólar=float(valor_dólar)
	valor_soles=int(valor)*valor_dólar
	valor_soles=round(valor_soles, 2)
	valor_soles=str(valor_soles)
	print('El valor en nuevos soles es: S/',valor_soles,'🇵🇪')