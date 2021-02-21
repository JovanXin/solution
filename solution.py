# 2019 R1 Q3
""" Optimizations made: 

1) Switched to dict instaed of list for people to avoid iterating through them every time
2) Create dictionary for total of each tea required for satisfaction, then subtract each one from the host's teas to see how many people would be unsatisfied

Wanted to optimize:
1) Only store data for number of teas if person was not a potential host -> could not do this as they gave hosts at the end? 
2) How can I store them as ints directly from input? Eg. line 34 
"""

people_teas = {
    "G": 0,
    "C": 0,
    "E": 0,
    "P": 0,
    "L": 0,
    "S": 0
}

people = {}

regular_people, potential_hosts = input().split()

regular_people = int(regular_people)
potential_hosts = int(potential_hosts)

for i in range(regular_people):
    person, fav_tea = input().split()
    people[person] = {
        "fav_tea": fav_tea,
    }
    
for j in range(regular_people):
    name, G, C, E, P, L, S = input().split()
    people[name]["teas"] = {
        "G": int(G),
        "C": int(C),
        "E": int(E),
        "P": int(P),
        "L": int(L),
        "S": int(S)
    }

hosts = []

for person in people.values():
    people_teas[person["fav_tea"]] += 1

for y in range(potential_hosts):
    host_name = input()
    unsatisfied = 0
    
    person_stats = people[host_name]["teas"]


    for people_tea_val, host_tea_val in zip(people_teas.values(), person_stats.values()):
        if people_tea_val > host_tea_val:
            unsatisfied += (people_tea_val - host_tea_val)
    

    if unsatisfied == 0:
        print(f"{host_name} Successful")
    elif unsatisfied <= 2:
        print(f"{host_name} Mildly Successful ({unsatisfied})")
    elif unsatisfied >2:
        print(f"{host_name} Disaster ({unsatisfied})")
