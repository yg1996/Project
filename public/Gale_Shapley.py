
import pandas as pd
import numpy as np
from collections import Counter
from copy import copy


import csv
import random
import datetime


def add_line_to_csv(csv_file, line_data):
    # Open the CSV file in append mode and ensure it doesn't append newlines automatically
    with open(csv_file, 'a', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the line_data to the CSV file as a new row
        writer.writerow(line_data)

def generate_random_data(csv_file, num_people,sex):
    # Define the categories for the CSV data
    categories = ['name', 'sex', 'age', 'body_type', 'diet', 'drinks', 'drugs', 'height', 'pets', 'religion', 'smokes','preferred_min_age', 'preferred_max_age', 'preferred_body_type', 'preferred_diet', 'preferred_drinks', 'preferred_drugs'
    , 'preferred_height', 'preferred_pets', 'preferred_religion', 'preferred_smokes','updated_at']
    data = []
    men_names = [f"Man {i+1}" for i in range(num_people)]
    women_names = [f"Woman {i+1}" for i in range(num_people)]
    current_timestamp = datetime.datetime.now()
    # Generate data for male individuals
    if(sex=='M'):
      for i in range(num_people):
          person = {'name': men_names[i], 'sex': 'M'}
          data.append(person)
    # Generate data for female individuals
    if(sex=='F'):
      for i in range(num_people):
          person = {'name': women_names[i], 'sex': 'F'}
          data.append(person)

    # Generate random data for each person
    for person in data:
        for category in categories[2:]:
            if category == 'age':
                person[category] = random.randint(18, 35)
            elif category == 'body_type':
                person[category] = random.choice(['Slim', 'Average', 'Athletic', 'Curvy'])
            elif category == 'diet':
                person[category] = random.choice(['Vegan', 'Vegetarian', 'Omnivore'])
            elif category == 'drinks':
                person[category] = random.choice(['Never', 'Socially', 'Regularly'])
            elif category == 'drugs':
                person[category] = random.choice(['Never', 'Sometimes', 'Often'])
            elif category == 'height':
                person[category] = random.randint(150, 200)
            elif category == 'pets':
                person[category] = random.choice(['Dog', 'Cat', 'None'])
            elif category == 'religion':
                person[category] = random.choice(['Christian', 'Muslim', 'Jewish', 'Other'])
            elif category == 'smokes':
                person[category] = random.choice(['No', 'Occasionally', 'Yes'])
            elif category == 'preferred_min_age':
                person[category] = random.randint(18, 35)
            elif category == 'preferred_max_age':
                person[category] = person['preferred_min_age']+10
            elif category == 'preferred_body_type':
                person[category] = random.choice(['Slim', 'Average', 'Athletic', 'Curvy'])
            elif category == 'preferred_diet':
                person[category] = random.choice(['Vegan', 'Vegetarian', 'Omnivore'])
            elif category == 'preferred_drinks':
                person[category] = random.choice(['Never', 'Socially', 'Regularly'])
            elif category == 'preferred_drugs':
                person[category] = random.choice(['Never', 'Sometimes', 'Often'])
            elif category == 'preferred_height':
                person[category] = random.randint(150, 200)
            elif category == 'preferred_pets':
                person[category] = random.choice(['Dog', 'Cat', 'None'])
            elif category == 'preferred_religion':
                person[category] = random.choice(['Christian', 'Muslim', 'Jewish', 'Other'])
            elif category == 'preferred_smokes':
                person[category] = random.choice(['No', 'Occasionally', 'Yes'])
            person['updated_at']=current_timestamp
        # Create a list of values for the CSV row based on the person's data
        line_data = [person[category] for category in categories]
        # Add the line_data to the CSV file
        add_line_to_csv(csv_file, line_data)

import csv
import os

def read_csv_data(csv_file):
    people = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            people.append(row)
    return people

def add_lines_to_csv(file1, file2):
    with open(file2, 'r') as f2:
        lines = f2.readlines()
    with open(file1, 'a') as f1:
        f1.writelines(lines)

# Example usage
csv_file = 'public/data/people.csv'
people_data = read_csv_data(csv_file)

man_list = []
women_list = []

# Extract names from the CSV data based on the 'sex' column
for person in people_data:
    name = person['name']
    sex = person['sex']

    if sex == 'M':
        man_list.append(name)
    elif sex == 'F':
        women_list.append(name)

# Example usage - If the number of men and women is not balanced, generate random data
num_none = abs(len(man_list) - len(women_list))
if num_none > 0:
    if len(man_list) < len(women_list):
        generate_random_data('temp_people.csv', num_none, 'M')
        add_lines_to_csv(csv_file, 'temp_people.csv')
    elif len(man_list) > len(women_list):
        generate_random_data('temp_people.csv', num_none, 'F')
        add_lines_to_csv(csv_file, 'temp_people.csv')

# Re-read the updated CSV data
people_data = read_csv_data(csv_file)

man_list = []
women_list = []

# Extract names from the updated CSV data
for person in people_data:
    name = person['name']
    sex = person['sex']

    if sex == 'M':
        man_list.append(name)
    elif sex == 'F':
        women_list.append(name)

num_people = len(man_list) + len(women_list)

# Sort the lists of names
man_list = sorted(man_list)
women_list = sorted(women_list)
print("Man List:", man_list)
print("Women List:", women_list)

# Remove the temporary people CSV file
if num_none > 0:
    os.remove('temp_people.csv')

import csv
import pandas as pd
import math
import copy

def calculate_match_score(person1, person2):
    # Define the weights for each category (higher weight means higher importance)
    weights = {
        'preferred_body_type': 5,
        'preferred_diet': 5,
        'preferred_drinks': 3,
        'preferred_drugs': 3,
        'preferred_pets': 2,
        'preferred_religion': 50,
        'preferred_smokes': 5
    }
    main_category = ['body_type', 'diet', 'drinks', 'drugs', 'pets', 'religion', 'smokes']

   # Calculate the match score between two people
    score = 0
    for preferred_category, weight in weights.items():
      for category in main_category:
        if person1[preferred_category] == person2[category]:
          score += weight
    if (person1['preferred_min_age'] < person2['age']<person1['preferred_max_age']):
      score += 10
    if (person1['preferred_height'] > person2['height']):
      score += 1
    # Normalize the score based on the number of people
    #max_score = (len(weights)+2) * max(list(weights.values()))
    #normalized_score = (score / max_score) * (num_people)
    #print(math.floor(normalized_score),' ',normalized_score)
    normalized_score = score
    return normalized_score

def create_match_scores_dataframes(csv_file):
    # Read the CSV file into a list of dictionaries
    people = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            people.append(row)

    # Separate men and women into different lists
    men = []
    women = []
    for person in people:
        if person['sex'] == 'M':
            men.append(person)
        elif person['sex'] == 'F':
            women.append(person)

    # Create DataFrames for men and women
    men = sorted(men, key=lambda x: x['name'])
    women = sorted(women, key=lambda x: x['name'])

    women_data = pd.DataFrame(columns=[person['name'] for person in women])
    men_data = pd.DataFrame(columns=[person['name'] for person in men])
    women_data=women_data.reindex(sorted(women_data.columns), axis=1)
    men_data=men_data.reindex(sorted(men_data.columns), axis=1)
    # Calculate the match score between each pair of women
    for i in range(len(women)):
        for j in range(len(men)):
            person1 = women[i]
            person2 = men[j]
            match_score = calculate_match_score(person1, person2)
            women_data.at[j, person1['name']] = match_score

    # Calculate the match score between each pair of men
    for i in range(len(men)):
        for j in range(len(women)):
            person1 = men[i]
            person2 = women[j]
            match_score = calculate_match_score(person1, person2)
            men_data.at[j, person1['name']] = match_score
    # Fill diagonal elements with a default value (e.g., 0)
    women_data.fillna(1, inplace=True)
    men_data.fillna(1, inplace=True)

    return women_data, men_data

# Example usage
csv_file = 'public/data/people.csv'
women_df, men_df = create_match_scores_dataframes(csv_file)

# Sort the DataFrames by column names
women_df = women_df.sort_index(axis=1)
men_df = men_df.sort_index(axis=1)

# Rank the scores in the DataFrames

#women_df = women_df.rank(axis=0, method='min', ascending=True)
#men_df = men_df.rank(axis=0, method='min', ascending=True)

w_add_list=[]
m_add_list=[]

# Check if additional RANDOM women or men were added
for item in man_list:
    for i in range(len(man_list)):
        if f"Man {i+1}" in item:
            m_add_list.append(item)
for item in women_list:
    for i in range(len(women_list)):
        if f"Woman {i+1}" in item:
            w_add_list.append(item)

# Convert the DataFrames to integer type
women_df = women_df.astype(int)
men_df = men_df.astype(int)

# Zero socres for Random pepoles
if len(m_add_list) < len(w_add_list):
  women_df[w_add_list] = 0
  for i in range(len(w_add_list)):
    index = women_list.index(f"Woman {i+1}")
    men_df.loc[index] = 0
else:
  men_df[w_add_list] = 0
  for i in range(len(m_add_list)):
    index = man_list.index(f"Man {i+1}")
    women_df.loc[index] = 0

women_dictionary = women_df.to_dict(orient='list')
men_dictionary = men_df.to_dict(orient='list')


# Print the updated DataFrames and dictionaries
print("Women DataFrame:")
print(women_df)
print()
print("Men DataFrame:")
print(men_df)
print("Women list:")
print(women_list)
print()
print("men list:")
print(man_list)
print()

print("Women dictionary:")
print(women_dictionary)
print()
print("Men dictionary:")
print(men_dictionary)
print()

# Sort the lists of men for each woman based on the scores
w_d=copy.deepcopy(women_dictionary)
m_d=copy.deepcopy(men_dictionary)
for woman in women_dictionary:
    scores = women_dictionary[woman]
    sorted_scores = sorted(range(len(scores)), key=lambda k: (-scores[k], man_list[k]))
    sorted_men = [man_list[i] for i in sorted_scores]
    women_dictionary[woman] = sorted_men

# Display the updated dictionaries
print("Women dictionary:")
print()
print(women_dictionary)


# Repeat the same process for the men's dictionary
for man in men_dictionary:
    scores = men_dictionary[man]
    sorted_scores = sorted(range(len(scores)), key=lambda k: (-scores[k], women_list[k]))
    sorted_women = [women_list[i] for i in sorted_scores]
    men_dictionary[man] = sorted_women

# Display the updated dictionaries
print("Men dictionary:")
print()
print(men_dictionary)

from copy import copy
import json

def gale_shapley(women_dict, men_dict, women_names, men_names):
    engagements = {}
    men_preferences = men_dict.copy()
    free_men = list(men_preferences.keys())

    while free_men:
        man = free_men.pop(0)
        man_pref_list = men_preferences[man]

        if not man_pref_list:
            continue

        woman = man_pref_list.pop(0)

        if woman not in engagements:
            engagements[woman] = man
        else:
            current_man = engagements[woman]
            if women_dict[woman].index(man) < women_dict[woman].index(current_man):
                engagements[woman] = man
                if men_preferences[current_man]:
                    free_men.append(current_man)
            else:
                if man_pref_list:
                    free_men.append(man)

    return engagements

# Apply Gale-Shapley algorithm on the generated dictionaries
engagements = gale_shapley(women_dictionary, men_dictionary, women_list, man_list)

# Create a list to store the matches
matches = []

# Iterate over the engagements and append matches to the list
for woman, man in engagements.items():
    if woman not in w_add_list and man not in m_add_list:
        matches.append({
            'woman': woman,
            'man': man
        })

# # Write the matches to the JSON file
# with open('data/matches.json', 'a') as file:
#     json.dump(matches, file)

print("Engagements:")
for woman, man in engagements.items():
    if woman in w_add_list:
        print(f"Unfortunately, we did not find a match for {man}")
        continue
    if man in m_add_list:
        print(f"Unfortunately, we did not find a match for {woman}")
        continue
    print(f"{woman} is matched with {man}")

# Continue with the rest of your code...
