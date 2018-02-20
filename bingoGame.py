import random
def getRandNumb(start,stop,k):
    return (random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],k))
def compare (playerList,computerList):
    playerList = list(playerList)
    computerList = list(computerList)
    if ( (playerList[0] in computerList) & (playerList[1] in computerList) &  (playerList[2] in computerList) & (playerList[3] in computerList) & (playerList[4] in computerList) ):
        return (True)
    else:
        return (False)
    print (list)
def bingo (nPlayers):
    computer = getRandNumb(0,80,80)
    players = []
    for i in range(nPlayers):
        players.append(getRandNumb(0,80,5))
    for i in range(5,80):
        for k in range(nPlayers):
            if (compare(players[k],computer[0:i])):
                return (i)
average = 0.0
n = 1000
for i in range(n):
    average += bingo(100)
average = average/100
print (average)
