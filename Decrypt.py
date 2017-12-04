#!/usr/bin/python3
import string

inText = input("Insert text to decrypt: ")
shift = int(input("Insert Shift, integer 1-26: "))
inText = inText.lower()  
inText = inText.replace(" ","") 
TextCrypt = ""
alphabet = dict(zip(string.ascii_lowercase, range(1, 27)))
revAlphabet = {v: k for k, v in alphabet.items()}   #this creates a reverse dictionary of the alphabet
for index, value in enumerate(inText):    #goes through the entered text and decrypts it
    temp = alphabet[value]
    temp = temp - shift
    if temp < 0:
        temp += 26
    
    TextCrypt += revAlphabet[temp]
print(TextCrypt)    #prints the decrypted text
