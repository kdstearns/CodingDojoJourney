$(document).ready(function(){

	$('form').submit(function(){
			return false;
		});

	$('form').submit(function(){
			var input = $('#city').val();
		
			$.get("http://api.openweathermap.org/data/2.5/weather?q="+input+"&units=imperial&appid=a2609c1e81c378c5ba7e8ab219d9cb6a", function(res){
			console.log(res);
			var name = "";
			name += "<h2>" + res.name + "</h2>";

			var temp = "";
				temp += "<h3>Temperature: " + res.main.temp + "°</h3>";

			$('#weatherData').html(name + temp)
		}, 'json');
	// $('form')[0].reset(); This is going to set all of the info into an array 
	$('#city').val(''); // This is better for simple clearing the form
	});
});
