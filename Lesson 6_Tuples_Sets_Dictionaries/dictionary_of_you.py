#create variable with user's name
user_name = "veebee"

#assign dictionary with user's details
user_fun_facts = {
    "suburb": "yarraville",
    "sport": "adventure racing",
    "beverage": "coffee",
    "trait": "hyperfocus",
    "language": "python",
    "kayak": "nk exrcize"
}

#run a for  loop through the dictionary and use F-string to print the key-value pairs
for key, value in user_fun_facts.items():
    print(f"Here's a fun fact, this person's fav {key} is {value}! \m/")

#adding data to dictionary using list
user_fun_facts["guitar style"] = "fingerstyle acoustic"
print(user_fun_facts)

#deleting data to dictionary
user_fun_facts.pop("suburb")
print(user_fun_facts)

#updating data to dictionary
user_fun_facts_extra = {"trail":"high country", "operating mode": "decisive"}
user_fun_facts.update(user_fun_facts_extra)
print(user_fun_facts)

#clearing data to dictionary
user_fun_facts.clear()
print(user_fun_facts)
