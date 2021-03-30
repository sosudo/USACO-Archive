# We use sys to reassign our input and output
import sys
# Reassign standard input and output by opening the necessary files and setting them
# to the values of sys.stdin and sys.stdout
sys.stdin = open('teleport.in', 'r')
sys.stdout = open('teleport.out', 'w')
# Mapping the input to the values a, b, x, and y using a list comprehension
a, b, x, y = [int(i) for i in input().split(" ")]
# The two possible paths from the start point (a or b) is directly from a to b 
# or by going from the start point (a or b), going to the closest teleporter (x or y), 
# teleporting, and then going from the second teleporter (y or x) to
# the stop point (b or a).
# ans_one is the distance of the path through the teleporters.
# It is essentially the distance from the leftmost point between the two choices a or b
# and the leftmost point between the two choices x or y added to the distance from
# rightmost point between the two choices x or y to the rightmost point between the
# two choices a or b.
ans_one = (abs(min([a,b])-min([x,y]))+abs(max([a,b])-max([x,y])))
# ans_two is the distance of the direct path from a to b
# It is essentially the distance between a and b
ans_two = abs(b-a)
# Output the lowest value of the two potential answers
print(min([ans_one, ans_two]))
# This approach can be reduced to five lines by deleting the ans_one and ans_two variable initializations and replacing the print statement with
# print(min([(abs(min([a,b])-min([x,y]))+abs(max([a,b])-max([x,y]))), abs(b-a)]))
# It is maintained at seven lines for readability.
