salario = float(input("Salario: "))

if salario <= 280:
    reajuste = salario * 20 / 100
    novo_salario = salario + reajuste
    print(f" Salario antigo: {salario} \n Aumento: 20% \n Valor de aumento: {reajuste} \n Salario atual: {novo_salario}")
    
elif salario >= 280 and salario <= 700: 
    reajuste = salario * 15 / 100
    novo_salario = salario + reajuste
    print(f" Salario antigo: {salario} \n Aumento: 15% \n Valor de aumento: {reajuste} \n Salario atual: {novo_salario}")

elif salario >= 700 and salario <= 1500: 
    reajuste = salario * 10 / 100
    novo_salario = salario + reajuste
    print(f" Salario antigo: {salario} \n Aumento: 10% \n Valor de aumento: {reajuste} \n Salario atual: {novo_salario}")

elif salario > 1500: 
    reajuste = salario * 5 / 100
    novo_salario = salario + reajuste
    print(f" Salario antigo: {salario} \n Aumento: 5% \n Valor de aumento: {reajuste} \n Salario atual: {novo_salario}")


    