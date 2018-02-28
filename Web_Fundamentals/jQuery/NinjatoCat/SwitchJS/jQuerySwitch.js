$(document).ready(function(){

	$('img').click(function(){
		var temp1 = $(this).attr('data-alt-src');
		var temp2 = $(this).attr('src');
		$(this).attr('data-alt-src',temp2)
		$(this).attr('src',temp1);
	});
});