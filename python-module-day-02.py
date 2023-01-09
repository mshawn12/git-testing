#!/usr/bin/env python
# coding: utf-8

# # 3.2 Reading and Writing in Python - 🐍

# # Activity 01 - Student Turn - Quick Check-Up - 👩‍🎓👨‍🎓
# 
# Let’s start with a quick warm-up activity to get the Python juices flowing.
# 
# ## Instructions
# 
# Create a simple Python program below that does the following:
# 
# * Prints "Hello User!"
# 
# * Then asks "What is your name?"
# 
# * Then responds "Hello &lt;user's name&gt;"
# 
# * Then asks: "What is your favorite number? "
# 
# * Then responds: "Your favorite number is lower than mine.", "Your favorite number is higher than mine.", or "Your favorite number is the same as mine!" depending on your favorite number.
# 
# 
# ## Hint
# 
# * Remember to cast your variables!
# 
# ---

# In[8]:


# Print Hello User!
print("Hello")

# Take in User Input
user_input = input("What is your name? ")

# Respond Back with User Input
print(f"Hello {user_input}")

# Take in the User Favorite Number
user_number = int(input("Fave number? "))

# Respond Back with a statement based on your favorite number
if (user_number > 100):
    print(f"Your favorite number({user_number}) is greater than mine")
    
elif (user_number == 100):
    print("We have the same favorite number")
    
else:
    print(f"Your favorite number({user_number}) is less than mine")


# 
# <details>
#   <summary><strong>✅ Solution 01 Click HERE</strong></summary>
# 
# ```python
# # Print Hello User!
# print("Hello User!")
# 
# # Take in User Input
# name = input("What is your name? ")
# 
# # Respond Back with User Input
# print("Hi " + name + "!")
# 
# # Take in the User Favorite Number
# favorite_number = input("What is your favorite number? ")
# 
# # Respond Back with a statement based on your favorite number
# if (int(favorite_number) < 7):
#     print("Your favorite number is lower than mine.")
# 
# elif (int(favorite_number) == 7):
#     print("Your favorite number is the same as mine!")
# 
# else:
#     print("Your favorite number is higher than mine.")
# ```
# 
# 
# </details>
# 
# 
# 
# 

# # Activity 02 - Instructor Turn - Simple Loops - 👩‍🏫🧑‍🏫

# In[9]:


# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)


# In[10]:


# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)


# In[11]:


# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
for word in words:
    print(word)


# In[92]:


# A While Loop will continue to loop through the code contained within it until some condition is met
x = "yes"
while x.lower() == "yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")
   


# ---

# # Activity 03 - Student Turn - Kid in a Candy Store - 👩‍🎓👨‍🎓 
# 
# In this activity, you will create the code that a candy store will use in their state-of-the-art candy vending machine.
# 
# ## Instructions
# 
# * Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.
# 
#   * For example: `"[0] Snickers"`
# 
# * Create a second loop that runs for a set number of times determined by the variable `allowance`.
# 
#   * For example: If allowance is equal to five, the loop should run five times.
# 
#   * Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable `candy_cart`.
# 
#   * For example: If the user enters "0" as their input, "Snickers" should be added into the `candy_cart` list.
# 
# * Use another loop to print all of the candies selected to the terminal.
# 
# ## Bonus
# 
# Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.
# 
# ---

# In[95]:


# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for index, candy in enumerate(candy_list):
    print(f"[{index}] {candy}")

    
# CODE HERE
for x in range(allowance):
    user_input = int(input("Selected item: "))
    print(f"{candy_list[user_input]}")
    print("")
    print("---------")

    candy_cart.append(candy_list[user_input])

#allowance = allowance - 1
print("Shopping cart:")
for candy in candy_cart:
    
    print(candy)
    
    


# #### Bonus 
# # CODE HERE

# In[63]:


# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for index, candy in enumerate(candy_list):
    print(f"[{index}] {candy}")

    
# CODE HERE

continue_shopping = "yes"

while continue_shopping == "yes":
    user_input = int(input("Select an item: "))
    print(f"{candy_list[user_input]}")
    print("")
    print("---------")

    candy_cart.append(candy_list[user_input])
    continue_shopping = input("Do you want to continue shopping? ").lower()

print("Shopping cart:")
for candy in candy_cart:
    
    print(candy)


# In[ ]:





# In[ ]:





# 
# <details>
#   <summary><strong>✅ Solution 03 Click HERE</strong></summary>
# 
# ```python
# # The list of candies to print to the screen
# candy_list = [
#     "Snickers",
#     "Kit Kat",
#     "Sour Patch Kids",
#     "Juicy Fruit",
#     "Swedish Fish",
#     "Skittles",
#     "Hershey Bar",
#     "Starbursts",
#     "M&Ms"
# ]
# 
# # The amount of candy the user will be allowed to choose
# allowance = 5
# 
# # The list used to store all of the candies selected inside of
# candy_cart = []
# 
# # Print all of the candies to the screen and their index in brackets
# for candy in candy_list:
#     print(f'[{str(candy_list.index(candy))}] {candy}')
# 
# # Another option to run the for loop involves Python's enumerate method
# # This method obtains both the index and the value of an item during a for loop
# # for index, candy in candy_list:
# #     print(index, candy)
# 
# # Run through a loop which allows the user to choose which candies to take home with them
# print("Which candy would you like to bring home?")
# for x in range(allowance):
#     selected = input("Input the number of the candy you want: ")
# 
#     # Add the candy at the index chosen to the candy_cart list
#     candy_cart.append(candy_list[int(selected)])
# 
# # Loop through the candy_cart to say what candies were brought home
# print("I brought home with me...")
# for candy in candy_cart:
#     print(candy)
# 
# ```
# 
# 
# </details>

# 
# <details>
#   <summary><strong>✅ Solution 03 Bonus Click HERE</strong></summary>
# 
# ```python
# # The list of candies to print to the screen
# candy_list = [
#     "Snickers",
#     "Kit Kat",
#     "Sour Patch Kids",
#     "Juicy Fruit",
#     "Swedish Fish",
#     "Skittles",
#     "Hershey Bar",
#     "Starbursts",
#     "M&Ms"
# ]
# 
# # The amount of candy the user will be allowed to choose
# allowance = 5
# 
# # The list used to store all of the candies selected inside of
# candy_cart = []
# 
# # Print all of the candies to the screen and their index in brackets
# for i in range(len(candy_list)):
#     print("[" + str(i) + "] " + candy_list[i])
# 
# 
# # Set answer to "yes" for while loop
# answer = "yes"
# 
# 
# while answer == "yes":
# 
#     # Ask which candy the user would like to bring ho
#     print("Which candy would you like to bring home?")
#     selected = input("Input the number of the candy you want: ")
# 
#     # Add the candy at the index chosen to the candy_cart list
#     candy_cart.append(candy_list[int(selected)])
# 
#     # ask the user if they want more candy
#     answer = input("Would you like to make another selection? ('yes' or 'no') ")
# 
# 
# # Loop through the candy_cart to say what candies were brought home
# print("I brought home with me...")
# for candy in candy_cart:
#     print(candy)
# 
# ```
# 
# 
# </details>

# # Activity 04 - Student Turn - House of Pies - 👩‍🎓👨‍🎓  
# 
# In this activity, you will build an order form that displays a list of pies and then prompts users to make a selection. The form will continue to prompt for selections until the user decides to end the process.
# 
# ## Instructions
# 
# * Create an order form that displays a list of pies to the user in the following way:
# 
# 
# ```
# Welcome to the House of Pies! Here are our pies:
# 
# ---------------------------------------------------------------------
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
# ```
# 
# * Then, prompt the user to enter the number for the pie they would like to order.
# 
# * Immediately follow up their order with `Great! We'll have that <PIE NAME> right out for you`, and then ask if they would like to make another order. If so, repeat the process.
# 
# * Once the user is done purchasing pies, print the total number of pies ordered.
# 
# ## Bonus
# 
# * Modify the application so that at the conclusion of the transaction, the user's purchases are listed out, with the total pie count broken by _each_ pie. For example:
# 
# ```
# You purchased:
# 0 Pecan
# 0 Apple Crisp
# 0 Bean
# 2 Banoffee
# 0 Black Bun
# 0 Blueberry
# 0 Buko
# 0 Burek
# 0 Tamale
# 1 Steak
# ```
# 
# ---
# 

# In[98]:


# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")
print("-------------------")

# While we are still shopping...

while shopping == "y":

    # Show pie selection prompt
    for index, pie in enumerate(pie_list):
        print(f"({index+1}) {pie}")
        

    # Add pie to the pie list
    selected = int(input("Please add a pie to the list using the menu number: "))
    pie_purchases.append(pie_list[selected - 1])

   
    # Inform the customer of the pie purchase
    print(f"You selected {pie_list[selected - 1]}. We'll have that right out for you")
    print()

    # Provide exit option
    shopping = input("Do you want to contiue shopping? ").lower()

# Once the pie list is complete
print()
print("Shopping Cart:")
print(f"You ordered {len(pie_purchases)} pie(s)")
print(pie_purchases)


# 
# <details>
#   <summary><strong>✅ Solution 04 Click HERE</strong></summary>
#     
# ```python
# # Initial variable to track shopping status
# shopping = 'y'
# 
# # List to track pie purchases
# pie_purchases = []
# 
# # Pie List
# pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
#             "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
# 
# # Display initial message
# print("Welcome to the House of Pies! Here are our pies:")
# 
# # While we are still shopping...
# while shopping == "y":
# 
#     # Show pie selection prompt
#     print("---------------------------------------------------------------------")
#     print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
#           " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
#           " (9) Tamale, (10) Steak ")
# 
#     pie_choice = input("Which would you like? ")
# 
#     # Add pie to the pie list
#     pie_purchases.append(pie_choice)
# 
#     print("------------------------------------------------------------------------")
# 
#     # Inform the customer of the pie purchase
#     print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")
# 
#     # Provide exit option
#     shopping = input("Would you like to make another purchase: (y)es or (n)o? ")
# 
# # Once the pie list is complete
# print("------------------------------------------------------------------------")
# print("You purchased a total of " + str(len(pie_purchases)) + ".")
# ```
# </detail>
# 

# <details>
#   <summary><strong>✅ Solution 04 Bonus Click HERE</strong></summary>
# 
# ```python
# # Initial variable to track shopping status
# shopping = 'y'
# 
# # List to track pie purchases
# pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 
# # Pie List
# pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
#             "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
# 
# # Display initial message
# print("Welcome to the House of Pies! Here are our pies:")
# 
# # While we are still shopping...
# while shopping == "y":
# 
#     # Show pie selection prompt
#     print("---------------------------------------------------------------------")
#     print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
#           " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
#           " (9) Tamale, (10) Steak ")
# 
#     pie_choice = input("Which would you like? ")
# 
#     # Get index of the pie from the selected number
#     choice_index = int(pie_choice) - 1
# 
#     # Add pie to the pie list by finding the matching index and adding one to its value
#     pie_purchases[choice_index] += 1
# 
#     print("------------------------------------------------------------------------")
# 
#     # Inform the customer of the pie purchase
#     print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")
# 
#     # Provide exit option
#     shopping = input("Would you like to make another purchase: (y)es or (n)o? ")
# 
# # Once the pie list is complete
# print("------------------------------------------------------------------------")
# 
# # Count instances of each pie
# print("You purchased: ")
# 
# # Loop through the full pie list
# for pie_index in range(len(pie_list)):
#     pie_count = str(pie_purchases[pie_index])
#     pie_name = str(pie_list[pie_index])
# 
#     # Gather the count of each pie in the pie list and print them alongside the pies
#     print(pie_count + " " + pie_name)
# ```
# </detail>

# # Activity 05 - Instructor Turn - Basic Read - 👩‍🏫🧑‍🏫

# In[73]:


# Store the file path associated with the file (note the backslash may be OS specific)
file = './Resources/input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


# # Activity 06 - Instructor Turn - Module - 👩‍🏫🧑‍🏫

# In[74]:


# Import the random and string Module
import random
import string

# Utilize the string module's custom method: ".ascii_letters"
print(string.ascii_letters)

# Utilize the random module's custom method randint
for x in range(10):
    print(random.randint(1, 10))


# # Activity 07 - Student Turn - Module Playground - 👩‍🎓👨‍🎓
# 
# In this activity, you will have the opportunity to explore and play around with some Python modules.
# 
# ## Instructions
# 
# There are tons of built-in modules for Python. Review some of Python's modules and play around with them. Use the following link:
# 
# 👉 [List of Built-In Python Modules](https://docs.python.org/3/py-modindex.html)
# 
# ---

# # Activity 08 - Instructor Turn - Read CSV - 👩‍🏫🧑‍🏫

# In[76]:


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


# In[77]:


csvpath = os.path.join('.', 'Resources', 'contacts.csv')

# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))



# In[100]:


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        print(row[0])


# In[ ]:





# # Activity 09 - Student Turn - Reading Comic Book Data - 👩‍🎓👨‍🎓
# 
# 
# In this activity, you will create an application that searches the provided CSV file for a specific graphic novel title and then returns the title, publisher’s name, and the year it was published.
# 
# ## Instructions
# 
# * Prompt the user for the book title they’d like to search.
# 
# * Search through the `comic_books.csv` to find the user's book.
# 
# * If the CSV contains the user's title, then print out the title, the publisher name, and the year it was published.
# 
#   * For example: `"Alien was published by DC Comics in 2015"`.
# 
# * If the CSV does not contain the user's title, then print out a message telling them that their book could not be found.
# 
#     * Set a variable to `False` to check if we found the comic book.
# 
#     * In the `for` loop, change the variable to confirm that the comic book is found.
# 
# ## References
# 
# Data modified from "Comic books CSV" Updated April 2021. Initially released in 2014 to accompany the British Library's exhibition Comics Unmasked. [https://www.bl.uk/collection-metadata/downloads](https://www.bl.uk/collection-metadata/downloads)
# 
# ---

# In[108]:


# Modules
import os
import csv

# Prompt user for title lookup
book = input("What title are you looking for? ")

# Set path for file
csvpath = os.path.join(".", "Resources", "comic_books.csv")
print(csvpath)

# Set variable to check if we found the video
found = False

# Open the CSV
with open (csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)
    
    # Loop through looking for the video
    #.. Added the lower() function -----------------
    for row in csvreader:
        if(row[0].lower() == book.lower()):
            print(f"{row[0]} was published by {row[8]} in {row[9]}")
            
            found = True
                
    if found == False:
        print("Error")
            # Set variable to confirm we have found the video



    # If the book is never found, alert the user


# <details>
#   <summary><strong>✅ Solution 09 Click HERE</strong></summary>
#     
# ```python
# # Modules
# import os
# import csv
# 
# # Prompt user for title lookup
# book = input("What title are you looking for? ")
# 
# # Set path for file
# csvpath = os.path.join(".", "Resources", "comic_books.csv")
# 
# # Set variable to check if we found the video
# found = False
# 
# # Open the CSV
# with open(csvpath, encoding='utf') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
# 
#     # Loop through looking for the video
#     for row in csvreader:
#         # print(row)
#         if row[0] == book:
#             print(row[0] + " was published by " + row[8] + " in " + row[9])
# 
#             # Set variable to confirm we have found the video
#             found = True
# 
# 
#     # If the book is never found, alert the user
#     if found is False:
#         print("Sorry about this, we don't seem to have what you are looking for!")     
# ```
# </details>

# --- 

# # Activity 10 - Instructor Turn - Write File - 👩‍🏫🧑‍🏫

# In[ ]:


# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join(".", "output", "new.csv")


# In[ ]:


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


# # Activity 11 - Instructor Turn - Zip - 👩‍🏫🧑‍🏫

# In[ ]:


import csv
import os

# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]


# In[ ]:


# Zip all three lists together into tuples
roster = zip(indexes, employees, department)
print(roster)

# Print the contents of each row
for employee in roster:
    print(employee)

# save the output file path
output_file = os.path.join("./output/activity-11-output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerows(roster)


# In[ ]:


# Zip all three lists together into tuples
# NOTE WHEN ZIPPING data it will only store once 
# SO BELOW THIS COMMENT
# IS WHY WE DECLARE the variable called roster again 
# in order to print and view

roster = zip(indexes, employees, department)
# to print out to terminal:
#comment out above code and run the code below
for employee in roster:
    print(employee)


# # Activity 12 - Student Turn - U.S. Census Breakdown - 👩‍🎓👨‍🎓
# 
# In this activity, you will be provided with a large dataset from the 2019 U.S. Census. Your task is to clean up this dataset and create a new CSV file that is easier to comprehend.
# 
# ## Instructions
# 
# * Create a Python application that reads in the data from the 2019 U.S. Census.
# 
# * Then, store the contents of `Place`, `Population`, `Per Capita Income`, and `Poverty Count` into Python Lists.
# 
# * Then, zip these lists together into a single tuple.
# 
# * Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your CSV.
# 
# ## Bonus
# 
# * Find the poverty rate (percentage of population living in poverty). Include this in your final output, converting the rate to a string and including a "%" at the end of the string.
# 
# * Parse the string associated with `Place`, separating it into `County` and `State`, so we can store both in separate columns.
# 
# ## Hints
# 
# * Windows users may get a `UnicodeDecodeError`. To avoid this, pass in `encoding="utf8"` as an additional parameter when reading in the file.
# 
# * As with many datasets, the file does not include the header line. Use the following list as a guide to the columns: "Place,Population,Median Age,Household Income,Per Capita Income,Employed Civilians,Unemployed Civilians,People in the Military,Poverty Count"
# 
# ## References
# 
# Data Source: [U.S. Census API - ACS 5-Year Estimates 2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)
# 
# ---

# In[113]:


import os
import csv

census_csv = os.path.join(".", "Resources", "census_starter.csv")

# Lists to store data
place = []
population = []
income = []
poverty_count = []
poverty_rate = []
county = []
state = []


# In[117]:


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(census_csv) as csvfile:
        
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        # Add place
        place.append(row[0])
        
        # Add population
        population.append(row[1])


        # Add per capita income
        income.append(row[4])


        # Add poverty count
        poverty_count.append(row[8])

        # Determine poverty rate to 2 decimal places, convert to string
        percent = round(int(row[8]) / int(row[1]) * 100,2)
        poverty_rate.append(f"{percent}%")
        
        # Split the place into county and state
        split_place = row[0].split(",")
        county.append(split_place[0])
        state.append(split_place[1])

# Zip lists together
cleaned_csv = zip(place, population, income, poverty_count, poverty_rate, county, state)

# Set variable for output file
output_file = os.path.join("./output/census_final.csv")


#  Open the output file
with open(output_file,"w") as datafile:

    # Write the header row
    writer = csv.writer(datafile)
    writer.writerow(["Place","Population","Income","Poverty Count", "Poverty Rate", "County", "State"])
    # Write in zipped rows
    writer.writerows(cleaned_csv)
    
print("File created")
    


# In[ ]:





# In[ ]:





# In[ ]:





# 
# <details>
#   <summary><strong>✅ Solution 12 Click HERE</strong></summary>
#     
# ```python
# import os
# import csv
# 
# census_csv = os.path.join(".", "Resources", "census_starter.csv")
# 
# # Lists to store data
# place = []
# population = []
# income = []
# poverty_count = []
# poverty_rate = []
# county = []
# state = []
# 
# # with open(udemy_csv, encoding='utf-8') as csvfile:
# with open(census_csv) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     for row in csvreader:
#         # Add place
#         place.append(row[0])
# 
#         # Add population
#         population.append(row[1])
# 
#         # Add per capita income
#         income.append(row[4])
# 
#         # Add poverty count
#         poverty_count.append(row[8])
# 
#         # Determine poverty rate to 2 decimal places, convert to string
#         percent = round(int(row[8]) / int(row[1]) * 100, 2)
#         poverty_rate.append(str(percent) + "%")
# 
#         # Split the place into county and state
#         split_place = row[0].split(", ")
#         county.append(split_place[0])
#         state.append(split_place[1])
# 
# # Zip lists together
# cleaned_csv = zip(place, population, income, poverty_count, poverty_rate, county, state)
# 
# # Set variable for output file
# output_file = os.path.join("./output/census_final.csv")
# 
# #  Open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)
# 
#     # Write the header row
#     writer.writerow(["Place", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate",
#                     "County", "State"])
# 
#     # Write in zipped rows
#     writer.writerows(cleaned_csv)
# ```
# </details>

# # Activity 13 - Instructor Turn - Functions - 👩‍🏫🧑‍🏫

# In[ ]:


# Define the function and tell it to print "Hello!" when called
def print_hello():
    print(f"Hello!")


# Call the function within the application to ensure the code is run
print_hello()
# -------------#


# In[121]:


# Functions that take in and use parameters can also be defined
def print_name(name):
    #print("Hello " + name + "!")
    print(f"Hello {name}")


# When calling a function with a parameter, a parameter must be passed into the function
print_name("Bob Smith")
# -------------#


#MY test
print_name(input("Enter name: "))


# In[ ]:


# The prime use case for functions is in being able to run the same code for different values
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_two = [11, 12, 13, 14, 15]
testMY = "Mickey"

# TEST MY
# list_information(list_one)
# list_information(list_two)

def list_information(simple_list):
    print(f"The values within the list are...")
    for value in simple_list:
        print(value)
    print("The length of this list is... " + str(len(simple_list)))


list_information(list_one)
list_information(list_two)

#MY test
list_information(testMY)
list_information(input("Enter name: "))


# In[ ]:




