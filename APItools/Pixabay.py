'''
This will eventually hold code that returns a url to an image on Pixabay.
'''
import requests # http://docs.python-requests.org/en/master/
import json
import random

def get_image_url(search_for="Thanksgiving"):
    '''
    Requests a bunch of images from Pixabay API and picks a random image from the results.
    :param search_for:
    :return: url as string if successful, None if no results found
    '''

    from APItools.APIkeys import pixabaykey # NB: APIkeys is not shared with repo to protect key integrity
    search_url = "https://pixabay.com/api"
    apiparms = {
        'key': pixabaykey,
        'q': search_for
    }

    # request data from Pixabay API
    response = requests.get(search_url,params=apiparms).json()
    hits = response['hits']
    hitcount = len(hits)
    if hitcount > 0 :
        # if data is returned, pick a random hit and return the image url found in the selected hit
        selected_index = random.randint(0,hitcount)
        # print(selected_index)
        # print(hits[selected_index]['previewURL'])
        return hits[selected_index]['previewURL']
    else:
        # if no results found, return None so code can inspect for that.
        return None

# debugging
if (__name__ == "__main__"):
    img_url = get_image_url()
    print(img_url)