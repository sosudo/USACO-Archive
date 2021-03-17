record = input() # Take in the input as a string.
record_list = [i for i in record]  # Use a list comprehension to map record into a list.
A, B, win_by_two, winner = 0, 0, False, None # A and B have scores of 0, the Win by Two rule hasn't been invoked, and a winner has not been declared.
while winner == None: # While a winner has not been declared.
  if len(record_list) == 0: # To avoid a ListIndex error, we can check if the list has 0 elements. If it does, then we can compare the scores of A and B and check to see which one has the higher score. The one with the higher score is the winner.
    winner = 'A' if A > B else 'B'
    break # Break away from the while loop.
  scorer = record_list[0] # Check who just scored.
  points = int(record_list[1]) # Check how many points the scorer scored.
  record_list = record_list[2:] # Remove the first 2 elements so that the scorer and points we just found aren't reused.
  if scorer == 'A': # If the scorer is A, increment A's score by how many points they score.
    A += points
  else: # If the scorer isn't A, it must be B. Increment B's score by how many points they score.
    B += points
  if A == 10 and B == 10: # Both A and B must be tied 10-10 in order for the Win by Two rule to be invoked. This will check if both A and B have scores of 10, and set win_by_two to True if they're tied 10-10.
    win_by_two = True
  if win_by_two == True: # If the Win by Two rule is invoked, the winner must have a score 2 or more higher than the loser. This block will check to see if A is greater than B + 2 and set A to the winner if it's true, if B is greater than A + 2 and set B to the winner, or just continue to the next iteration of the while loop because there is no winner.
    if A >= B + 2:
      winner = 'A'
      break # Break away from the while loop.
    if B >= A + 2:
      winner = 'B'
      break # Break away from the while loop.
    else:
      continue
  if win_by_two == False: # If the Win by Two rule is not invoked, the winning requirement is that either A or B must have a score of 11. 
    if A == 11: # Set the winner to A if A has a score of 11.
      winner = 'A'
      break # Break away from the while loop.
    elif B == 11: # Set the winner to B if B has a score of 11.
      winner = 'B'
      break # Break away from the while loop.
    else:
      continue # Continue to the next iteration of the while loop if there is no winner.
print(winner) # Print the winner
