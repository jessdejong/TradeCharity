function init(year, month, day, money)
{
	$("#table table").find("tr:gt(0)").remove();
	$.get("backtest/"+year+"/"+month+"/"+day+"/"+money,function(data){
		//console.log(data);
		var ar = data.split("\n");
		//console.log(ar);
		var hi = 0;		
		for(var line in ar)
		{
			if(line==ar.length-1) break;
			//console.log(ar[line]);
			var ar2 = ar[line].split("|");
			var testing = $('<div class="card"><h3>'+ar2[2]+' ('+ar2[6]+')'+'</h3><p>'+ar2[3]+'</p></div>');
			$(testing).click(function(){
				window.open(ar2[4]);
			});
			$("#cardContainer").append(testing);
			
			var sent = parseFloat(ar2[6]);
			var times = parseInt(ar2[8]);
			hi += times;				
			if (sent > 0) {
				$("#table table").append('<tr><td>'+ar2[1]+'</td><td>'+ar2[8]+'</td><td>$'+ar2[7]+'</td><td style="color:green">'+(parseInt(ar2[10])-parseInt(ar2[9]))+'</td><td>$'+(parseFloat(ar2[7])/money)+'</td><td>$'+ar2[9]+'</td></tr>');
			}
			else {
				$("#table table").append('<tr><td>'+ar2[1]+'</td><td>'+ar2[8]+'</td><td>$'+ar2[7]+'</td><td style="color:red">'+(parseInt(ar2[9])-parseInt(ar2[10]))+'</td><td>$'+(parseFloat(ar2[7])/money)+'</td><td>$'+ar2[9]+'</td></tr>');
			}
			if(line==ar.length-2)
			{
				$("#numberTable table tr:nth-child(2) > td:nth-child(1)").html("$"+ar2[7]);
				$("#numberTable table tr:nth-child(2) > td:nth-child(2)").html("$"+(parseInt(ar2[7])-money));
				$("#numberTable table tr:nth-child(2) > td:nth-child(3)").html(hi);
			}

		}

	});
}

$(window).on("load", function() {
	init(2019,1,30,1000);
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
		$("#cardContainer").hide();
		$("#investContainer").show();
	});
	$("form").keypress(function(event){
		if(event.key == "Enter")
			init(parseInt($("form input:nth-child(1)").val()), parseInt($("form input:nth-child(3)").val()), parseInt($("form input:nth-child(5)").val()), parseInt($("form input:nth-child(7)").val()));
	});
});
