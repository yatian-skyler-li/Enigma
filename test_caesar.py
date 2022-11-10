# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string
from collections import Counter

#Wkcdob rkc qsfox Nylli k cymu Nylli sc pboo

def caesarKey(shift):
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
    return keys, invkeys

#encrypt
def encrypt(message):
    encryptedMessage = []
    for letter in message:
        if letter == ' ': #spaces
            encryptedMessage.append(letter)
        else:
            encryptedMessage.append(keys[letter])
    return ''.join(encryptedMessage)

#decrypt
def decrypt(encryptedMessage):
    decryptedMessage = []
    for letter in encryptedMessage:
        if letter == ' ': #spaces
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(invkeys[letter])
    return ''.join(decryptedMessage)


letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#create the Caesar cypher
totalLetters = 26

secretMessage = "Wkcdob rkc qsfox Nylli k cymu Nylli sc pboo"
print("Secret Message:",secretMessage)

#frequency of each letter
letter_counts = Counter(secretMessage)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    #print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    if (freq > maxFreq) and (letter != ' '):
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

for n in range(totalLetters):
    shift = n #COMPUTE SHIFT HERE
    print("Predicted Shift:", shift)
    keys, invkeys = caesarKey(shift)
    guessMessage = decrypt(secretMessage)
    print("My guess for the message is:",guessMessage)

