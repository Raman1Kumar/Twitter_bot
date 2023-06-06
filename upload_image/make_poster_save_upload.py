from http import server
from msilib.schema import File
from re import I
from textwrap import TextWrapper

from pyautogui import sleep
# from strem1 import doit
from datetime import date, datetime


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os 


import sys
sys.path.insert(1,'F:\\coding project\\insta_bot(twitter)')
from utils.transfer_photo import transfer
from utils.pyJsonJs import pyJsonJs
from upload_image.upload_img import upload_img


# SaveImages ->Open browser using selenium and download image created by p5js on http://127.0.0.1:8000//p5/index.html or local host
def SaveImages(FileNumber,TweerNNumber):
    print("here")
    pyJsonJs(FileNumber,TweerNNumber)
    print("nother")
    browser=webdriver.Chrome()
    browser.get("http://127.0.0.1:8000//p5/index.html")
    time.sleep(10)
    while not os.path.exists(f"C:\\Users\\RAMAN KUMAR\\Downloads\\{FileNumber}#{TweetNumber}.jpg"):
            time.sleep(1)
            time_counter += 1
            print(time_counter)
            if time_counter > time_to_wait:break

    # Save image ended



def making_poster_uploading():


    # Open log file and get data for tweet number and tweet day;
    with open("./state_track/curr.txt","r") as file:
        global data
        global day
        global TweetNumber
        global TDate
        data=file.read()
        val=data.split("#")
        FileNumber=int(val[0])
        TweetNumber=int(val[1])
        TDate=val[2]
        print(f"File number is ${FileNumber}")
        print(f"TWeet number is ${TweetNumber}")
        print(f"Date  is ${TDate}")
    # Open log file and get data for tweet number and tweet day end;

        
    # 3 cases are possible 


    # 1st updating previous day with current day (when 0 image uploaded)
    if(TDate!=str(datetime.now().date())):
        with open("./state_track/curr.txt","w") as file:
            temp=f"{FileNumber+1}#{0}#{datetime.now().date()}"
            print(temp)
            file.write(temp)
            print("New Day :) \n Everything reset")
    # 1st case end;
        


    # 2nd case posted
    if(TweetNumber<=4):
        try:

            # Saving image
            print("Saving image")
            SaveImages(FileNumber,TweetNumber)
            print("Image saved")
            # Saving image ended

            
            # Transfering image
            time_to_wait = 10
            time_counter = 0
            print("tranfering the image")
            sleep(2)
            transfer("C:\\Users\\RAMAN KUMAR\\Downloads","F:\\coding project\\insta_bot(twitter)\\pic")
            print("Transfered successfully")
            sleep(2)
            # Tranfering image ended

            # Posting image
            while not os.path.exists(f"./pic/{FileNumber}#{TweetNumber}.jpg"):
                time.sleep(1)
                time_counter += 1
                print(time_counter)
                if time_counter > time_to_wait:break
        
            print("Tweeting.....")
            upload_img(FileNumber,TweetNumber)

            print("Tweeted successfully")
            # Posting image ended

            
            # upload_img(FileNumber,TweetNumber)
            with open("curr.txt","w") as file:
                temp=f"{FileNumber}#{TweetNumber+1}#{datetime.now().date()}"
                file.write(temp)
                print("new data successfully updated")
            

        except:
            print("Something went wrong")
    # 2nd case end


    # 3rd Case All mail sent
    else:
        print("Today mail sent")
    # 3rd case end;

