var quarters = 0;

function slots()
{
	var chance = Math.floor(Math.random() * 100);
	var payout = Math.floor(Math.random() * 50) + 50;
	var win = 67;

	if(chance === win)
	{
		console.log(chance);
		console.log("YOU WIN!!!!")
		console.log(payout);
		quarters += payout;
		console.log(quarters);
	}

	else
	{
		console.log(chance);
		console.log("Sorry, play again!")
	}
}

slots();