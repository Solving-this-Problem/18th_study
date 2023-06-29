N = int(input())

pattern = []
for _ in range(N):
    pattern.append(list(input()))

# 1. Find the head
for i in range(N):
    for j in range(N):
        if pattern[i][j] == "*":
            head = (i, j)
            break
    else:
        continue
    break


heart = (head[0] + 1, head[1])

l_arm, r_arm, waist, l_leg, r_leg = 0, 0, 0, 0, 0
i, j = heart

while  j-1-l_arm >= 0 and pattern[i][j-1-l_arm] == '*':
    l_arm += 1

while j+1+r_arm < N and  pattern[i][j+1+r_arm] == '*':
    r_arm += 1

while i+1+waist < N and  pattern[i+1+waist][j] == '*':
    waist += 1

while i+1+waist+l_leg < N and pattern[i+1+waist+l_leg][j-1] == '*':
    l_leg += 1

while i+1+waist+r_leg < N and pattern[i+1+waist+r_leg][j+1] == '*':
    r_leg += 1

print(*map(lambda x: x+1, heart)) 
print(l_arm, r_arm, waist, l_leg, r_leg)
