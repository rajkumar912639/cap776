# A variable to store the height of the triangle
height = 5
# A loop to iterate over the rows
for i in range(1, height + 1):
  # A loop to iterate over the columns
  for j in range(1, i + 1):
    # Print an asterisk without a newline
    print("*", end="")
  # Print a newline after each row
  print()
