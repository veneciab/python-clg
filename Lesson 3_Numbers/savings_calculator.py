money_start = input("How much money is available at the start?: ")
saving_years = input("How many years to save to get to FI?: ")
interest_rate = input("What is the best interest rate?: ")
print(float(money_start))
print(int(saving_years))
print(float(interest_rate))

money_result = float(money_start) * float(interest_rate) * int(saving_years)
print(str(money_result))
print(f"You'll need a minimum of ${money_result} to hit FI")
print(money_result > 10000)


