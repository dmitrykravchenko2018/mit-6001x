#!/usr/bin/env python3

'''
	Week 2 Probem set 2 Problem 1
	Write a program to calculate the credit card balance
	after one year if a person only pays the minimum monthly 
	payment required by the credit card company each month.

'''

def calcCardBalance(balance, annualInterestRate, monthlyPaymentRate):
	monthlyInterestRate = annualInterestRate / 12.0

	for i in range(1, 13):
		minMounthlyPayment = balance * monthlyPaymentRate
		unpaidBalance = balance - minMounthlyPayment
		balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
		print("Month ", i, "Remaining balance: ", round(balance, 2))
	print("Remaining balance: ", round(balance, 2))

#calcCardBalance(42, 0.2, 0.04)

'''
	Problem 2
	write a program that calculates the minimum fixed monthly payment 
	needed in order pay off a credit card balance within 12 months.
	By a fixed monthly payment, we mean a single number which does not 
	change each month, but instead is a constant amount that will be paid each month.

'''
	
def calcLowMothlyPayment(balance, annualInterestRate):
	monthlyInterestRate = annualInterestRate / 12.0
	res = []

	def calcBalance(balance, minFixedPayment):
		
		for i in range(1, 13):
			unpaidBalance = balance - minFixedPayment
			balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

		return round(balance)

	lo, hi = 10, balance
	while lo <= hi:
		m = lo + (hi - lo) // 2
		m = round(m, -1)
		endBalance = calcBalance(balance, m)
		#print(endBalance, m)
		if endBalance < 0:
			hi = m - 10
			res.append(m)
		elif endBalance > 0:
			lo = m + 10
		else:
			res.append(m)

	return min(res)

#print("Lowest Payment: ", calcLowMothlyPayment(3329, 0.2)) # 310
#print("Lowest Payment: ", calcLowMothlyPayment(4773, 0.2)) # 440
#print("Lowest Payment: ", calcLowMothlyPayment(3926, 0.2)) # 360

'''
	Problem 3 
	Using Bisection Search to Make the Program Faster 
	Monthly interest rate = (Annual interest rate) / 12.0
	Monthly payment lower bound = Balance / 12
	Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0 
'''

def bisectionLowPayment(balance, annualInterestRate):
	monthlyInterestRate = annualInterestRate / 12.0
	E = 0.001 # I have no idea how to calculate this value, in this particular just let it be 0.1
	NMAX = 30000 # Max number of steps, used to avoid infinite loop

	def sign(x):
		return (x > 0) - (x < 0)

	def calcBalance(balance, minFixedPayment):
		
		for i in range(1, 13):
			unpaidBalance = balance - minFixedPayment
			balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

		return round(balance)

	lo = balance / 12.0
	hi = (balance * (1 + monthlyInterestRate)**12) / 12.0
	f_m = float('inf')
	f_lo = calcBalance(balance, lo)
	f_hi = calcBalance(balance, hi)
	n = 0

	while abs(f_m) > E and n <= NMAX:
		m = lo + (hi - lo) / 2
		f_m = calcBalance(balance, m)
		if sign(f_lo) == sign(f_m):
			lo = m
		elif sign(f_hi) == sign(f_m):
			hi = m
		n += 1

	return print("Failed: Number of steps exceeded") if n == NMAX else m

print("Lowest Payment: ", round(bisectionLowPayment(320000, 0.2), 2)) # 29157.09
print("Lowest Payment: ", round(bisectionLowPayment(999999, 0.18), 2)) # 90325.03
