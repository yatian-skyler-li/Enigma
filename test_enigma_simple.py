# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import enigma
import rotor

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD EE")

#print(engine)

# Part a)
message = "Hello World"
print("Message:", message)
secret = engine.encipher(message)
print("Encoded Message:", secret)

#Write code to decrypt message below
#HINT: Reuse the code above to do it. You do not need to write a decrypt function.
#INSERT CODE HERE
engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD EE")
newMessage = engine.encipher(secret)
print(newMessage)

#Part b)
ShakesHorribleMessage = "Vxye ajgh D yf? Ptn uluo yjgco L ws nznde czidn. Bsj ccj qdbk qjph wpw ypxvu!"
#ShakesHorribleMessage2 = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"

#Write code to decrypt message above
#INSERT CODE HERE

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                                plugs="AA BB CC DD EE")
                                
guessMessage = engine.encipher(ShakesHorribleMessage)
print(guessMessage)
