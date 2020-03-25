import requests
import hashlib


url_prof = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/1c/1c7e037c1968d2127e2b75d54fb86cbd12dffd32.jpg"
url_mark = "https://steamcommunity-a.akamaihd.net/market/image/4EIH0R7GqQJrfzDFJIBMPGWWareRUqaCMD5gXTZQcRbgCPD_NmctUqp7NwnnCu92YuVoXp58cgEAh67FS1ZbdAmWUN0R-mE4KQPjHUEjTbUmnv3Il8GmDpaRB5BzBPXDgJlqBAgmjbC9ds4KYVB39QdsaY1H4olZovSYejj3/avatar.jpg"

#url = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/29/29e026cb677a13fa6eaf47cb0798692b34d35202.jpg"

response = requests.get(url_prof)
response_2 = requests.get(url_mark)

print(response.content[:500]==response_2.content[:500])
print(hashlib.sha256(response.content[:500]).hexdigest())


def get_similar(profile_url, collection):
    profile_url = profile_url.split('_full.jpg')[0] + '.jpg'
    response = requests.get(profile_url)
    picture_hash = hashlib.sha256(response.content[:500]).hexdigest()

    return  # collection.find_one({"image_hash": picture_hash})


#def is_similar(first, second):
#    first = np.asarray(first).flatten()
#    second = np.asarray(second).flatten()
#    correlation = np.corrcoef(first, second)
#    return correlation [0][1] > 0.92


#def hash_img(first, second):
#    first = np.asarray(first).flatten()
#    second = np.asarray(second).flatten()
#    intersection = np.intersect1d(first,second)
#    print(intersection)



#print(hash_img(img_1,img_2))
