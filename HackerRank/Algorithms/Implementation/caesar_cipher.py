def shift_letter(letter, k):
    if letter.isalpha():
        lowend = 97
        highend = 122
        if letter.isupper():
            lowend = 65
            highend = 90
        k = k % 26
        new_ord = ord(letter) + k
        if new_ord > highend:
            new_ord = lowend + (new_ord % (highend + 1))
        return chr(new_ord)
    else:
        return letter
    
text_length = int(input())
text = input()
k = int(input())
new_text = ""
for letter in text:
    new_text += shift_letter(letter, k)
print(new_text)
                
