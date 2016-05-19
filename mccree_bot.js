var _           = require('lodash');
var Client      = require('node-rest-client').Client;
var Twit        = require('twit');
var async       = require('async');


var t = new Twit({
	consumer_key        : process.env.MCCREE_BOT_TWIT_CONSUMER_KEY,
    	consumer_secret     : process.env.MCCREE_BOT_TWIT_CONUSMER_SECRET,
    	access_token        : process.env.MCCREE_BOT_TWIT_ACCESS_TOKEN,
    	access_token_secret : process.env.MCCREE_BOT_TWIT_ACCESS_TOKEN_SECRET
});

run = function(){
	async.waterfall([
	  getPlaces,
	  formatTweet,
	  postTweet
	  ],
	  }

getPlaces = function(){
	var current_time = new Date();
	if((current_time.getMinutes()) == 0){
		var GMT = current_time.gethours() - 5;
		var which_time = 'GMT-' + GMT;
		var place = fileRead(which_time);	
	}
}

function fileRead(file){
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", file, false);
	rawFile.onreadystatechange = function(){
		if(rawFile.status === 4){
			if(rawFile.status === 200 || rawFile.status == 0){
				var alltext = rawFile.responseText;
				alert(allText);
			}
		}
	}
	rawFile.send(null);
}
}
