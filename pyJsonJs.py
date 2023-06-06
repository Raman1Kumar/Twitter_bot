
import json

def pyJsonJs(FileNumber,TweetNumber):
    with open("middle.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["FileNumber"] = FileNumber
    data["TweetNumber"]=TweetNumber

    with open("middle.json", "w") as jsonFile:
        json.dump(data, jsonFile)