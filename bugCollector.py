#Joseph Schwabauer
#Chapter 4 
#2/8/2017
#Programming exercise #1

#set a variable to track number of dyas
day = 1
#set a variable to hold the total number of bugs
total = 0

#loop through 5 days
while day <= 5 :
    #get from the user how many bugs were caught for each day
    print("Enter the bugs collected on day", day, ": ")
    bugs = float(input())
    #increment the day each time the loop runs 
    day = day + 1
    #add new entry of bugs caught to the total
    total += bugs
    
   #display to user the total number of bugs caught in five days 
print('In five days, you have collected', total, 'bugs.') 

