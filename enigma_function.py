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
start = time.process_time()
def key_guess():
    counter = 0
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0,26):
                counter += 1
                keyguess = capitalLetters[i] + capitalLetters[j] + capitalLetters[k]
                engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I, rotor.ROTOR_II, rotor.ROTOR_III, key=keyguess, plugs="AA BB CC DD EE")
                decryptedMessage = engine.encipher(ShakesHorribleMessage)
                if decryptedMessage[-12:] == crib:
                    return decryptedMessage, counter
            
#Print the Decoded message
#INSERT CODE HERE
decodedMessage, counter = key_guess()
time_used = time.process_time() - start
print(decodedMessage)
print(counter)
print(time_used)

# Count the attempts for 5 rotors and plugboard
plugboard = math.factorial(26)/(math.factorial(6)*math.factorial(10)*2**10)
rotornumber = 5*4*3

total_counter = counter*plugboard*rotornumber
total_time_used_hour = time_used*total_counter/(counter*3600)
print("With 10 pairs of plugboard and 5 rotors, the total attempts are",total_counter)
print("The approximate time is", total_time_used_hour,"hours")

time_used_1940 = 48828125*total_time_used_hour
