import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import json
from set_interval import set_interval 
import credential

import requests



# Getting credential
ACCESS_TOKEN=credential.INSTAGRAM_ACCESS_TOKEN
USER_ID=credential.INSTAGRAM_USER_ID


cloudinary.config(
  cloud_name = credential.CLOUDINARY_CLOUD_NAME,
  api_key = credential.CLOUDINARY_API_KEY,
  api_secret = credential.CLOUDINARY_API_SECREAT,
  secure = True
)
# Getting credential end



def post_image(data,FileNumber,TweetNumber):


    # Getting image path and caption text
    caption=data[TweetNumber]["text"]
    print(caption)
    image_path=f"./pic/{FileNumber}#{TweetNumber}.jpg"
    print(image_path)
    # Getting image path and caption text end


    # Posting on Cloudinary
    image_id=f"{FileNumber}_{TweetNumber}"
    print("image id")
    print(image_id)
    print("uploading image on Cloudinary")
    upload_data=upload(image_path, public_id=image_id)
    print(upload_data["url"])
    img_url=upload_data["url"]
    # Posting on Cloudinary end;


  # Uploading image in instagram container and posting
    print("Uloading image on instagram and posting")


    # Uploading image in instagram container
    CAPTION=caption 
    IMG_URL=img_url
    url = f"https://graph.facebook.com/v17.0/{USER_ID}/media?image_url={IMG_URL}&caption={CAPTION}&access_token={ACCESS_TOKEN}"
    payload={}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    data = response.json()
    print(data)
    CREATION_ID=data['id']
    # Uploading image in instagram container end;


    # Posting image on Instagram
    url = f"https://graph.facebook.com/v17.0/{USER_ID}/media_publish?creation_id={CREATION_ID}&access_token={ACCESS_TOKEN}"
    payload={}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    # Posting image on Instagram end;


    # Deleting image from cloudinary
    print("Deleting image from cloudinary")
    cloudinary.uploader.destroy(f"{FileNumber}_{TweetNumber}")
    # Deleting image from cloudinary


    print("posted sucessfully")




# Function which open file whose text is need to be posted and post it.
def upload_img(FileNumber,TweetNumber):
   
    
    
    with open(f"./1/{FileNumber}.json") as json_data:
        
        data = json.load(json_data)
        post_image(data,FileNumber,TweetNumber)
#upload image end

    

   




   