from collections import deque
def function(num, operand):
    s = num[0]
    flag = 0
    for i in range(len(operand)):
        if operand[i] == "-":
            flag = 1
            
        if flag == 0:
            s += num[i+1]
        else:
            s -= num[i+1]
    return s

line = list(input())
string = []
num_set = []
operand = []
for i in line:
    if i == "+" or i == "-":
        num_set.append(int("".join(string)))
        operand.append(i)
        string = []
    else:
        string.append(i)
num_set.append(int("".join(string)))

print(function(num_set,operand))
