from math import *
import numpy
import os

price_info = open('1month15.txt', 'r')
perfectBuys = open('perfect.txt', 'r')

os.system('touch d2sell.txt')
d2sells = open('d2sell.txt', 'w')

cap_price = []
perfect_buys = []

for line in price_info:
	cap_price.append(float(line))

for line in perfectBuys:
	perfect_buys.append(line.split())

def d(p1, p2):
	return p2-p1

def d2(p1, p2, p3):
	return p1 - 2*p2 + p3

def avg(s, n):
	return s/n

p1 = 388.22
p2 = 387.91
buying = False

index = -1
perf_buy = []
perf_sell = []

for i in range(len(perfect_buys)):
	if perfect_buys[i][0] == '***********************':
		index = index + 1
	if perfect_buys[i][0] == "SELL":
		temp = []	
		temp.append(index)
		temp.append(float(perfect_buys[i-1][2]))
		temp.append(float(perfect_buys[i-3][2]))
		temp.append(float(perfect_buys[i-2][2]))
		perf_sell.append(temp)
	if perfect_buys[i][0] == "BUY":
		temp = []	
		temp.append(index)
		temp.append(float(perfect_buys[i-1][2]))
		temp.append(float(perfect_buys[i-3][2]))
		temp.append(float(perfect_buys[i-2][2]))
		perf_buy.append(temp)

d1bSum = 0 
d2bSum = 0
d1sSum = 0 
d2sSum = 0

for i in perf_buy:
	d2sells.write(str(i[2])+"\n")
	d1bSum = d1bSum + i[2]
	d2bSum = d2bSum + i[3]

for i in perf_sell:
	d1sSum = d1sSum + i[2]
	d2sSum = d2sSum + i[3]

print "Sell d1 average = ",avg(d1sSum, len(perf_sell))
print "Sell d2 average = ",avg(d2sSum, len(perf_sell))
print "Buy d1 average = ",avg(d1bSum, len(perf_buy))
print "Buy d2 average = ",avg(d2bSum, len(perf_buy))

tempStats = []

for i in perf_buy:
	if i[3]!=0:
		tempStats.append(i[2]/i[3])

print numpy.mean(tempStats)
print numpy.std(tempStats)