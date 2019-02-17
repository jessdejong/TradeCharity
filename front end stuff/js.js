$(window).on("load", function() {
	$("#newsContainer").hide();
	$("#investContainer").hide();
	$("#down").click(function(){
		clicked = true;
		$("html,body").animate({scrollTop: $(window).height()}, 1000); 
	});
	$("#portfolio").click(function(){
		$("#newsContainer").hide();
		$("#investContainer").hide();
		$("#portfolioContainer").show();
	});
	$("#news").click(function(){
		$("#portfolioContainer").hide();
		$("#investContainer").hide();
		$("#newsContainer").show();
	});
	$("#invest").click(function(){
		$("#portfolioContainer").hide();
		$("#newsContainer").hide();
		$("#investContainer").show();
	});
});