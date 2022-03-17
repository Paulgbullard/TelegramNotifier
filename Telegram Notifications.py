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
import config

def time_check():
    current = datetime.now()
    current = current.strftime("%M")
    
    return(current)

def time_get():
    current = datetime.now()
    current = current.strftime("%H:%M")
    
    current = current+" update:"
    
    return(current)

def temp_get():
    url2 = "https://www.metoffice.gov.uk/weather/forecast/u10k6gts5#?nearestTo=Higham%20(Kent)&date=2022-03-04"
    req = requests.get(url2)
    soup = BeautifulSoup(req.text, "html.parser")

    curr_temp = soup.find("tr",class_ = "step-temp")
    curr_temp = curr_temp.select("div")[0].text
    curr_temp = "The current temperature is: "+curr_temp

    return(curr_temp)

def headline_get():
    url = "https://www.bbc.co.uk/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    headline = soup.find('p',class_='ssrcss-6arcww-PromoHeadline e1f5wbog4').text
    headline = "The BBC's current headline is: "+headline
    return(headline)

def sport_headline_get():
    url = "https://www.bbc.co.uk/sport"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    headline = soup.find('h3',class_='gs-c-promo-heading__title gel-double-pica-bold sp-o-link-split__text').text
    headline = "The BBC's current sport headline is: "+headline
    return(headline)
    
def telsend(msg):
    token = config.token
    url = f"https://api.telegram.org/bot{token}"
    params = {"chat_id": config.chat, "text": msg}
    r = requests.get(url + "/sendMessage", params=params)
    
if __name__ == '__main__':
    while True:
        if time_check() == '00':
            time_get()
            headline_get()
            sport_headline_get()
            temp_get()
            msg = time_get()+"\n"+temp_get()+"\n"+headline_get()+"\n"+sport_headline_get()
            telsend(msg)
            wait = 1
            time.sleep(wait*60)
        


