from facebook_scraper import get_posts
from message.models import socialMessage

def scrap(i):
	for posts in get_posts('alcheringaiitg', pages=i):
		inst=socialMessage()
		inst.message = posts['text']
		inst.imglink = posts['image']
		inst.save()

	print('Scraping done!')