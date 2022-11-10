# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time
import math

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
#print(lastMessage)
crib = "Hail Shakes!"
#crib_substring = ""
#print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE
start = time.time()
counter = 0
for i in range(0, 26):
    for j in range(0, 26):
        for k in range(0,26):
            counter += 1
            keyguess = capitalLetters[i] + capitalLetters[j] + capitalLetters[k]
            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I, rotor.ROTOR_II, rotor.ROTOR_III, key=keyguess, plugs="AA BB CC DD EE")
            decryptedMessage = engine.encipher(ShakesHorribleMessage)
            end = time.time()
            
#Print the Decoded message
#INSERT CODE HERE
            if decryptedMessage[-12:] == crib:
                print(decryptedMessage)
                print(counter)
                print(end-start)
                break

plugboard = math.factorial(26)/(math.factorial(6)*math.factorial(10)*2**10)
rotornumber = 5*4*3
total_counter = counter*plugboard*rotornumber
print(total_counter)
