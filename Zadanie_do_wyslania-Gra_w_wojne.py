colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
        {'Figure':'Ace',  'Power':14},
        {'Figure':'King', 'Power':13},
        {'Figure':'Queen','Power':12},
        {'Figure':'Jack', 'Power':11},
        {'Figure':'10',   'Power':10},
        {'Figure':'9',    'Power':9}]
     
allCards=[]
for c in colors:
    for f in figures:
        aCard=f.copy()
        aCard['Color']=c
        allCards.append(aCard)
     
import random
     
random.shuffle(allCards)
print(allCards)
     
player1=[]
player2=[]
     
player1=allCards[:12]
player2=allCards[12:]
     
     
print('Karty dla gracza 1')
print(player1)
     
print('Karty dla gracza 2')
print(player2)    
     
while len(player1) >0 and len(player2) >0:
    card1=player1.pop(0)
    card2=player2.pop(0)
    
    stack=[]
     
    if card1["Power"]==card2["Power"]:
        while card1["Power"]==card2["Power"]:
 
            print('Wojna', card1['Power'], card2['Power'])
            stack.append(card1)
            stack.append(card2)
 
            if len(player1)<2:
                player2.extend(stack)    
                player2.extend(player1)
                player1=[]
                print('Wojne wygrywa gracz 2 z powodu braku kart u gracza 1 \t %d \t %d' % (card1["Power"], card2["Power"]))
                break
            elif len(player2)<2:
                player1.extend(stack)    
                player1.extend(player2)
                player2=[]
                print('Wojne wygrywa gracz 1 z powodu braku kart u gracza 2 \t %d \t %d' % (card1["Power"], card2["Power"]))
                break
            else:
                card1=player1.pop(0)
                card2=player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1=player1.pop(0)
                card2=player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('Wojne wygrywa gracz 1 \t %d \t %d' % (card1["Power"], card2["Power"]))
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('Wojne wygrywa gracz 2 \t %d \t %d' % (card1["Power"], card2["Power"]))
    
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('Zgarnia gracz 1 \t %d \t %d' % (card1["Power"], card2["Power"]))
    
    elif card1["Power"] < card2["Power"]:
        player2.append(card1)
        player2.append(card2)
        print('Zgarnia gracz 2 \t %d \t %d' % (card1["Power"], card2["Power"]))
     
if len(player1) > 0:
    print('Gracz 1 zwycieza')
else:
    print('Gracz 2 zwycieza')