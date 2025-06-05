# Randomly choose to people from data
from game_data import data
from random import randint
import art

print("Run code!!!!!!!!!!!!!!!!!!!!!")


def number_generator():
  """generates a random number from 0 to the highest number in the data array"""
  return randint(0, 24)


# Ensure people are different
def compare_people(person):
  """compares the first person to random second perosn and ensures they are different"""
  second_option = data[number_generator()]
  while person['name'] == second_option['name']:
    second_option = data[number_generator()]
  return second_option


# Compare follower function
def compare_follower(person1, person2):
  """Checks who has the highest follower count"""
  if person1['follower_count'] == person2['follower_count']:
    return "tie",
  elif person1['follower_count'] > person2['follower_count']:
    return person1
  else:
    return person2


def higher_lower():
  first_person = data[number_generator()]
  second_person = compare_people(first_person)
  final_score = 0

  print(art.logo)

  # Print description, excluding follower count
  print(f"Compare A: {first_person['name']}, {first_person['description']}, from {first_person['country']}")
  print(art.vs)
  print(f"Agains B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")

  answer = compare_follower(first_person, second_person)

  # Have user guess which one has more followers
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  if guess == 'A':
    guess = first_person
  else:
    guess = second_person


  # If right go again and if wrong end game
  while guess == answer:
    final_score += 1
    print(art.logo)
    print(f"You're right! Current score: {final_score}")
    first_person = answer
    second_person = compare_people(first_person)
    print(f"Compare A: {first_person['name']}, {first_person['description']}, from {first_person['country']}")
    print(art.vs)
    print(f"Against B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")

    answer = compare_follower(first_person, second_person)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == 'A':
      guess = first_person
    else:
      guess = second_person

  print(f"Sorry, that's wrong. Final score: {final_score}")

higher_lower()

while input("Do you want to play again? Type 'Y' or 'N': ").lower() == 'y':
  print('\n' * 10)
  higher_lower()