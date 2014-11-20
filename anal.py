from math import *
import os

price_info = open('1month15.txt', 'r')
perfectBuys = open('perfect.txt', 'r')

cap_price = []
perfect_buys = []

for line in price_info:
	cap_price.append(line)

for line in perfectBuys:
	perfect_buys.append(line.split())

def d(p1, p2):
	return p2-p1

def d2(p1, p2, p3):
	return p1 - 2*p2 + p3

p1 = 388.22
p2 = 387.91
buying = False

index = 0
perf_buy = []
perf_sell = []

for i in range(len(perfect_buys)):
	if perfect_buys[i][0] == "SELL":
		temp = []	
		temp.append(perfect_buys[i-1][2])
		temp.append(perfect_buys[i-2][2])
		temp.append(perfect_buys[i-3][2])
		perf_sell.append(temp)
	if perfect_buys[i][0] == "BUY":
		temp = []	
		temp.append(perfect_buys[i-1][2])
		temp.append(perfect_buys[i-2][2])
		temp.append(perfect_buys[i-3][2])
		perf_buy.append(temp)

for i in perf_buy:
	for j in range(3):
		print i[j]