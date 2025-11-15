# Conversor de Temperatura Celsius, Fahrenheit, Kelvin

""""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter

"""
temperatura = float(input("Entre a temperatura a ser convertida -> "))


unidade = str(input("Entre a unidade (c para celsius, f para fahrenheit, k para kelvin) -> ")).lower()

converte = str(input(f"Entre a unidade para qual deseja converter (c, f, k) -> ")).lower()

resultado = 0.0

if unidade == converte:
    print(f"Não é necessária conversão. A temperatura já está em {unidade}.")
    resultado = temperatura


elif converte == 'c':
    if unidade == 'f':
        
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {resultado:.2f}°C")
    elif unidade == 'k':
        
        resultado = temperatura - 273.15
        print(f"{temperatura}K é igual a {resultado:.2f}°C")
    else:
        print(f"Unidade de origem '{unidade}' inválida.")


elif converte == 'f':
    if unidade == 'c':
        
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {resultado:.2f}°F")
    elif unidade == 'k':
        
        resultado = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K é igual a {resultado:.2f}°F")
    else:
        print(f"Unidade de origem '{unidade}' inválida.")


elif converte == 'k':
    if unidade == 'c':
        
        resultado = temperatura + 273.15
        print(f"{temperatura}°C é igual a {resultado:.2f}K")
    elif unidade == 'f':
        
        resultado = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F é igual a {resultado:.2f}K")
    else:
        print(f"Unidade de origem '{unidade}' inválida.")


else:
    print(f"Unidade de destino '{converte}' inválida.")



