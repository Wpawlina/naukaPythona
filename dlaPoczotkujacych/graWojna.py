def War():
    import random
    from queue import Queue
    allCards=[]
    colors = ['Hearts','Diamonds','Clubs','Spades']
    figures = [
        {'Figure':'Ace',  'Power':14},
        {'Figure':'King', 'Power':13},
        {'Figure':'Queen','Power':12},
        {'Figure':'Jack', 'Power':11},
        {'Figure':'10',   'Power':10},
        {'Figure':'9',    'Power':9}]
    for color in colors:
        for fig in figures:
            aCard={}
            aCard=fig.copy()
            aCard['Color']=color
            allCards.append(aCard)
    random.shuffle(allCards)
    player1=Queue()
    player2=Queue()
    while len(allCards)>0:
        player1.put(allCards.pop())
        player2.put(allCards.pop())
    while  not player1.empty() and  not player2.empty():
        cardP1=player1.get()
        cardP2=player2.get()
        if cardP1['Power']>cardP2['Power']:
            player1.put(cardP1)
            player1.put(cardP2)
        elif cardP1['Power']<cardP2['Power']:
            player2.put(cardP1)
            player2.put(cardP2)
        else:
            cardsOnTable = [cardP1, cardP2]
            while not player1.empty() and not player2.empty():
                # Each player puts one card face down
                if not player1.empty():
                    cardsOnTable.append(player1.get())
                if not player2.empty():
                    cardsOnTable.append(player2.get())
                
                # Each player reveals a card
                if player1.empty() or player2.empty():
                    break
                cardP1 = player1.get()
                cardP2 = player2.get()
                cardsOnTable.append(cardP1)
                cardsOnTable.append(cardP2)
                
                if cardP1['Power'] != cardP2['Power']:
                    break

            if player2.empty() or cardP1['Power'] > cardP2['Power']:
                for card in cardsOnTable:
                    player1.put(card)
            elif player1.empty() or cardP1['Power'] < cardP2['Power']:
                for card in cardsOnTable:
                    player2.put(card)
            else:  # If we end up here, it means both players ran out of cards simultaneously
                # Divide the cards evenly between players
                for i, card in enumerate(cardsOnTable):
                    (player1 if i % 2 == 0 else player2).put(card)
                
    if player1.empty():
        print('Player 2 won')
    else:
        print('Player 1 won')
War()




    
