import csv

d = dict() # create empty dict

# create key value pairs
with open('MORSE.csv') as file:
    for line in file:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val
d.pop('LETTER')

# enquire user input
user_input = input("What is the word: ").upper()
split = [char for char in user_input]

# convert word to morse code
morse_code = []
for x in split:
    morse_code.append(d.get(x))

print(f'Your coded word: {"".join(morse_code)}')
