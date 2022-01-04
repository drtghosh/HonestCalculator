score = int(input())
max_score = int(input())
percent = 100 * score / max_score

percent_a, percent_b, percent_c, percent_d = 90, 80, 70, 60

if percent >= percent_a:
    print('A')
elif percent >= percent_b:
    print('B')
elif percent >= percent_c:
    print('C')
elif percent >= percent_d:
    print('D')
else:
    print('F')