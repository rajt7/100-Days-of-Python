alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

flag = True

def caesar(direction, text, shift):
    caesar_text = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            caesar_text += alphabet[new_position]
        else:
            caesar_text += char
    print(f"The {direction}d text is: {caesar_text}")

while(flag):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift amount:\n"))

    shift = shift % 26

    caesar(direction, text, shift)
    
    result = input("Type 'yes' if you want to continue. Otherwise type 'no'.")
    if result == 'no':
        flag = False
        print("Goodbye") 