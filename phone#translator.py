#Joseph Schwabauer
#Number Translator HW
#3/29/17
#CSC-121


#initialize an empty array
phoneA = [ ]

#method header
def main():
    #get a ten digit phone number from the user
    phone = str(input("Please enter a 10 digit phone number that is written in alphabetic letters: "))
    #loop through input varialbe and append each index value to the empty array
    for p in phone:
        phoneA.append(p)

    #loop through each index of the array
    for n in range(len(phoneA)):
        #if value in index is an alphabetical value replace with corresponding number
        if phoneA[n].isalpha():  
            if phoneA[n]== 'a':
                phoneA[n] = 2
            elif phoneA[n]== 'b':
                phoneA[n] = 2
            elif phoneA[n]== 'c':
                phoneA[n] = 2
            elif phoneA[n]== 'd':
                phoneA[n] = 3
            elif phoneA[n]== 'e':
                phoneA[n] = 3
            elif phoneA[n]== 'f':
                phoneA[n] = 3
            elif phoneA[n]== 'g':
                phoneA[n] = 4
            elif phoneA[n]== 'h':
                phoneA[n] = 4
            elif phoneA[n]== 'i':
                phoneA[n] = 4
            elif phoneA[n]== 'j':
                phoneA[n] = 5
            elif phoneA[n]== 'k':
                phoneA[n] = 5
            elif phoneA[n]== 'l':
                phoneA[n] = 5
            elif phoneA[n]== 'm':
                phoneA[n] = 6
            elif phoneA[n]== 'n':
                phoneA[n] = 6
            elif phoneA[n]== 'o':
                phoneA[n] = 6
            elif phoneA[n]== 'p':
                phoneA[n] = 7
            elif phoneA[n]== 'q':
                phoneA[n] = 7
            elif phoneA[n]== 'r':
                phoneA[n] = 7
            elif phoneA[n]== 's':
                phoneA[n] = 7
            elif phoneA[n]== 't':
                phoneA[n] = 8
            elif phoneA[n]== 'u':
                phoneA[n] = 8
            elif phoneA[n]== 'v':
                phoneA[n] = 8
            elif phoneA[n]== 'w':
                phoneA[n] = 9
            elif phoneA[n]== 'x':
                phoneA[n] = 9
            elif phoneA[n]== 'y':
                phoneA[n] = 9
            elif phoneA[n]== 'z':
                phoneA[n] = 9
        #if value in index is not alphabetical, keep value the same               
        else:
            phoneA[n] = phoneA[n]

    print(phoneA)

            
            
main()
