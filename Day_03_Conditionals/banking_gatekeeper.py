# Algorithmic Number Reversal
target_num = int(input("Enter a 3-digit structural number (e.g., 582): "))
  #Execution phase 
units_digit = target_num % 10
dropped_factor = target_num // 10 
tens_digit = dropped_factor % 10 
hundreds_digit = dropped_factor // 10 
#Structural calculation reconstruction 
inverted_num = (units_digit * 100) + (tens_digit * 10) + hundreds_digit 
print(f"Original Configuration: {target_num}") 
print(f"Inverted Configuration : {inverted_num}")
