import sys
sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')
line_one = input()
line_two = input()
a, b = [int(i) for i in line_one.split(" ")]
c, d = [int(i) for i in line_two.split(" ")]
if a < b and b <= c and c < d:
  print(d-c+b-a)
elif a <= c and c <= b and b <= d:
  print(d-a)
elif a <= c and c < d and d <= b:
  print(b-a)
elif c <= a and a < b and b <= d:
  print(d-c)
elif c < d and d <= a and a < b:
  print(d-c+b-a)
elif c <= a and a <= d and d <= b:
  print(b-c)
