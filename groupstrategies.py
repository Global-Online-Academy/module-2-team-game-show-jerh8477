# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING

import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split","steal"),("split","split"),("steal","split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy: Everytime the opponent steals, our "trust factor aka splitpercent" goes down by 20%, and everytime they split, the trust factor goes up by 2%.  
# 
def USC1(history): 
    splitpercent = 100
    for i in range(0, len(history)): 
        oppMove = history[i][1]
        if oppMove == 'steal': 
            splitpercent -= 20 
        else:
            splitpercent += 2
        
        if splitpercent > 100: 
            splitpercent = 100 
        elif splitpercent < 0:
            splitpercent = 0 
        
    num = random.randint(0, 100)
    if num > splitpercent: 
        print(splitpercent)
        return 'steal'
    else: 
        print(splitpercent)
        return 'split'

# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
