def shift_letter(letter, k):
    curr_ord = ord(letter)
    k = k % 26
    if curr_ord >= 97 and curr_ord <= 122:
        new_ord = curr_ord + k
        if new_ord > 122:
            diff = new_ord % 123
            new_ord = 97 + diff
        return chr(new_ord)
    elif curr_ord >= 65 and curr_ord <= 90:
        new_ord = curr_ord + k
        if new_ord > 90:
            diff = new_ord % 91
            new_ord = 65 + diff
            return chr(new_ord)
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
                
