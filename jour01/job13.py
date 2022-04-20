loops = int(input("combien de nombre entier:"))

lis = []

for x in range(loops):
    lis.append(int(input("chiffre "+str(x+1)+": ")))

lis.sort()
print(lis)
