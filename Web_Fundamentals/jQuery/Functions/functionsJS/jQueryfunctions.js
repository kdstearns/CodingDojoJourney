$(document).ready(function(){

	$('img').hide();

	$('#classButton').click(function(){
		$('#classPar').addClass('newClass');
	});

	$('#slideButton').click(function(){
		$('#surprise').slideToggle();
	});

	$('#appButton').click(function(){
		$('#result').append('<h4> Look what I can do! </h4>');
	});

	$('#downButton').click(function(){
		$('#notfart').slideDown();
	});

	$('#upButton').click(function(){
		$('#notfart').slideUp();
	});

	$('#fadeInButton').click(function(){
		$('#comic').fadeIn("slow", function(){
		});
	});

	$('#fadeOutButton').click(function(){
		$('#comic').fadeOut("slow", function(){
		});
	});

	function displayVals(){
		var singleValues = $('#single').val();
		var multipleValues = $('#multiple').val() || [];
		$('h4').html(' <b> Single: </b> ' + singleValues + ' <b> Multiple </b> ' + multipleValues.join(", ") );
	}

		$('select').change(displayVals);
		displayVals();

});