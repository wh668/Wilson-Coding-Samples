# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import math 

"""
Counting Sundays Problem

Goal: Count # of Sundays that fall on the first of the month during 
the 21st century.

If a month has 31 days, the first day of the next month falls 
3 days later in the week.

If a month has 30 days, the first day of the next month falls 
2 days later in the week. 

The first day of March always falls on the same day of the 
week as the first day of February, with the exception of leap years,
in which the first day of March falls 1 day later in the week. 

Jan 1, 1900 is a Monday.

My approach uses modular arithmetic with the following scheme:
    
    Monday = 1
    Tuesday = 2
    .
    .
    .
    Sunday = 7
    
Start with Jan 1, 1900 = 1 => Jan 1, 1901 = 2 as 1900 % 400 != 0. 

First note the "obvious" solution where we take 12 * 100 = 1200 months with 
roughly equal day distribution => 1200/7 ~ 171 once rounded. 
"""

'Declare our counting variables'
FirstDayCounter = 2
MonthCounter = 1
YearCounter = 1901
ShortMonth = [4, 6, 9, 11]
LongMonth = [1, 3, 5, 7, 8, 10, 12]
SundayCounter = 0

'Iterate through each year and increment once we check each first day.'

'Increment Sunday counter when we have a first day on a Sunday (7)'

for YearCounter in range(1901, 2001):
      MonthCoutner = 1
      
      for MonthCounter in range(1, 13):
            if MonthCounter in ShortMonth:
                FirstDayCounter += 2
            elif MonthCounter in LongMonth:
                FirstDayCounter += 3
            else:
                if YearCounter % 100==0 and YearCounter%400==0:
                    FirstDayCounter += 1
                    
                elif YearCounter % 100 !=0 and YearCounter % 4 == 0:
                    FirstDayCounter += 1
            if FirstDayCounter % 7 == 0:
                SundayCounter += 1
            MonthCounter += 1

      YearCounter += 1

print(SundayCounter)



"""
Reduced proper fraction problem

Goal is to count the number of reduced fractions p/q with p<q and q <= 12000
where 1/3 < p/q < 1/2 

Utilizing the function gcd() from math package
"""


def ReducedFrac():
    arr = []
    p = 1
    count = 0
    for p in range(1,12000):
        for q in range(2,12001):
            if math.gcd(p, q) == 1 and p<q:
                arr.append(p/q)
                if p/q < 1/2 and p/q > 1/3:
                    count += 1
            q += 1
        p += 1 
    return count

' print(ReducedFrac()) ' 



"""
This problem counts the least number to reach .99 ratio for bouncy numbers to 
total numbers. 

We know for the first 1000 numbers, 525 are bouncy => raito = .525

Bouncy numbers are defined as non monotonic w.r.t digits

123345 -> Inc Number
543321 -> Dec Number
192836 -> Bouncy Number
"""

def getDigit(number, n):
    return number // 10**n % 10

def isIncNum(number):
    flag = True 
    k = 1
    numAsStr = str(number)
    while k in range(len(numAsStr)) and flag == True:
        if(getDigit(number,k) > getDigit(number, k-1)):
            flag = False
        k += 1
    return flag

def isDecNum(number):
    flag = True 
    k = 1
    numAsStr = str(number)
    while k in range(len(numAsStr)) and flag == True:
        if(getDigit(number,k) < getDigit(number, k-1)):
            flag = False
        k += 1
    return flag

def bouncyCounter():
    bouncyNum = 525
    currentNum = 1000
    ratioCount = 1.0
    
    while int(ratioCount) in range(99):
        currentNum += 1
        if isIncNum(currentNum) or isDecNum(currentNum) :
            bouncyNum += 0
        else:
            bouncyNum += 1
        ratioCount =( float(bouncyNum) / float(currentNum) )*100
    
    return currentNum

' print(bouncyCounter()) ' 





"""
Checking which is the first prime number which can be written as a 
summation of primes in over 5000 unique ways. 
"""
from time import time

start = time()

def checkIfPrime(n):
    isPrime = True
    for i in range(2,n):
        if n%i==0:
            isPrime = False
            break
    return isPrime

primeList = [2]
for num in range(3,10000):
    if checkIfPrime(num):
        primeList.append(num)

        
max=100
mat = []
for i in range(0,max+1):
    mm = [0]*(max+1)
    mat.append(mm) 

mat[2][2]=1


for a in range(2,max+1):
    bindex=0
    bPrime=primeList[bindex]
    while bPrime<a+1:
        if a==bPrime: mat[a][bPrime]=1
        for i in range(1,bPrime+1):      
            val=mat[a-bPrime][i]
            mat[a][bPrime]+=val
            if a==bPrime: mat[a][bPrime]=1
        bindex+=1
        bPrime=primeList[bindex]
max=10 
sums=0
while sums<5001:
    sums=0
    for i in range(0,max+1):
        sums +=mat[max][i]

    if checkIfPrime(max): sums-=1    
    max+=1
result=max-1


stop = time()
print(f'Result: {result}')
print(f'Time: {stop - start:4e}s')



"""
Square Summations

Given ( (a-1)^n + (a+1)^n )/a^2, the goal is to sum up the maximum remainder
for each 3 \le a \le 1000 and varying n

By virtue of the binomial expansion, we get for any a, the maximum remainder
can be written as 2a * floor[(a-1)/2] 
"""

def squareSummations():
    a = 3
    totalSum = 0
    for a in range(3,1001):
        totalSum += 2*a*math.floor(float((a-1)/2))
    return totalSum

' print(squareSummations()) ' 
        
