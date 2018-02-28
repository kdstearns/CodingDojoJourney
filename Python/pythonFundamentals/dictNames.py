# PART ONE
# students = [
# 	{'first_name': 'Michael', 'last_name': 'Jordan'},
# 	{'first_name': 'John', 'last_name': 'Rosales'},
# 	{'first_name': 'Mark', 'last_name': 'Guillen'},
# 	{'first_name': 'KB', 'last_name': 'Tonel'},
# ]

# def studentNames(var):
# 	for element in var:
# 		print element['first_name'] + ' ' + element['last_name']
# studentNames(students)


# PART TWO
users = {
	'Students': [
		{'first_name': 'Michael', 'last_name': 'Jordan'},
		{'first_name': 'John', 'last_name': 'Rosales'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'},
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choy'},
		{'first_name': 'Martin', 'last_name': 'Puryear'},
	]
}

def allNames(var):
	for key, data in users.items():
		num = 1
		print key
		for value in data:
			print str(num) + " - " + value['first_name'].upper() + " " + value['last_name'].upper() + " - " + str(len(value['first_name']) + len(value['last_name']))
			num += 1

allNames(users)