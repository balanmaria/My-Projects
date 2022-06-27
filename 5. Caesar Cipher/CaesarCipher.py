import Beginner.Day8.art

print(Beginner.Day8.art.logo)

def caeser(cdirection, ctext, cshift):
    end_text=""

    if cdirection == "decode":
        cshift *= -1

    for l in ctext:
        if l in alphabet:
            position=alphabet.index(l)
            new_position = position + cshift
            end_text += alphabet[new_position]
        else:
            end_text += l

    print(f"The {cdirection}d text is {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 # daca nr ptr care vrea sa se faca shit-area este mai mare decat nr de litere din alfabet (26)

    caeser(direction, text, shift)

    doc=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if doc == "no":
        should_continue=False
        print("Goodbye!")