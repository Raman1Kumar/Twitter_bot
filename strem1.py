from ftplib import parse150
from glob import glob
import json
from operator import setitem
import tweepy
import credential
from set_interval import set_interval 

# Authenticate to Twitter

def doit(FileNumber,TweetNumber):


    auth = tweepy.OAuthHandler(credential.API_KEY, credential.API_SECRET)
    auth.set_access_token(credential.ACCESS_TOKEN,credential.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    # test authentication
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
        
    with open(f"./1/{FileNumber}.json") as json_data:
        data = json.load(json_data)

    
    def post_image():
        global i
       
        tweet_text=data[TweetNumber]["text"]
        image_path=f"./pic/{FileNumber}#{TweetNumber}.jpg"
        api.update_status_with_media(tweet_text, image_path)
        print("posted sucessfully")


    post_image()
