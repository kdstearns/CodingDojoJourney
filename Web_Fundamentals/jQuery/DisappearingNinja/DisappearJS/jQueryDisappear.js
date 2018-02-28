$(document).ready(function(){

	$('img').click(function(){
		$(this).attr('src','../DisappearIMGS/blank.jpg')
	});

	$('button').click(function(){
		$('img').attr('src','../DisappearIMGS/dogkisses.jpg');
	});
});