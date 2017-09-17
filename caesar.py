def alphabet_position(letter):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    letter=letter.lower()
    loc=alphabet.index(letter)
    return loc

def rotate_character(char, rot):
    alphalow="abcdefghijklmnopqrstuvwxyz"
    alphaup="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char.isupper():
        new_loc=(alphaup.index(char)+rot)%26
        value=alphaup[new_loc]
    elif char.isalpha()==False:
        value=char
    elif char.islower():
        new_loc=(alphalow.index(char)+rot)%26
        value=alphalow[new_loc]
    return value

def rotate_string(text,rot):
    message=""
    for char in text:
        letter=rotate_character(char,rot)
        message+=letter
    return message

