import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#for reddit api access, unique to developer
client_id = "client_id"
client_secret = "client_secret"
user_agent = "script:shell:v1.0 (by u/username"

#the user whose comments you want to access
username = input("Enter redditor username: ")

#open reddit instance
reddit = praw.Reddit(
    user_agent=user_agent,
    client_id=client_id,
    client_secret=client_secret
)
#get all comments by user
user_comments = reddit.redditor(username).comments.new(limit=None)

#write comments to .txt
with open(f"{username}_comments.txt", "w") as file:
	for comment in user_comments:
		body = comment.body
		file.write(body+"\n\n")

#make wordcloud from .txt
with open(f"{username}_comments.txt") as file:
	wordcloud = WordCloud().generate(file.read())
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()