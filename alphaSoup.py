
handle = open("alphaSoup.txt","r")  #opens the file to read the text
text = handle.read()                #create a handle for the text
letters = ("".join(text))          #create a space in between the letters

space = "_"
listExtras = []
extras = [pos for pos, char in enumerate(letters) if char == space]
for i in extras:
    extra = i + 1
    listExtras.append(extra)

for l in listExtras:
    letters = letters[:l] + letters[l+1:]

for x in "_":
    letters = letters.replace(x,"")

print listExtras


counts = dict()                     #delcare a dictonary
for x in letters:             #for loop to go through every letter in the text
    counts[x] = counts.get(x,0) + 1   #for each iteration in letters equals a key in the counts dictionary


for l in sorted(counts, key=counts.get, reverse=True):
    print l, counts[l]

print letters
#s = s[:pos] + s[(pos+1):]



#   blanks = letters.index("_")         #hold the index of a blank
#   xtra = blanks + 1                   #hold the index of the character after the blank
#   letters.replace(letters.index(blanks),"_")
#for e in letters:
 #   extra = letters.index('m')
#print extra


#letters3 = letters.replace("_", "") #replace  the '_' with nothing