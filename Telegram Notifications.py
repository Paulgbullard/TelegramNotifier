#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:00:49 2022

@author: paul
"""

from bs4 import BeautifulSoup
import requests
import re
import time
from datetime import datetime
import tweepy
import config

def time_check():
    #Get the current date/time
    current = datetime.now()
    
    #Strip the minutes from the date/time
    current = current.strftime("%M")
    
    #return the current minute
    return(current)

def hour_check():
    #Get the current date/time
    current = datetime.now()
    
    #strip the hour from the date/time, and convert to int
    current = int(current.strftime("%H"))
    
    #return the current hour
    return(current)
    

def time_get():
    #Get the current date/time
    current = datetime.now()
    
    #Strip hours and minutes from the date/time
    current = current.strftime("%H:%M")
    
    #Create a string
    current = current+" update:"
    
    #return the string
    return(current)

def temp_get():
    #get the met office page for Strood
    url2 = "https://www.metoffice.gov.uk/weather/forecast/u10k6gts5#?nearestTo=Higham%20(Kent)&date=2022-03-04"
    req = requests.get(url2)
    soup = BeautifulSoup(req.text, "html.parser")

    #find the table row with the current temperature
    curr_temp = soup.find("tr",class_ = "step-temp")
    
    #get the value
    curr_temp = curr_temp.select("div")[0].text
    
    #create a string
    curr_temp = "The current temperature is: "+curr_temp

    #return the string
    return(curr_temp)

def headline_get():
    #get the bbc homepage
    url = "https://www.bbc.co.uk/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    #find the main headline
    headline = soup.find('p',class_='ssrcss-6arcww-PromoHeadline e1f5wbog4').text
    
    #create a string
    headline = "The BBC's current headline is: "+headline
    
    #return the string
    return(headline)

def sport_headline_get():
    #get the bbc sport page
    url = "https://www.bbc.co.uk/sport"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    #find the main headline
    headline = soup.find('h3',class_='gs-c-promo-heading__title gel-double-pica-bold sp-o-link-split__text').text
    
    #create a string
    headline = "The BBC's current sport headline is: "+headline
    
    #return the string
    return(headline)

def tweet_get():
    # API Keys and Tokens
    consumer_key = config.twitterapi
    consumer_secret = config.twitterapisecret
    access_token = config.twitteraccess
    access_token_secret = config.twitteraccesssecret

    # Authorization and Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # WOEID of UK
    woeid = 23424975
     
    # fetching the trends
    trends = api.get_place_trends(id = woeid)
    
    #return the value in a string
    return("The top trend in the UK is: "+trends[0]['trends'][0]['name'])
    
def telsend(msg):
    #Authenticate
    token = config.token
    url = f"https://api.telegram.org/bot{token}"
    
    #Create the params
    params = {"chat_id": config.chat, "text": msg}
    r = requests.get(url + "/sendMessage", params=params)

if __name__ == '__main__':
    while True:
        if time_check() == '00' and (8 <= hour_check() <=22):
            time_get()
            headline_get()
            sport_headline_get()
            temp_get()
            tweet_get()
            msg = time_get()+"\n"+temp_get()+"\n"+headline_get()+"\n"+sport_headline_get()+"\n"+tweet_get()
            telsend(msg)
            wait = 1
            time.sleep(wait*60)
            int == 0
            int = int + 1
            print("Checked "+int+" times")
            
        


