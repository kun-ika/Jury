m = int(input())

def reflection(value):
    words = []
    word = ''
    for char in value:
        if char != ',':
            word += char
        else:
            words.append(word)
            word = ''
    words.append(word)
    for word in reversed(words): 
        print(word)

input_str = input()
reflection(input_str)
