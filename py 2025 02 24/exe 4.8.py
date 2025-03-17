text = input("digite o texo: ")
desmembre = text.split()
if desmembre.index() >= 5:
    for palavra in desmembre:
        print(palavra)
else:
    print("erro!")