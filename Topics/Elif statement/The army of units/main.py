army = int(input())

army_dict = {1: 'no army',
             10: 'few',
             50: 'pack',
             500: 'horde',
             1000: 'swarm'}

breakpoints = list(army_dict.keys())
for point in breakpoints:
    if army < point:
        print(army_dict[point])
        break
if army >= 1000:
    print("legion")
