record = input()
record_list = [i for i in record]
A, B, win_by_two, winner = 0, 0, False, None
while winner == None:
  scorer = record_list[0]
  record_list.pop(0)
  points = int(record_list[0])
  record_list.pop(0)
  if scorer == 'A':
    A += points
  else:
    B += points
  if A == 10 and B == 10:
    win_by_two = True
  if win_by_two == True:
    if A >= B + 2:
      winner = 'A'
      break
    if B >= A + 2:
      winner = 'B'
      break
    else:
      continue
  if win_by_two == False:
    if A == 11:
      winner = 'A'
    elif B == 11:
      winner = 'B'
    else:
      continue
print(winner)
