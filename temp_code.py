my_dict = { 'numa': 6, 'numb': 3, 'numc': 2, 'numd': 4, 'nume': 1, 'numf': 5}
sortedDict = sorted(my_dict)
print(my_dict)
print(sortedDict)


idk = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
print(sorted_footballers_by_goals[0][0])
