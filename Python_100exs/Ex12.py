np1 = float(input("Digite a nota da NP1: "))
np2 = float(input("Digite a nota da NP2: "))

media = (np1 + np2) / 2

if media == 10:
    print(f"Sua nota foi {media}, EXCELENTE!!!")
    
elif media >= 7:
    print(f"Sua nota foi {media}, APROVADO!")
    
elif media <= 6:
    print(f"Sua nota foi {media}, EXAME!!\n")
    
    NPexame = float(input("Nota do exame: "))
    exame = (np1 + np2 + NPexame) / 3
    
    if exame >= 5:
        print(f"Sua nota foi {exame}, passou")
    
    else:
        print(f"Sua nota foi{media}, PEGOU DP!!")
    
