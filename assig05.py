#write a program to find even or odd
print("question no #1:Find even or odd numbers?\n")
def find_even():
     while True:
          try:
             num = int(input("Enter a number to find even or odd:"))
             if num % 2 == 0:
               print("The number is even.")
               break
             else:
               print("The number is odd.")
          except ValueError:
               print("invalied number. Please try valied number.")
               return num
num = find_even()

               
  
print("\n||-----------------Question End------------------||\n")


#wehether it is devisible by both 2 and 3
print("question no #2:Find the number divider by both 2 and 3?\n")
def devied_number():
    while True:
        try:
          num = int(input("Enter a nnumber:"))
          if num % 2 == 0 and num % 3 == 0:
             print("This num is divisible by both 2 and 3")
             break
          else:
             print ("This num is not divisible by both 2 and 3")
        except ValueError:
             print("Invalid number. Please try again with valid number")
             return num
num = devied_number()



print("\n||-----------------Question End------------------||\n")


#write a program to check positive negative or zero.
print("question no #3: Check positive negative or zero?\n")
def check_numbers():
    while True:
        try:
         num = int(input("Enter a number :"))
         if num>0:
           print("The number is positive.")
         if num<0:
           print("THE number is negative.")
         if num==0:
            print("The number is zero.")
        except ValueError:
           print("invalid number. please try again.")
           break 
        return num
num = check_numbers()
   


print("\n||-----------------Question End------------------||\n")


# Find the age
print("Question no #4: Find the age ?\n")
from datetime import datetime
def CalculateAge():
  while True:
    try:
      birth_year = int(input("Enter your birth year: "))
      # current_year = int(input("Enter the current year: "))
      current_year = datetime.now().year
      if birth_year > current_year:
        print("Invalid year. Please enter a year that is less than or equal to the current year.")
        break
      else:
        age = current_year - birth_year
        return age
    except ValueError:
      print("Invalid input. Please enter a valid year.")
      
age = CalculateAge()



print("\n||-----------------Question End------------------||\n")


# write a program to check who is valid for voting.
print("Question no #5:check who is valid for voting?\n")

print(f"Your age is {age} years.")
def vote_check():
    while True:
       ask = str(input("They have a nationaleity of pakistani: "))
       if ask == "yes":
          print("You are eligible to vote")
       elif ask == "no":
          print("please obtain a vaild ID to vote")
       else: 
        print("Invalid input. Please enter either 'yes' or 'no'.")
       return ask
ask = vote_check()



print("\n||-----------------Question End------------------||\n")


#write a program to check the age of thhe people are child,tenngar,adult and senior.
print("question no #6: Find the age age adult child teenger or senior\n")
def ageDetermine():
    while True:
        from datetime import datetime
        currentYear = datetime.now().year
        birthYear = int(input("Enter your birth year: "))
        age = currentYear - birthYear
        print(f"Your Age is: {age}")
        if age <=12:
           print("They are a child.")
        if age >=13 and age <= 19:
           print("They are a teenager.") 
        if age >=20 and age <=59:
           print("They are an adult.")
        if age >=60:
           print("They are a senior.")
        return age
age = ageDetermine()


print("\n||-----------------Question End------------------||\n")



#Write a program to find month numbers.
print("Question no #7 :Find the month name for the given number?\n")
def month_name():    
    month = int(input("Enter a month number: "))
    match month:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:  
            print("Invalid")
    return month_name


result = month_name()
