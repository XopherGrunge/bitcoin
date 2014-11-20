from math import *
import os

rf = open('1month15.txt', 'r')
os.system('touch perfect.txt')
wf = open('perfect.txt', 'w')

cap_price = []

for line in rf:
	cap_price.append(line)

def d(p1, p2):
	return p2-p1

def d2(p1, p2, p3):
	return p1 - 2*p2 + p3

p1 = 388.22
p2 = 387.91
buying = False

for i in cap_price:
	p3 = float(i)
	if (buying and p3<p2):
		print "SELL"
		wf.write("SELL\n")
		buying = False
	elif (not buying and p3>p2):
		print "BUY"
		wf.write("BUY\n")
		buying = True
	print "**********************"
	print "d1 = ", d(p2, p3)
	print "d2 = ", d2(p1, p2, p3)
	print "price = ", p3
	wf.write("***********************\n")
	wf.write("d1 = "+str(d(p2, p3))+"\n")
	wf.write("d2 = "+str(d2(p1, p2, p3))+"\n")
	wf.write("price = "+str(p3)+"\n")
	p1 = p2
	p2 = p3
