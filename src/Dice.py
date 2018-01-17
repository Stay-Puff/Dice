'''
Created on Jan 7, 2018

@author: Admin
'''
import random

numberOfDice = input("How many dice are you using?")

min = 1
max = input("How many sides does each dice have?")

roll_again = "yes"


while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    tempDice = numberOfDice
    tempValue = 0
    totalValue = 0
    while tempDice > 0:
        tempValue = random.randint(min, max)
        print tempValue
        totalValue = totalValue + tempValue
        tempDice = tempDice - 1
    print "Total Value: "
    print totalValue
    roll_again = raw_input("Roll the dices again?")