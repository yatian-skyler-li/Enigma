# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)
print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    if (freq > maxFreq) and (letter != ' '):
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = letters.index(str(maxLetter)) - letters.index('e') #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)

#decrypt
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        #INSERT CODE HERE
        keys[letter] = letters[(index + shift)%totalLetters]
        invkeys[letter] = letters[(index - shift)%totalLetters]

    else: #uppercase
        #INSERT CODE HERE
        keys[letter] = letters[(index + shift)%totalLetters + totalLetters]
        invkeys[letter] = letters[(index - shift)%totalLetters + totalLetters]

print("Cypher Dict:", keys)

decryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string
