#imports

# # # # #
#variables

alphabet = 'abcdefghijklmnopqrstuvwxyz' 

# # # # # # #
#functions
def shift_letter(letter, shift):
    index = alphabet.index(letter)
    index = (index + shift)%26
    return alphabet[index]


def caesar_shift(phrase, shift):
    result = ""
    for letter in phrase:
        result += shift_letter(letter, shift)
    return result

def brute_force_caesar_cypher(phrase):
    for shift in range(1, 26):
        print(caesar_shift(phrase, shift))

#

#shift one letter
#print(shift_letter('a', 3))

#shift phrase
brute_force_caesar_cypher('zebra')