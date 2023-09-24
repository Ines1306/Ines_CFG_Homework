# How to use the Harry Potter API:
# First I used the console to pip install requests, then I imported requests and used the URL that has all data
# regarding the HP characters
import requests
response = requests.get("https://hp-api.onrender.com/api/characters")
# print(response.status_code) # To make sure we get 200 for successful
data = response.json()
# print(data)

print("Welcome to the Harry Potter Quiz that will test what percentage of fan you are!\nThere are 5 questions and for "
      "each correct answer you earn 10 points.\nLet's see what you've got!")

list_characters = []
i = 0
for character in data:
    if i == 20: # Because we just want the first 20 characters of the API
        break
    list_characters.append(character['name'])
    i = i + 1

print(f"First, here is the list of all characters that you may be asked about:{list_characters}")

answer_user=[]
answer_correct=[]

#Question 1

answer_user1 = input("\nQuestion 1: To which house did Cho Chang belong to?").capitalize()
answer_user.append(answer_user1)

for character1 in data:
    if character1['name'] == 'Cho Chang':
        answer_correct1 = character1['house']
        answer_correct.append(answer_correct1)

print(f"The answer is {answer_correct1}\n")

#Question 2

answer_user2 = input("Question 2: In which day was Harry Potter born? Write your answer in the format DD-MM-YYYY.")
answer_user.append(answer_user2)

# We need to import the datetime module to calculate today's date and turn the user's answer into a date
# In order to do this we need to import datetime from datetime as seen bellow
from datetime import datetime

answer_correct2 = data[0]['dateOfBirth']
answer_correct.append(answer_correct2)

def days_passed():
    answer2_datetime = datetime.strptime(answer_correct[1],"%d-%m-%Y") #transform correct answer into a date
    today = datetime.today()
    difference_days = today-answer2_datetime #the result is 15755 days, 22:19:31.270663 on 19/09
    final_difference_days = (str(difference_days))[:5] #by using string slicing the result is 15755 on 19/09
    return final_difference_days

print(f"Harry Potter was born on the 31st of July of 1980. Around {days_passed()} days have passed!\n")

#Question 3

answer_user3_temp = input('Question 3: Is it true that Harry Potter was known as "The Boy Who Lived"? Answer '
                          'with True or False.').capitalize()

if answer_user3_temp == "True":
    answer_user3 = True
elif answer_user3_temp == "False":
    answer_user3 = False
else:
    answer_user3 = answer_user3_temp

answer_user.append(answer_user3)
answer_correct3 = True
answer_correct.append(answer_correct3)

print(f"The answer is True. Harry was known as {data[0]['alternate_names'][0]} and {data[0]['alternate_names'][1]}.")


#Question4

answer_user4 = input("\nQuestion4: What species could Professor Remus Lupin turn into?").lower()
answer_user.append(answer_user4)

for character4 in data:
    if character4['name'] == 'Remus Lupin':
        answer_correct4 = character4['species']
        answer_correct.append(answer_correct4)

print(f"Professor Lupin was a {answer_correct4} and in fact his patronus was also a wolf!")

#Question5

answer_user5 = input("\nQuestion5: The pink Professor Dolores Umbridge had a cat for a patronus, which breed?").lower()
answer_user.append(answer_user5)

answer_correct5_total = data[19]['patronus']
answer_correct5 = answer_correct5_total.split(" ")[0] # Since we only want the first word of the resulting list
answer_correct.append(answer_correct5)

print(f"It was a {answer_correct5} cat!")

# Creating a dictionary of characters and respective patronus:
list_characters_new = list_characters[:5]
list_patronus = [data[0]['patronus'], data[1]['patronus'], data[2]['patronus'], data[3]['patronus'],
                 data[4]['patronus']]
adict={}

for index in range(len(list_characters_new)):
    adict[list_characters_new[index]] = list_patronus[index]
# print(adict) # Just to make sure that the dictionary was well created

print(f"Other characters' patronus are: {adict}")

# Let's put the questions and answers in a CSV file
question1 = 'Question 1: To which house did Cho Chang belong to?'
question2 = 'Question 2: In which day was Harry Potter born? Write your answer in the format DD-MM-YYYY.'
question3 = 'Question 3: Is it true that Harry Potter was known as "The Boy Who Lived"? Answer with True or False.'
question4 = 'Question4: What species could Professor Remus Lupin turn into?'
question5 = 'Question5: The pink Professor Dolores Umbridge had a cat for a patronus, which breed?'

import csv
header = ['Question','Answer']
data = [
    {'Question': question1, 'Answer': answer_correct1},
    {'Question': question2, 'Answer': answer_correct2},
    {'Question': question3, 'Answer': answer_correct3},
    {'Question': question4, 'Answer': answer_correct4},
    {'Question': question5, 'Answer': answer_correct5}
]

with open('HPQuiz.csv','w') as csv_file:
    file = csv.DictWriter(csv_file, fieldnames=header)
    file.writeheader()
    file.writerows(data)

# with open('HPQuiz.csv','r') as file2: # Just to be sure that everything is correct
#     file3 = csv.DictReader(file2)
#     for row in file3:
#         print(row)


# Let's calculate the Final Score

# print(answer_correct) # just to check if the list is being filled
# print(answer_user) # just to check if the list is being filled
final_score=0

for i in range(len(answer_correct)):
    if answer_correct[i] == answer_user[i]:
        final_score += 10

print(f"\nYour final score is {final_score}/50. No matter what your score is, congrats on being a Harry Potter fan!")
