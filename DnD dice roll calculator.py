'''''''''''''''''''''''''''''''''''''''''''''
DnD Dice Roll Calculator


This program assists in the dice rolling 
part of DnD play. If you have your own dice 
to use, you can still use this program to 
add up the rolls for you and apply bonuses,
all for as many people as you want. It can
also tell you who's total roll is the highest
for initiative rolls. All input is validated
for correctness to an extent, and the user
is given a message indicating what was wrong
if incorrect input is submitted. This program
attempts to be very natural in its 
communication with the user. It accepts a 
range of words for indicating yes or no and 
it reports all numbers with correct grammar 
(a vs an).

First started: 12-29-2016
Last updated: 1-2-2016
Coded by: Joel N. Johnson
'''''''''''''''''''''''''''''''''''''''''''''


#Import Libraries
import random
import time

print
print

'''
#Testing the randomness of the random number generator. conclusion: it sucks but oh well
n = 1
total = 0
while n < 1000001:
    if random.randint(1,10) < 2:
        total = random.randint(1,100000) + total
    else:
        total = 10 + random.randint(1,1000000) + total
    n = n + 1
avg = total/n
print avg
'''

#Main Loop
repeat = 1
while repeat == 1:
    
    #Ask Number of People
    while True:
        try:
            print "How many people are we calculating for?"
            person = int(raw_input())
        except ValueError:
            print
            print "Oops, didn't catch that. I'm looking for numeric characters."
            print
            continue
        else:
            break
    
    #Ask Real or Simulated Dice
    while True:
        try:
            print
            print "Are you using real dice?"
            dice = raw_input()
            dice = float(dice)
        except ValueError:
            if not dice:
                print "Oops, didn't catch that."
                print
                continue
            else:
                dice = str(dice)
                break
        if dice*0 == 0:
            print
            print "Oops, didn't catch that. I'm looking for a nonnumeric response."
            print
            continue
        else:
            dice = str(dice)
            break
    
    i = 1
    values = []
    
    #Loop For Each Person
    while i <= person:
        
        firstRoll = 0
        secondRoll = 0
        bonus = 0
        
        #If no Dice, Ask Sided Die and Simulate Roll
        #Else, Ask Result of Roll
        if dice.lower() not in ['y', 'yes', 'yep', 'yessir', 'yeppers', 'indeed', 'yeah', 'great', 'sure', \
        'affirmative', 'yepp', 'yea', '10-4', 'yas', 'yass', 'yasss', 'yus', 'yuss', 'yusss', 'fuck you stop looking at my code']:
            while True:
                try:
                    print
                    print "Ok. For person %i, what sided die am I rolling?" % i
                    d = int(raw_input())
                except ValueError:
                    print
                    print "Oops, didn't catch that. I'm looking for numeric characters."
                    print
                    continue
                else:
                    break
            firstRoll = random.randint(1,d)
            j = 0
            while j < 50:
                print "%i\tRolling..." % random.randint(1,d)
                time.sleep(0.01)
                j = j + 1
            print
            print
            print
            print
            print
            if firstRoll in [8, 11, 18, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]:
                print "The die lands on an %i." % firstRoll
            else:
                print "The die lands on a %i." % firstRoll
        else:
            while True:
                try:
                    print
                    print "Value of person %i's first roll: " % i
                    firstRoll = int(raw_input())
                except ValueError:
                    print
                    print "Oops, didn't catch that. I'm looking for numeric characters."
                    print
                    continue
                else:
                    break
        
        #Ask if Rolling a Die Twice Because Avgs
        while True:
            try:
                print
                print "Is a second roll required for this person?"
                yesno = raw_input()
                yesno = float(yesno)
            except ValueError:
                if not yesno:
                    print "Oops, didn't catch that."
                    print
                    continue
                else:
                    yesno = str(yesno)
                    break
            if yesno*0 == 0:
                print
                print "Oops, didn't catch that. I'm looking for a nonnumeric response."
                print
                continue
            else:
                yesno = str(yesno)
                break
        
        #If Rolling Twice
        if yesno.lower() in ['y', 'yes', 'yep', 'yessir', 'yeppers', 'indeed', 'yeah', 'great', 'sure', \
        'affirmative', 'yepp', 'yea', '10-4', 'yas', 'yass', 'yasss', 'yus', 'yuss', 'yusss', 'fuck you stop looking at my code']:
            #If no Dice, Simulate Second Roll
            #If Dice, Ask Result of Second Roll
            if dice.lower not in ['y', 'yes', 'yep', 'yessir', 'yeppers', 'indeed', 'yeah', 'great', 'sure', \
            'affirmative', 'yepp', 'yea', '10-4', 'yas', 'yass', 'yasss', 'yus', 'yuss', 'yusss', 'fuck you stop looking at my code']:
                print
                print "Rolling a %i sided die again..." % d
                time.sleep(2)
                secondRoll = random.randint(1,d)
                j = 0
                while j < 50:
                    print "%i\tRolling..." % random.randint(1,d)
                    time.sleep(0.01)
                    j = j + 1
                print
                print
                print
                print
                print
                if secondRoll in [8, 11, 18, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]:
                    print "The die lands on an %i." % secondRoll
                else:
                    print "The die lands on a %i." % secondRoll
            else: 
                while True:
                    try:
                        print
                        print "Value of second roll: "
                        secondRoll = int(raw_input())
                    except ValueError:
                        print
                        print "Oops, didn't catch that. I'm looking for numeric characters."
                        print
                        continue
                    else:
                        break
        
        #Ask for Bonus  
        while True:
            try:
                print
                print "Value of person %i's bonus: " % i
                bonus = int(raw_input())
            except ValueError:
                print
                print "Oops, didn't catch that. I'm looking for numeric characters."
                print
                continue
            else:
                break
       
        #Add Roll(s) and bonus 
        total = firstRoll + secondRoll + bonus
        
        #Store Total for this Person in Next Available Array Index
        values.append(total)
        i = i + 1
    
    print    
    i = 1
    
    #Repoet Each Person's Total Roll
    while i <= person:
        print "Person %d's total roll is %d." % (i, values[i-1])
        i = i + 1
    
    #Ask if Highest Roll is Needed
    while True:
        try:
            print
            print
            print "Would you like me to report the highest roll?"
            yesno = raw_input()
            yesno = float(yesno)
        except ValueError:
            if not yesno:
                print "Oops, didn't catch that."
                print
                continue
            else:
                yesno = str(yesno)
                break
        if yesno*0 == 0:
            print
            print "Oops, didn't catch that. I'm looking for a nonnumeric response."
            print
            continue
        else:
            yesno = str(yesno)
            break
    
    print
    
    #If Highest Roll is Needed, Print Player with Highest Roll and Value of Roll
    if yesno.lower() in ['y', 'yes', 'yep', 'yessir', 'yeppers', 'indeed', 'yeah', 'great', 'sure', \
    	'affirmative', 'yepp', 'yea', 'yas', 'yass', 'yasss', 'yus', 'yuss', 'yusss', '10-4', 'fuck you stop looking at my code']:
        import operator
        i, highest = max(enumerate(values), key=operator.itemgetter(1))
        
        #Determine if Highest Roll is Said with 'a' or 'an'
        if highest in [8, 11, 18, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]:
            print "Player %d has the highest roll with an %d." % (i+1, highest)
        else:
            print "Player %d has the highest roll with a %d." % (i+1, highest)
    
    #Ask to Restart Program
    while True:
        try:
            print
            print
            print "Repeat program?"
            yesno = raw_input()
            yesno = float(yesno)
        except ValueError:
            if not yesno:
                print "Oops, didn't catch that."
                print
                continue
            else:
                yesno = str(yesno)
                break
        if yesno*0 == 0:
            print
            print "Oops, didn't catch that. I'm looking for a nonnumeric response."
            print
            continue
        else:
            yesno = str(yesno)
            break
    
    #If Restart is desired, Repeat Program
    if yesno.lower() in ['y', 'yes', 'yep', 'yessir', 'yeppers', 'indeed', 'yeah', 'great', 'sure', \
    'affirmative', 'yepp', 'yea', 'yas', 'yass', 'yas', 'yass', 'yasss', 'yus', 'yuss', 'yusss', '10-4', 'fuck you stop looking at my code']:
        repeat = 1
    else:
        repeat = 0
        
    print
    
print