import time

logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(message, shift_number, direction):
    end_message = ""
    if direction == "decode":
        shift_number *= -1
    for letter in message:
        if letter.lower() in alphabet:
            position = alphabet.index(letter.lower())
            new_position = (position + shift_number) % len(alphabet)
            if letter.isupper():
                end_message += alphabet[new_position].upper()
            else:
                end_message += alphabet[new_position]
        else:
            end_message += letter
    print(f"Here's the {direction}d message: {end_message}")

play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n")) % len(alphabet)

    caesar(message, shift_number, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise, type any other key to exit:\n").lower()
    if restart != "yes":
        play_again = False
        print("\nThank you. Goodbye.")
        time.sleep(3)
