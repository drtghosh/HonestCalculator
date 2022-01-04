box_l = int(input())
box_w = int(input())
box_h = int(input())
door_w = int(input())
door_h = int(input())

box_second = sorted([box_l, box_w, box_h])[1]
box_min = min(box_l, box_w, box_h)

door_max = max(door_w, door_h)
door_min = min(door_w, door_h)

if box_second <= door_max and box_min <= door_min:
    print("The box can be carried")
else:
    print("The box cannot be carried")