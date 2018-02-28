var users = {
	'Students': [
		{first_name: 'Michael', last_name: 'Jordan'},
		{first_name: 'John', last_name: 'Rosales'},
		{first_name: 'Mark', last_name: 'Guillen'},
		{first_name: 'KB', last_name: 'Tonel'}
	],

	'Instructors': [
		{first_name: 'Michael', last_name: 'Choi'},
		{first_name: 'Martin', last_name: 'Puryear'},
	]
}

function userNames()
{
	for(var x = 0; x < users.length; x++)
	{
		console.log(x + " - " + users[x].first_name + " " + users[x].last_name + " - " users[x].length);
	}
}

userNames();
