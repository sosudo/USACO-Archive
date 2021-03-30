# We use sys to reassign our input and output
import sys
# Reassign standard input and output by opening the necessary files and setting them
# to the values of sys.stdin and sys.stdout
sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')
# Taking in the input lines as strings
line_one = input()
line_two = input()
# Use list comprehensions to map the values of a, b, c, and d as integer values
a, b = [int(i) for i in line_one.split(" ")]
c, d = [int(i) for i in line_two.split(" ")]
# Each ordering of a, b, c, and d can simply be hardcoded since each one has a specific
# output value.
# Furthermore, the only values that have the potential to be equal are:
# a = c, d
# b = c, d
# a < b <= c < d will always lead to the output d-c+b-a.
if a < b and b <= c and c < d:
  print(d-c+b-a)
# a <= c <= b <= d always leads to the output d-a.
elif a <= c and c <= b and b <= d:
  print(d-a)
# a <= c < d <= b always leads to the output b-a.
elif a <= c and c < d and d <= b:
  print(b-a)
# c <= a < b <= d always leads to the output d-c.
elif c <= a and a < b and b <= d:
  print(d-c)
# c < d <= a < b always leads to the output d-c+b-a.
elif c < d and d <= a and a < b:
  print(d-c+b-a)
# c <= a <= d <= b will always lead to the output b-c.
elif c <= a and a <= d and d <= b:
  print(b-c)
