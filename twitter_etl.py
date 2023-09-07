import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():

    consumer_key = "" 
    consumer_secret = "" 
    access_key = ""
    access_secret = ""


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

        # Creating an API object 
    api = tweepy.API(auth)
    # using get_user with screen_name

    screen_names = ['elonmusk','iamsrk']
    list_tweet_info = []

    for each_screen_name in screen_names:
        user = api.get_user(screen_name=each_screen_name)
        tweet_dict = {
            "user_id" : user.id,
            "user_description" : user.description,
            "user_followers_count" : user.followers_count
        }
        list_tweet_info.append(tweet_dict)

    print(list_tweet_info)
    df = pd.DataFrame(list_tweet_info)
    df.to_csv('s3-bucket-path')

if __name__=="__main__":
    run_twitter_etl()
