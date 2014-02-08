$().ready(function() {
	$(".option").click(function(e) {
		e.preventDefault();
		clickedName = $(this).data("candidate-name");
		$(".option").forEach(function(option) {
			if (option.data("candidate-name") === correctUser) {
				option.addClass("correct");
			}
			else if (option.data("candidate-name") === clickedName)
			{
				option.addClass("wrong");
			}
			else
			{
				option.addClass("neutral");
			}
		})
		if (clickedName === correctUser) {
			window.location = "/continue/" + (score + 1);
		}
		else {
			window.location = "/you_goofed" + (score);
		}
	})
})