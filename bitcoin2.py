import os
rf = open('1month15.txt', 'r')
#os.system('touch output.txt')
#wf = open('output.txt', 'w')

closing_price = []

for line in rf:
	closing_price.append(line)

def resetValues():
	global bank
	global pCoins
	global nCoins
	global wallet
	global buying
	global selling
	global lastP
	global boughtP
	bank = 0.5
	wallet = 0.5
	pCoins = float(closing_price[0])
	nCoins = wallet/pCoins
	lastP = pCoins
	buying = False
	selling = True
	lastP = float(closing_price[0])
	boughtP = pCoins

def sell(price):
	global bank
	global pCoins
	global nCoins
	global wallet
	global buying
	global selling
	buying = True
	selling = False
	pCoins = price
	wallet = nCoins*pCoins
	bank = bank + wallet
	wallet = 0

def buy(price):
	global bank
	global pCoins
	global nCoins
	global wallet
	global buying
	global selling
	global boughtP
	buying = False
	selling = True
	wallet = bank/2
	bank = bank - wallet
	pCoins = price
	boughtP = price
	nCoins = wallet/pCoins

def find(min, max):
	for i in closing_price:
		global lastP
		global pCoins
		tempP = float(i)
		if (tempP/boughtP > max and selling):
			sell(tempP)
		elif (tempP/lastP < min and buying):
			buy(tempP)
		lastP = tempP

highest = 1.0
highestI = None
highestJ = None

resetValues()

for i in range(25):
	for j in range(25):
		sellP = 1.0 + i/100.0
		buyP = 1.0 - j/100.0
		find(buyP, sellP)
		if (bank+wallet > highest):
			highest = bank+wallet
			highestI = i
			highestJ = j
		resetValues()

count = 0

resetValues()

for i in closing_price:
		count = count + 1
		tempP = float(i)
		if (tempP/boughtP > 1.0 + highestI/100.0 and selling):
			oldP = boughtP
			sell(tempP)
			print count, "::: Sold at:   ", pCoins, "Percent = ", tempP/oldP
		elif (tempP/lastP < 1.0 - highestJ/100.0 and buying):
			buy(tempP)
			print count, "::: Bought at: ", pCoins, "Percent = ", tempP/lastP
		lastP = tempP

print "buy P = ", 1.0 - highestJ/100.0, "  ||  sell P = ", 1.0 + highestI/100.0, "  || money = ", bank+wallet

print "****************************"\

resetValues()

count = 0

for i in closing_price:
		count = count + 1
		tempP = float(i)
		if (tempP/boughtP > 1.13 and selling):
			oldP = boughtP
			sell(tempP)
			print count, "::: Sold at:   ", pCoins, "Percent = ", tempP/oldP
		elif (tempP/lastP < 0.97 and buying):
			buy(tempP)
			print count, "::: Bought at: ", pCoins, "Percent = ", tempP/lastP
		lastP = tempP

print "money = ", bank + wallet