points = 190
prize = None

if points <= 50:
  prize = "wooden rabbit!"
elif 151 <= points <= 180:
  prize = "wafer-thin mint!"
elif points >= 181:
  prize = "penguin!"
# else:
#   result = "Oh dear, no prize this time."

if prize:
  result = "Congratulations! You won a {}!".format(prize)
else:
  result = "Oh dear, no prize this time."

print(result)