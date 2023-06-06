
import json

import sys
sys.path.insert(1,'F:\\coding project\\insta_bot(twitter)')

def pyJsonJs(FileNumber,TweetNumber):
    with open("./state_track/middle.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["FileNumber"] = FileNumber
    data["TweetNumber"]=TweetNumber

    with open("middle.json", "w") as jsonFile:
        json.dump(data, jsonFile)

