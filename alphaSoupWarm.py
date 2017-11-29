handle = open("alphaSoup.txt","r")  #opens the file to read the text
text = handle.read()                #create a handle for the text
letters = ("".join(text))           #join characters of text into letters variable

space = "_"                         #designates a variable for underscore
listExtras = []                     #initiate a list for the extra characters following the underscores
extras = [pos for pos, char in enumerate(letters) if char == space] #list comprehension statement to create a
for i in extras:                    #for loop to iterate through underscore indices and add one to to them
    extra = i + 1
    listExtras.append(extra)        #put extra characters indices into new list
    
listXtras = listExtras[::-1]        #put the values in listExtras array into reverse order and store

for l in listXtras:                 #loop thourgh list of extra characters
    letters = letters[:l] + letters[l+1:]   #splice letters string leaving out each index listed in listXtras
    
for x in "_":                       #loop though characters in letters relpacing the underscores with nothing
    letters = letters.replace(x,"")

counts = dict()                     #delcare a dictonary
for x in letters:                   #for loop to go through every letter left in the text
    counts[x] = counts.get(x,0) + 1   #for each iteration in letters equals a key in the counts dictionary

for l in sorted(counts, key=counts.get, reverse=True):  #sort the dictionary by the values and print
    print l, counts[l]
