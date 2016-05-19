import tweepy, datetime, time

CONSUMER_KEY = 'MIc92N3vOhNLxTouH3NsGfpBg'
CONSUMER_SECRET = 'opG7SIvcUWMFhM3quGVMmeF52t1BYNoRvYTatm1Ecvbjck8J0E'
ACCESS_KEY = '730526129069527040-GUIfGuLmsvT4OlnrP5JffTs6dwogQfq'
ACCESS_SECRET = 'mBWPOETlw3FsjGdgXhLwwavWqxzH9UfaCQbCiS0IOIJoE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



while True:
	now = datetime.datetime.now()
	append = 'GMT-'
	script = "It's high noon... in "
	if (now.minute == 0):
		hour = now.hour
		if (hour == 0):
			hour = 19
		elif(hour == 1):
			hour = 20
		elif(hour == 2):
			hour = 21
		elif(hour == 3):
			hour = 22
		elif(hour == 4):
			hour = 23
		else:
			hour -= 5
		append += str(hour)
		append += '.txt'
		filename = open(append, 'r')
		f = filename.readline()
		filename.close()
		script += f
		api.update_status(script)
		print (script) 
		time.sleep(3600)
