# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

x=int(input('Enter a integer less than 10:'))


for i in people:
    if x <=10:
      print(people[0:x])
      break
else:
   print("Please enter a number that less than 10, try again")


    