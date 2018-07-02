# File: GivingThanks Bot

import praw
import re
import pdb 
import os 


CLIENT_ID = ''
CLIENT_SECRET = ''
PASSWORD = ''
USERNAME = ''
USER_AGENT = ''

SUBREDDIT_NAME = ''

#if using praw.ini file, use bot profile in there
reddit = praw.Reddit(
	client_id = CLIENT_ID,
	client_secret = CLIENT_SECRET,
	password = PASSWORD,
	username = USERNAME,
	user_agent = USER_AGENT) 
subreddit = reddit.subreddit(SUBREDDIT_NAME)

#If no txt file, create it, and create list
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
#Compilation of comment IDs that have been used
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#Every new comment that contains "!ty" will be replied with you have been given thanks.
#Every new comment that contains "!deletethanks" will delete the parent comment, as long as the author is of the bot.
print("Begin Comment stream.")
for comment in subreddit.stream.comments():
	if re.search("!ty", comment.body, re.IGNORECASE):
		parent=comment.parent()
		print("Found parent comment for !ty.")
		if parent.id not in posts_replied_to:
			print("Bot replying to :", parent.author)
			parent.reply("You have been given thanks!")
			print("User has been given thanks.")
			posts_replied_to.append(parent.id)
			with open("posts_replied_to.txt", "w") as f:
				for post_id in posts_replied_to:
					f.write(post_id + "\n")		
			print("Successfully written to txt file")
		else:
			print("Already been replied to.")
	if re.search("!deletethanks", comment.body, re.IGNORECASE):
		parent=comment.parent()
		if parent.author == "GivingThanksBot":
			print("Deleting parent comment.")
			parent.delete()
		
		
################################################
#The rest is if you wish to include submissions#
################################################		
	
#For submission posts- they are separate from comments.

#for printing simple information
#for submission in subreddit.hot(limit=5):
	#print("Title: ", submission.title)
	#print("Test: ", submission.selftext)
	#print("Score: ", submission.score)
	#print("--------------------------\n")
	
	
#	if submission.id not in posts_replied_to:
#		if re.search("!ty", submission.selftext, re.IGNORECASE):
#			submission.reply("You have been given thanks!")
#			print("Bot replying to : ", submission.title)
#			posts_replied_to.append(submission.id)


