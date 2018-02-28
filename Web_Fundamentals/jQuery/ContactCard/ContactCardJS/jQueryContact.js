$(document).ready(function(){

	// $('form').submit(function(){
	// 	return false;
	// });

	$('form').submit(function(){
		var firstname = $('#first').val();
		var lastname = $('#last').val();
		var description = $('#desc').val();
		var contactCard = '<div><h2>' + firstname + ' ' + lastname + '</h2><p>Click here for description</p><p id="bio">' + description + '</p></div>';

		$('#card').append(contactCard);
		$('form')[0].reset();
	});

	$(document).on('click', '#card div', function(){
		$(this).children().toggle();
	});
});