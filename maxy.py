'''add random functioanlity'''
'''maxy will be helping us in commenting on the posts
code: Yogitha Polavarapu'''
#import random
import facebook
#token generated from facebook you can get this from https://developers.facebook.com/tools/explorer/145634995501895/
token='<insert token here>'
graph = facebook.GraphAPI(token)

#feed = graph.get_connections("me", "home")
# first parameter is the id of the user, you can execute the second one in graph API
feed = graph.get_connections("649761338441252", "feed?{story,message,from,name}&limit=10")
#replies=["ThankYou","Thanks","Thanks a lot","Thanks a bunch","Gracias"]

for var in range(0,10):
	retrieve = feed["data"][var]
	Details = retrieve["from"]
	Name = Details["name"]
	graph.put_like(post["id"])
	#lets you know the name of the person in the console
	print "->from "+ Name
	#and the message he poseted
	print "->->"+ post["message"]
#	message= [random.randint(0, len(replies))]
#posts as a comment
	graph.put_object(post["id"], "comments", message="<insert your message> "+ fromName)
	print message
