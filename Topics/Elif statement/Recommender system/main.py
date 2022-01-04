age = int(input())
movie_dict = {
    16: "Lion King",
    25: "Trainspotting",
    40: "Matrix",
    60: "Pulp Fiction",
}

age_limits = list(movie_dict.keys())
for a in age_limits:
    if age <= a:
        print(movie_dict[a])
        break
if age > 60:
    print("Breakfast at Tiffany's")