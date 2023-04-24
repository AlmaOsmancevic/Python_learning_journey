#last semesters grades stored in 2d-list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#list creations
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#New grade just came in - add to list with append()
gradebook.append(["computer science", 100])

#New grade just came in - add to list with append()
gradebook.append(["visual arts", 93])

#modify grade on visual arts 
gradebook[-1][-1] = 98

#Delete grade from poetry class with remove()
gradebook[2].remove(85)

#Add new grade type instead for poetry class
gradebook[2].append("Pass")

#store last semesters grades with this years grade together in one full gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)