# Randomly choose to people from data
from game_data import data
from random import randint
import art

print("Run code!!!!!!!!!!!!!!!!!!!!!")


def number_generator():
  """generates a random number from 0 to the highest number in the data array."""
  return randint(0, 24)


# Ensure people are different
def compare_people(person):
  """compares the first person to random second perosn and ensures they are different."""
  second_option = data[number_generator()]
  while person['name'] == second_option['name']:
    second_option = data[number_generator()]
  return second_option


# Compare follower function
def compare_follower(person1, person2):
  """Checks who has the highest follower count."""
  if person1['follower_count'] == person2['follower_count']:
    return "tie",
  elif person1['follower_count'] > person2['follower_count']:
    return person1
  else:
    return person2
  
def format_data(account):
  """Format the account data into printable format."""
  return  f"Compare A: {account['name']}, {account['description']}, from {account['country']}"



def higher_lower():
  """Start the game to guess which of the two peple have the most instagram followers"""
  first_person = data[number_generator()]
  second_person = compare_people(first_person)
  final_score = 0

  print(art.logo)

  # Print description, excluding follower count
  print(f"Compare A: {format_data(first_person)}")
  print(art.vs)
  print(f"Against B: {format_data(second_person)}")

  answer = compare_follower(first_person, second_person)

  # Have user guess which one has more followers
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  if guess == 'A':
    guess = first_person
  else:
    guess = second_person


  # If right or follower count is the same go again.
  while guess == answer or answer == "tie":
    print(art.logo)
    final_score += 1
    if answer == "tie":
      print(f"They both have the same number of followers. Current score: {final_score}") 
    else:
      print(f"You're right! Current score: {final_score}")
    first_person = answer
    second_person = compare_people(first_person)
    print(f"Compare A: {format_data(first_person)}")
    print(art.vs)
    print(f"Against B: {format_data(second_person)}")

    answer = compare_follower(first_person, second_person)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == 'A':
      guess = first_person
    else:
      guess = second_person

  # If guess is wrong, end loop
  print(f"Sorry, that's wrong. Final score: {final_score}")


# Start game
higher_lower()

# Option to start the game again
while input("Do you want to play again? Type 'Y' or 'N': ").lower() == 'y':
  print('\n' * 10)
  higher_lower()