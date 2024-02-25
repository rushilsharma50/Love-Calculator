import random

# lower is use for lower casing the name
# strip is use for removing the unnecessary space
first_name = input("enter your name: ").lower().strip()
second_name = input("enter your crush name: ").lower().strip()

letters = "abcdefghijklmnopqrstuvwxyz"
love_score = 0

for letter in letters:
  # This line calculates the minimum number of times a specific letter appears in both names.
  min_count = min(first_name.count(letter), second_name.count(letter))
  love_score += min_count * random.uniform(0.9, 7.1)

# This calculates the compatibility percentage by dividing the score
# by the total number of letters in both names and multiplying by 100.
percentage = love_score / len(first_name + second_name) * 100
love_percentage = round(percentage, 2)
print(f"{first_name} and {second_name} love percentage is {love_percentage}%")

# Determine the message based on the love percentage.
if love_percentage < 25:
  print("Just give up, there is nothing can you do.\U0001F605")
elif love_percentage < 50:
  print("Welcome to the friendzone\U0001F923")
elif love_percentage < 75:
  print("Make a move dammit!\U0001F621")
elif love_percentage < 100:
  print("Just propose that person\U0001F60D")
elif love_percentage == 100:
  print("Congatulations! You parents can have granchild now!\u263A")
else:
  print("how can that be possible in todays generation?\U0001f613")
print("---------------------------------------------------------------------")
print(
    "Remember:-Love is complex and cant be accurately calculated by a program.\U0001F600"
)