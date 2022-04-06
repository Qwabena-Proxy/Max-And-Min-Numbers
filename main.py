def number_check(number) -> tuple:
  max_number = max(number)
  max_number = min(number)
  
  return f'{max_number} is the maximum number and {min_number} is the minimum number.'

#Seperate entry with ,
entry = input("Enter data:").split(",")
print(number_check(entry))
