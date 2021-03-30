import sys
sys.stdin = open('teleport.in', 'r')
sys.stdout = open('teleport.out', 'w')
a, b, x, y = [int(i) for i in input().split(" ")]
ans_one = (abs(min([a,b])-min([x,y]))+abs(max([a,b])-max([x,y])))
ans_two = abs(b-a)
ans_three = abs(a-b)
print(min([ans_one, ans_two, ans_three]))
