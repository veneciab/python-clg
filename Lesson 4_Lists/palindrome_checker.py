magic_word = input("What is today's magic word? ")
#elements of magic_word == magic_word.reverse

#string has to be converted to list
letters_in_magic_word = list(magic_word)
print(letters_in_magic_word)

#reverse the converted (string to) list
letters_in_magic_word.reverse()
print(letters_in_magic_word)

#convert list (of reverse elements) back into a string
letters_in_magic_word_string = ''.join(letters_in_magic_word)
print(letters_in_magic_word_string)

#check if word is a palindrome
if letters_in_magic_word_string == magic_word:
    print("TRUE")
else:
    print("FALSE")


