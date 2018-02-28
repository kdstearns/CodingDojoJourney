$(document).ready(function(){

	var pokemon = "";
	for (var x = 1; x <= 151; x++)
	{
		pokemon += "<img id="+x+" src='https://pokeapi.co/media/img/" + x + ".png'>";
	}
	var imgFill = '<div>' + pokemon + '</div>';

	$('#pokeImgs').append(imgFill);

	$('img').click(function(){
		var id = $(this).attr('id');
		$.get('https://pokeapi.co/api/v2/pokemon/'+id+'/' , function(res){

			console.log(res);

			var name = "";
			name += "<h2>" + res.name + "</h2>";

			var sprite = "<img src='"+res.sprites.front_default+"'>"

			var type = "";
			type += "<h3>Types</h3>";
			type += "<ul>";

			for(var x = 0; x < res.types.length; x++)
			{
				type += "<li>" + res.types[x].type.name + "</li>";
			}
			type += "</ul>";
			
			var height = "";
			height += "<h3>Height</h3>";
			height += "<h4>" + res.height + "</h4>";

			var weight = "";
			weight += "<h3>Weight</h3>";
			weight += "<h4>" + res.weight + "</h4>";

			$('#info').html(name + sprite + type + height + weight);
		}, 'json');
	});
});