import os

rf = open('1month15.txt', 'r')
os.system('touch prices.txt')
wf = open('prices.txt', 'w')
os.system('touch sell.txt')
sf = open('sell.txt', 'w')
os.system('touch buy.txt')
bf = open('buy.txt', 'w')

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
	bank = 50
	wallet = 50
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

resetValues()

for i in closing_price:
	global lastP
	global pCoins
	global lastP
	tempP = float(i)
	if (tempP < lastP and selling):
		sell(lastP)
		print "Sold:   price = ", "{:.2f}".format(lastP), " ||  money = ", "{:.2f}".format(bank+wallet)
		soldstring = "Sold:   price = "+str("{:.2f}".format(lastP))+" ||  money = "+str("{:.2f}".format(bank+wallet))
		wf.write(soldstring)
		wf.write('\n')
		sf.write(str(lastP))
		sf.write('\n')
	if (buying and tempP > lastP):
		buy(lastP)
		print "Buy:    price = ", "{:.2f}".format(lastP), " ||  money = ", "{:.2f}".format(bank+wallet)
		print "*******************************************************"
		buystring = "Buy:    price = "+str("{:.2f}".format(lastP))+" ||  money = "+str("{:.2f}".format(bank+wallet))
		wf.write(buystring)
		wf.write('\n')
		wf.write("*******************************************************")
		wf.write('\n')
		bf.write(str(lastP))
		bf.write('\n')
	lastP = tempP