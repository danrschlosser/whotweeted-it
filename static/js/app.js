$().ready(function() {
	$("form").submit(function(e) {
		e.preventDefault();
		var val = $("#user_name").val();

		$.post("/post/"+val+"/"+score, function() {
			var leaderboard = function() {
				window.location = "/leaderboard";
			};
			setTimeout(leaderboard, 500);

		});
	});

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
				if (score === 0) {
				window.location = "/continue/" + (score);
				}
				else {
				window.location = "/donegoofed/" + (score);
				}
			}
		};
        setTimeout(leave, 500); // check again in a second

	});



    var $quote = $(".candidate-name");

    var $numChars = $quote.text().length;

    if (($numChars >= 1) && ($numChars < 13)) {
        $quote.css("font-size", "1.4em");
    }
    else if (($numChars >= 13) && ($numChars < 15)) {
        $quote.css("font-size", "1.2em");
    }
    else if ($numChars >= 15) {
        $quote.css("font-size", "1em");
	}
});

function sharefacebook () {
	FB.login(function (res) {
        //problem with facebook login
        if(!res.authResponse) {
          alert('problem with facebook login. Please try again or use an email.');
        }
        //post to wall
        
        //get data about person
        FB.api('/me', function (res) {

res.first_name
res.last_name

        FB.ui({
          method: 'feed',
          name: 'Who Tweeted It',
          link: 'whotweeted.it',
          picture: 'http://www.earthtimes.org/newsimage/environmental-impact-disposal-waste-large-scale-pig-production.jpg',
          caption: 'Who Tweeted It',
          description: "I got a score of " + score + ". Can you beat me?"
        },
        function(response) {
          if (response && response.post_id) {
				window.location = "/leaderboard";
          } else {
            var leaderboard = function() {
				window.location = "/leaderboard";
			};
          }
        });
      }, {scope: 'publish_actions'});


          
      });
        


        
}

