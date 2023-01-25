import random

box = []

card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_suit = ["♠", "♥", "♣", "◆"]

for i in card_number:
    for j in card_suit:
        box.append((i,j))

random.shuffle(box)
p1 = []
p2 = []

for i in range(6):
    if i%2 == 0:
        p1.append(box[i])

    else :
        p2.append(box[i])

# print(p1)
# print(p2)


p1sum = 0 
p2sum = 0 

for i in p1:
    if i[1] == "♣":
        p1sum += (4*i[0])
    elif i[1] == "♠":
        p1sum += (3*i[0])
    elif i[1] == "◆":
        p1sum += (2*i[0])
    else:
        p1sum += (i[0])

print(p1sum)

for i in p2:
    if i[1] == "♣":
        p2sum += (4*i[0])
    elif i[1] == "♠":
        p2sum += (3*i[0])
    elif i[1] == "◆":
        p2sum += (2*i[0])
    else:
        p2sum += (i[0])

print(p2sum)

if p1sum > p2sum :
    print(f'p1승리 : {p1sum} : {p2sum}')
elif p1sum < p2sum :
    print(f'p2승리 : {p2sum} : {p1sum}')
else:
    print("무승부")