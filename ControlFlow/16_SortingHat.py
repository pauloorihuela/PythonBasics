# Write code below 💖

hufflepuff=0
slytherin=0 
ravenclaw=0 
gryffindor=0

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
q1=int(input())

if q1==1:
    gryffindor=gryffindor+1
    ravenclaw=ravenclaw+1
elif q1==2:
    hufflepuff=hufflepuff+1
    slytherin=slytherin+1
else:
    print("Wrong input. ")


print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
q2=int(input())

if q2==1:
    hufflepuff=hufflepuff+2
elif q2==2:
    slytherin=slytherin+2
elif q2==3:
    ravenclaw=ravenclaw+2
elif q2==4:
    gryffindor=gryffindor+2
else:
    print("Wrong input. ")


print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
q3=int(input())

if q3==1:
    slytherin=slytherin+4
elif q3==2:
    hufflepuff=hufflepuff+4
elif q3==3:
    ravenclaw=ravenclaw+4
elif q3==4:
    gryffindor=gryffindor+4
else:
    print("Wrong input. ")


print("The score for the house  is gryffindor", gryffindor)
print("The score for the house  is hufflepuff", hufflepuff)
print("The score for the house  is ravenclaw", ravenclaw)
print("The score for the house  is slytherin", slytherin)

# Bonus

if (gryffindor>hufflepuff) and (gryffindor>ravenclaw) and (gryffindor>slytherin):
    print("The house with more points is Gryffindor")
elif (hufflepuff>gryffindor) and (hufflepuff>ravenclaw) and (hufflepuff>slytherin):
    print("The house with more points is Hufflepuff")
elif (ravenclaw>gryffindor) and (ravenclaw>hufflepuff) and (ravenclaw>slytherin):
    print("The house with more points is Ravenclaw")
else:
    print("The house with more points is Slytherin")


