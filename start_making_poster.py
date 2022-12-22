from http import server
from msilib.schema import File
from re import I
from textwrap import TextWrapper

from pyautogui import sleep
from strem1 import doit
from datetime import date, datetime
from pyJsonJs import pyJsonJs

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os 

from transfer import transfer




def first():

    def SaveImages(FileNumber,TweerNNumber):
        pyJsonJs(FileNumber,TweerNNumber)
        browser=webdriver.Chrome()
        #browser.get("http://127.0.0.1:5500/p5/index.html")
        browser.get("http://127.0.0.1:8000//p5/index.html")
        # browser.get("http://localhost//p5//index.html")
        time.sleep(10)
        while not os.path.exists(f"C:\\Users\\RAMAN KUMAR\\Downloads\\{FileNumber}#{TweetNumber}.jpg"):
                time.sleep(1)
                time_counter += 1
                print(time_counter)
                if time_counter > time_to_wait:break



    # async()=>{
    #     await
    # }

    #SaveImages(0,0)




    with open("./curr.txt","r") as file:
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


        

    if(TDate!=str(datetime.now().date())):
        with open("curr.txt","w") as file:
            temp=f"{FileNumber+1}#{0}#{datetime.now().date()}"
            print(temp)
            file.write(temp)
            print("New Day :) \n Everything reset")

        



    if(TweetNumber<=4):
        try:

            print("trying")
            SaveImages(FileNumber,TweetNumber)
            print("Image saved")
                    
            time_to_wait = 10
            time_counter = 0
            # while not os.path.exists(f"C:\\Users\\RAMAN KUMAR\\Downloads\\{FileNumber}#{TweetNumber}.jpg"):
            #     time.sleep(1)
            #     time_counter += 1
            #     print(time_counter)
            #     if time_counter > time_to_wait:break
            print("tranfering the image")
            sleep(2)
            transfer("C:\\Users\\RAMAN KUMAR\\Downloads","F:\\coding project\\twitterbot\\pic")
            print("Transfered successfully")
            sleep(2)
            while not os.path.exists(f"./pic/{FileNumber}#{TweetNumber}.jpg"):
                time.sleep(1)
                time_counter += 1
                print(time_counter)
                if time_counter > time_to_wait:break

        
            print("Tweeting.....")
            doit(FileNumber,TweetNumber)
            print("Tweeted successfully")

            
            # doit(FileNumber,TweetNumber)
            with open("curr.txt","w") as file:
                temp=f"{FileNumber}#{TweetNumber+1}#{datetime.now().date()}"
                file.write(temp)
                print("new data successfully updated")
            

        except:
            print("send mail eroor")
    else:
        print("Today mail sent")
