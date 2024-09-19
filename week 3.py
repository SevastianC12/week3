#Write a program that ask teh user for a number in the range of 1-7
#each number corresponding to a day in the week exp: (Monday=1, Tuesday=2, etc).
number_of_days=int(input('Enter a number between 1 and 7: '))
if number_of_days==1:
    print('Monday')
elif number_of_days==2:
    print('Tuesday')
elif number_of_days==3:
    print('Wednesday')
elif number_of_days==4:
    print('Thursday')
elif number_of_days==5:
    print('Friday')
elif number_of_days==6:
    print('Saturday')
elif number_of_days==7:
    print('Sunday')
else:
    print('Error: The number must be between 1 and 7.')

#Write a program that ask for the length and width of two rectangles.
#The program should tell the user which rectangle has the greater area, or if the areas are the same.
length1=int(input('Enter the length of recatangle 1: '))
width1=int(input('Enter the width of rectangle 1: '))

length2=int(input('Enter the length of rectangle 2: '))
width2=int(input('Enter the width of rectangle 2: '))

area1= length1 * width1
area2= length2 * width2

if area1> area2:
    print(' Rectangle 1 has the greater area: ')
elif area2> area1:
    print('Rectangle 2 has the greater area: ')
else:
    print('Both have the same area. ')

#Write a program that ask the user to enter a person's age.
#The program should display a message indicating whether th person is an infant, a child, a teenager, or an adult.
persons_age=int(input('Enter your age: '))


if persons_age<=1:
    print('The person is an infant')
elif 1<persons_age<13:
    print('The person is a child')
elif 13<=persons_age<19:
    print('The person is a teenager')
else:
    print('The person is an adult')

#Write a program that prompts the user to enter a number between 1-10 and display the roman numeral version
number=int(input('Enter a number between 1-10: '))

if number==1:
    print('I')
elif number==2:
    print('II')
elif number==3:
    print('III')
elif number==4:
    print('IV')
elif number==5:
    print('V')
elif number==6:
    print('VI')
elif number==7:
    print('VII')
elif number==8:
    print('VIII')
elif number==9:
    print('IX')
elif number==10:
    print('X')
else:
 print('Error:Please Enter a number between 1-10')

#Write a program that ask the user to enter an object's mass, the calculates its weight.
#if it weight more than 500 newtons(too heavy) if less than 100 newtons(too light)
mass = float(input("Enter the object's mass: "))
weight = mass * 9.8

if weight > 500:
    print(f"Object is too heavy: {weight:.2f}")
elif weight < 100:
    print(f"Object is too light: {weight:.2f}")
else:
    print(f"The weight of the object's mass: {weight:.2f}")

#Design a program tha ask teh unser to enter month,day,year.
#Determine whether the month time the day equals the year, if so display the date is magic otherwise display a message saying the date is not magic.
month=int(input('Enter the month(numeric form): '))
day=int(input('Enter the day: '))
year=int(input('Enter the two-digit year: '))

if month * day==year:
    print("The date is magic.")
else:
    print('The date is not magic')

#Write a program that ask the user to enter the names of two primary colors to mix.
#if user enter anything but red,blue,yellow display an error message
#otherwise display the results of said colors 
primary_colors={'red','blue','yellow'}
color_combinations = {
        ("red", "blue"): "purple",
        ("blue", "red"): "purple",
        ("red", "yellow"): "orange",
        ("yellow", "red"): "orange",
        ("blue", "yellow"): "green",
        ("yellow", "blue"): "green"
    }
color1 = input('Enter the first primary color (red, blue, yellow): ')
color2 = input('Enter the second primary color (red, blue, yellow): ')

if color1 in primary_colors and color2 in primary_colors:
    results=color_combinations.get((color1,color2))
    if results:
        print(f'The result of mixing {color1} and {color2} is {results}.')
else:
    print('Error: Both inputs must be primary colors (red, blue, yellow).')

##Write me a program that calculate the number of packages of hot dogs and the numbe rof packages of hot dog buns needed for a cookout
#with the leftovers
#ask the user for ammount of people attending and how many per person
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

people = int(input('Enter the number of people attending: '))
hot_dogs_per_person = int(input('Enter the number of hot dogs per person: '))

total_hot_dogs = people * hot_dogs_per_person
total_buns = total_hot_dogs

hot_dog_packages_needed = total_hot_dogs // HOT_DOGS_PER_PACKAGE + (total_hot_dogs % HOT_DOGS_PER_PACKAGE != 0)
bun_packages_needed = total_buns // BUNS_PER_PACKAGE + (total_buns % BUNS_PER_PACKAGE != 0)

more_than_one_hot_dog_package = hot_dog_packages_needed > 1
more_than_one_bun_package = bun_packages_needed > 1

hot_dogs_leftover = (hot_dog_packages_needed * HOT_DOGS_PER_PACKAGE) - total_hot_dogs
buns_leftover = (bun_packages_needed * BUNS_PER_PACKAGE) - total_buns

if more_than_one_hot_dog_package:
    print(f"You need {hot_dog_packages_needed} packages of hot dogs.")
else:
    print(f"You need only one package of hot dogs.")

if more_than_one_bun_package:
    print(f"You need {bun_packages_needed} packages of hot dog buns.")
else:
    print(f"You need only one package of hot dog buns.")

print(f"Hot dogs left over: {hot_dogs_leftover}")
print(f"Hot dog buns left over: {buns_leftover}")

#Write a program that ask the user to enter a pocket number and displays whether the pocket is green, red or black
#The program should idisplay an error message if the user enters a number outside the range of 0-36
pocket=int(input('Enter a pocket number between 0-36: '))
if pocket ==0:
    print('Green')
elif pocket in{1,3,5,7,9}:
    print('Red')
elif pocket in{2,4,6,8,10}:
    print('Black')
elif pocket in{11,13,15,17}:
    print('Black')
elif pocket in{12,14,16,18}:
    print('Red')
elif pocket in{19,21,23,25,27}:
    print('Red')
elif pocket in{20,22,24,26,28}:
    print('Black')
elif pocket in{29,31,33,35,}:
    print('Black')
elif pocket in{30,32,34,36}:
    print('Red')
else:
    print('Error: The number is outside the range of 0 to 36.')

#Create a game where the program counts the ammount of change you have
#If you total the amount for a dollar you win anything above or below you lose
pennies_value=0.01
nickel_value=0.05
dime_value=0.10
quarter_value=0.25

print('Welcome to the change-counting game')
print('Fill out the information below')

pennies=int(input('Enter amount of pennies: '))
nickels=int(input('Enter amount of nickels: '))
dimes=int(input('Enter amount of dimes: '))
quarters=int(input('Enter amount of quarters: '))

total_value=(pennies*pennies_value +nickels*nickel_value + dimes*dime_value+ quarters*quarter_value)
dollar_value=1.00

if total_value == dollar_value:
    print("Congratulations! You've made exactly one dollar!")
elif total_value > dollar_value:
        print(f"Your total is ${total_value:.2f}. That's more than one dollar.")
else:
    print(f"Your total is ${total_value:.2f}. That's less than one dollar.")


#Write a program that ask the user to enter the number of books that he or she has purchased this month
#Then displays teh number of points arwarded.
books_purchased=int(input('Enter the amount of books purchased: '))
if books_purchased==0:
    print('You have zero points')
elif books_purchased ==2:
    print('You have 5 points')
elif books_purchased ==4:
    print('You have 15 points')
elif books_purchased ==6:
    print('You have 30 points')
elif books_purchased >8:
    print('You have 60 points')
else:
    print('Buy more books')

#Write a program that ask the user to enter the number of packages purchased.
#The ammount of discount and the total amount 
discount1 = 0.10
discount2 = 0.20
discount3 = 0.30
discount4 = 0.40

package_purchased = int(input('Enter the number of packages bought: '))
retail = 99
total_price = package_purchased * retail

if 10 <= package_purchased <= 19:
    discount = discount1
elif 20 <= package_purchased <= 49:
    discount = discount2
elif 50 <= package_purchased <= 99:
    discount = discount3
elif package_purchased >= 100:
    discount = discount4
elif package_purchased < 10:
    print("No discount available")
    discount = 0
else:
    print('Enter the correct number of packages')
    discount = 0

if discount > 0:
    after_discount = total_price * (1 - discount)
    print(f'After buying {package_purchased} packages, your total after the discount is: ${after_discount:,.2f}')
    print(f'The discount applied:{discount}')

#Write a program that ask the user to enter the weight of a package then displays the shipping charges.
Rate1=1.50
Rate2=3.00
Rate3=4.00
Rate4=4.75

weight_package=float(input("Enter the weight of the package: "))

if weight_package<=2:
    total_cost=weight_package*Rate1
    print(f'The total Cost of the package:${total_cost:.0f}')
elif 2<weight_package<=6:
    total_cost=weight_package*Rate2
    print(f'The total Cost of the package:${total_cost:.0f}')
elif 6< weight_package<=10:
     total_cost=weight_package*Rate3
     print(f'The total Cost of the package:${total_cost:.0f}')
elif weight_package>10:
     total_cost=weight_package*Rate4
     print(f'The total Cost of the package:${total_cost:.0f}')
else:
    print('Invalid weight entered.')


#Write a program that ask the user to enter a number of seconds
#If the number of seconds entered by the user is greater or equal to 60 program should convert the number of seconds to min and seconds.
#If the number of second entered is greater than or equal to 3,600 the program should convert the number of seconds to hours, minutes and seconds.
#If the number of seconds entered by the user is >= than 86,400 then it should convert the number of seoconds to days,hours,minutes,and seconds

Seconds_in_Min = 60
Seconds_in_hour = 3600
Seconds_in_day = 86400

amount_of_seconds = int(input('Enter the total amount of seconds: '))

if amount_of_seconds >= Seconds_in_day:
    total_days = amount_of_seconds // Seconds_in_day
    remaining_seconds = amount_of_seconds % Seconds_in_day
    total_hours = remaining_seconds // Seconds_in_hour
    remaining_seconds = remaining_seconds % Seconds_in_hour
    total_mins = remaining_seconds // Seconds_in_Min
    remaining_seconds = remaining_seconds % Seconds_in_Min
    print(f'{amount_of_seconds} is equivalent to {total_days} days, {total_hours} hours, {total_mins} minutes, and {remaining_seconds} seconds.')
elif amount_of_seconds >= Seconds_in_hour:
    total_hours = amount_of_seconds // Seconds_in_hour
    remaining_seconds = amount_of_seconds % Seconds_in_hour
    total_mins = remaining_seconds // Seconds_in_Min
    remaining_seconds = remaining_seconds % Seconds_in_Min
    print(f'{amount_of_seconds} is equivalent to {total_hours} hours, {total_mins} minutes, and {remaining_seconds} seconds.')
elif amount_of_seconds >= Seconds_in_Min:
    total_mins = amount_of_seconds // Seconds_in_Min
    remaining_seconds = amount_of_seconds % Seconds_in_Min
    print(f'{amount_of_seconds} is equivalent to {total_mins} minutes and {remaining_seconds} seconds.')
else:
    print(f'{amount_of_seconds} is equivalent to {amount_of_seconds} seconds.')


#write a program that ask the user to enter the year and determine if its a leap year

year = -int(input('Enter a year: '))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Create a program that leads a person through the steps of fixing a bad Wi-Fi connection.
while True:
    print('Reboot the computer and try to connect.')
    answer = input('Did that fix the problem? (yes/no): ')
    
    if answer == 'yes':
        print('Problem solved!')
        break
    
    print('Reboot the router and try to connect.')
    answer = input('Did that fix the problem? (yes/no): ')
    
    if answer == 'yes':
        print('Problem solved!')
        break

    print('Make sure the cables between the router and modem are plugged in frimly.')
    answer = input('Did that fix the problem? (yes/no): ')
    
    if answer == 'yes':
        print('Problem solved!')
        break

    print('Move the router to a new location and try to connect.')
    answer = input('Did that fix the problem? (yes/no): ')
    
    if answer == 'yes':
        print('Problem solved!')
        break

    print('Get a new router.')
    answer = input('Did that fix the problem? (yes/no): ')
    
    if answer == 'yes':
        print('Problem solved!')
        break

#Write a program that ask whether any members of your party are vegetarian,vegan,or gluten-free.
#Then displays the number of restaurants to which you may take the group

while True:
    answer1=input('Is anyone in your party a vegetarian?(yes/no): ')
    answer2=input('Is anyone in your party a vegan?(yes/no): ')
    answer3=input('Is anyone in your party gluten-free?(yes/no):')
    
    if answer1=='yes':
        if answer2=='yes':
            if answer3=='yes':
                print("Here are your restaurant choices: \n Corner Cafe-vegetarian.\n The Chef's Kitchen-Vegetarian. ")
                break

    if answer1=='no':
        if answer2=='no':
            if answer3=='no':
                print("Here are your restaurant choices: \n Joe's Gourmet Burgers-Vegetarian.")
                break
    
    if answer1=="yes":
        if answer2=='no':
            if answer3=='Yes':
                print('Here are your restaurant choices: \n Main Street Pizza Company-Vegetarian.')
                break

    if answer1=='yes':
        if answer2=='no':
            if answer3=='no':
                print("Here are your restaurant choices: \n Mama's Fine Italian-Vegetarian.")
                break

