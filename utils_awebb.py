
# Online Python - IDE, Editor, Compiler, Interpreter

''' ITERATION 5
Module: Webb Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. .
A good byline could be used in every Python analytics project we do.
'''

import statistics

has_black_cat: bool = True
number_of_black_cats: int = 1
cat_skills_offered: list = ["Mouse Catching", "Machine Learning", "Making A Mess"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
has_dog: bool = True
number_of_dogs = int=2
dog_skills_offered: list = ["Barking", "Walking", "Chewing Shoes"]
dog_skill_test_scores: list = [5.8, 5.6, 5.9, 6.0, 5.7]

# Calculate basic stats for client satisfaction scores
min_client_score: float = min(client_satisfaction_scores)
max_client_score: float = max(client_satisfaction_scores)
mean_client_score: float = statistics.mean(client_satisfaction_scores)
stdev_client_score: float = statistics.stdev(client_satisfaction_scores)

# Calculate basic stats for dog skill test scores
min_dog_score: float = min(dog_skill_test_scores)
max_dog_score: float = max(dog_skill_test_scores)
mean_dog_score: float = statistics.mean(dog_skill_test_scores)
stdev_dog_score: float = statistics.stdev(dog_skill_test_scores)

byline: str = f"""
-------------------------------------------------
Webb Analytics: Analytics for the Web, by Webb
-------------------------------------------------
Has Black Cat: {has_black_cat}
Number of Black Cats: {number_of_black_cats}
Cat Skills Offered: {cat_skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_client_score}
Maximum Satisfaction Score: {max_client_score}
Mean Satisfaction Score: {mean_client_score}
Standard Deviation of Satisfaction Score: {stdev_client_score}
Has Dog: {has_dog}
Number of Dogs: {number_of_dogs}
Dog Skills Offered: {dog_skills_offered}
Dog Skills Test Score: {dog_skill_test_scores}
Minimum of Dog Skills Test Score: {min_dog_score}
Maximum of Dog Skills Test Score: {max_dog_score}
Mean of Dog Skills Test Score: {mean_dog_score}
Standard Deviation of Dog Skills Test Score: {stdev_dog_score}
"""

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

if __name__ == '__main__':
    main()
