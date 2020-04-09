T = int(input())
games = int(input())
scores = {1:0, 2:0, 3:0, 4:0}
for i in range(games):
    s = list(map(int, input().split(" ")))
    if s[2] > s[3]:
        scores[s[0]] += 3
    elif s[2] < s[3]:
        scores[s[1]] +=3
    else:
        scores[s[0]] +=1
        scores[s[1]]+=1
rem = 6 - games
for i in range(rem):
    