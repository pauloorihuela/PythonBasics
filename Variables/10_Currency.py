# Write code below 💖

pesos=float(input("What do you have left in pesos? "))
soles=float(input("What do you have left in soles? "))
reais=float(input("What do you have left in reais? "))

usd=float()

usd=(pesos*0.00024)+(soles*0.27)+(reais*0.0040)

print("En total tiene ", usd, ("$"))
