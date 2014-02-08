$().ready(function() {
	$(".option").click(function(e) {
		e.preventDefault();
		clickedName = $(this).data("candidate-name");
		if (clickedName == correctUser) {
			$(".scorebar").text("Current streak: " + (score +1));
		}
		$(".option").each(function() {
			if ($(this).data("candidate-name") == correctUser) {
				$(this).addClass("correct");
			}
			else if ($(this).data("candidate-name") == clickedName) {
				$(this).addClass("wrong");
			}
			else {
				$(this).addClass("neutral");
			}
		});
		var leave = function () {
			if (clickedName == correctUser) {
				window.location = "/continue/" + (score + 1);
			}
			else {
				window.location = "/donegoofed/" + (score);
			}
		}
        setTimeout(leave, 1000); // check again in a second

	});
});