from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
param = True

def caesar(plain_text,shift_number,mode):
    output = ""
    for texto in text:
        if texto not in alphabet:
            new_input = texto
        else:
            place = int(alphabet.index(texto))
            if direction == "d":
                new_index = place - shift
            elif direction == "e":
                new_index = place + shift
                if new_index >= 26:
                    new_index = ((shift % 26) - 26 ) + place  
            new_input = alphabet[new_index]
        output += new_input    
    print(f"Your {direction}encrypted text is: {output}")
    

while param:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    lenght = len(text)-1
    caesar(text,shift,direction)
    restart = input("Would you like to Encrypt/Decrypt something else: type 'y' for yes or 'n' for no \n")

    if restart == "n":
        print("Goodbye")
        param = False
