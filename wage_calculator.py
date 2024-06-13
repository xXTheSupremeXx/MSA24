#Write a program to get the hours worked and hourly wage

#Write a function to get a 2 inputs from the user: Hours Worked and hourly wage
def get_positive_float_input():
  #ask a user to enter their hors worked, and validate correct input
  #if bad input, reprompt the user
  user_hours_worked = 0
  while(True):
    try:
      user_hours_worked = float(input("Enter how many hours you have worked daily: "))
      #check if hours worked is > 0. If not, reprompt the user
      if user_hours_worked <= 0:
        print("ERROR: Enter a number greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")

  return user_hours_worked

def get_positive_float_hourly_wage_input():
  #ask a user to enter their hors worked, and validate correct input
  #if bad input, reprompt the user
  user_hourly_wage = 0
  while(True):
    try:
      user_hourly_wage = float(input("Enter your hourly wage: "))
      #check if hours worked is > 0. If not, reprompt the user
      if user_hourly_wage <= 0:
        print("ERROR: Enter a number greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")

  return user_hourly_wage
  
#INPUT
#get hours and hourly wage from the user
user_hours_worked = get_positive_float_input()
user_hourly_wage = get_positive_float_hourly_wage_input()

#PROCESSING
#use a conversion to calculate the total money
taxes_percentage = .88
days = 350
annual_wage_before_tax = user_hours_worked*user_hourly_wage*days
annual_wage_after_tax = (user_hours_worked*user_hourly_wage*days)/taxes_percentage
total_tax_amount = annual_wage_after_tax - annual_wage_before_tax

#OUTPUT
#print output to the user
print(f'\nPay Advice\n----------\nHours Worked: {user_hours_worked}$\nHourly Wage: {user_hourly_wage}$\nWage before tax: {annual_wage_before_tax:.2f}$\nTax Amount: {total_tax_amount:.2f}$\nWage After Tax: {annual_wage_after_tax:.2f}$')
