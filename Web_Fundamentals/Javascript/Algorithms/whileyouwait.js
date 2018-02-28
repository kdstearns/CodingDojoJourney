function countdown(num)
{
	var daysUntilMyBirthday = num;
	while (daysUntilMyBirthday >= 30)
	{
		console.log(daysUntilMyBirthday + " days left, I wish it was closer.");
		daysUntilMyBirthday--;
	}

	while (daysUntilMyBirthday < 30 && daysUntilMyBirthday > 5)
	{
		console.log(daysUntilMyBirthday + " left, YAY it's getting close!");
		daysUntilMyBirthday--;
	}
	while(daysUntilMyBirthday <= 5 && daysUntilMyBirthday > 0)
	{
		console.log("MY BIRTHDAY IS ALMOST HERE!!!!!");
		daysUntilMyBirthday--;
	}

	while(daysUntilMyBirthday == 0)
	{
		return("YES! IT'S FINALLY HERE!!! PARTY TIME!");
	}
}

countdown(5);