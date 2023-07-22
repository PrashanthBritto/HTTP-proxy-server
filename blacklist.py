blacklistdomain = ["spotify.com","facebook.com"]

def check_if_blocked(domain):
	if domain in blacklistdomain:
		return True
	else:
		return False