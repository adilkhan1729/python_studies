import random
city_list = []

with open("city_list_file.txt", "r") as fh:
    city_list = fh.read()
    city_list = city_list.split("\n")

new_city_list = []
# Convert to lower case
for city in city_list:
    new_city_list.append(city.lower())

while True:
    human_turn = input("Name a city ")
    if not human_turn.lower() in new_city_list:
        print("Computer wins, hint is - > ", random.choice(new_city_list))
        break
    randNumber= random_number = random.randint(0, 2500) # Deliberate bug
    if randNumber > len(new_city_list):
        print("Computer lost")
    else:
        print("Computer says->", new_city_list[randNumber])

