#import module where function to count vowels was created
import counting_vowels

#ask user their full name
full_name = input("Why hello there! Pray tell what is your full name?")

#convert characters to lower case
full_name_converted = full_name.lower()

print(f"Thanks! What a beautiful name {full_name}")
print(f"I like how there are {count} vowels in your name")
