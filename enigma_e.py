import string
import enigma
import rotor
import time

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
rotors = [rotor.ROTOR_I, rotor.ROTOR_II, rotor.ROTOR_III, rotor.ROTOR_IV]
start = time.time()
counter = 0
for i in range(0, 26):
    for j in range(0, 26):
        for k in range(0,26):
            counter += 1
            keyguess = capitalLetters[i] + capitalLetters[j] + capitalLetters[k]
            for l in range (0, 5):
                
                engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I, rotor.ROTOR_II, rotor.ROTOR_III, key=keyguess, plugs="AA BB CC DD EE")
                decryptedMessage = engine.encipher(ShakesHorribleMessage)
                end = time.time()
                if decryptedMessage[-12:] == crib:
                    print(decryptedMessage)
                    print(counter)
                    print(end-start)
                    break