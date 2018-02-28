var arr=[4, "purple", -12, "unicorn"];
var newArray=[];
function numbersOnly()
{
	for(var x = 0; x < arr.length; x++)
	{
		if(typeof arr[x] === "number" )
		{
			newArray.push(arr[x]);
		}
	}
	return newArray;
}

numbersOnly();