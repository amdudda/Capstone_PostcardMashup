'''
This will eventually hold code that returns a url to an image on Pixabay.
'''
import requests # http://docs.python-requests.org/en/master/
import random
import urllib, datetime
from os.path import sep

def get_image_url(search, pixabaykey=None):
    '''
    Requests a bunch of images from Pixabay API and picks a random image from the results.
    :param search_for:
    :return: url as string if successful, None if no results found
    '''
    if not pixabaykey:
        from APItools.APIkeys import pixabaykey # NB: APIkeys is not shared with repo to protect key integrity
    search_url = "https://pixabay.com/api"
    apiparms = {
        'key': pixabaykey,
        'q': search
    }

    # request data from Pixabay API
    resp = requests.get(search_url, params=apiparms)
    status = resp.status_code
    if status == 200:
        response = resp.json()
        # print(response.text)
        # response = response.json()
        hits = response['hits']
        hitcount = len(hits)
        if hitcount > 0 :
            # if data is returned, pick a random hit and return the image url found in the selected hit
            selected_index = random.randint(0, hitcount-1)
            # print(selected_index)
            # print(hits[selected_index]['previewURL'])
            return hits[selected_index]['previewURL']
        else:
            # if no results found, return None so code can inspect for that.
            return None
    else:
        print ("Got other status_code, returning None for now: " + str(status))
        return None

def save_image(imageurl):
    ''' takes a url as an argument and tries to save the image to a directory'''

    def timestamp():
        stamp = datetime.datetime.now()
        ts = str(stamp.date()) + "-" + str(stamp.hour) + "-" + str(stamp.minute)
        return ts

    startfrom = imageurl.rfind("/") + 1

    ts = timestamp()
    filename = ts + "_" + imageurl[startfrom:]
    print(filename)

    # use os.path.sep to insert the appropriate directory delimiter between directory and filename
    filepath = "images" + sep + filename

    try:
        urllib.request.urlretrieve(imageurl, filepath)
        return True
    except urllib.error.HTTPError as exc:
        print("An error occurred: " + str(exc))
        return False


# debugging
if __name__ == "__main__":
    img_url = get_image_url("Thanksgiving")
    print(img_url)
    save_image(img_url)