#Postcard Mashup

## Description

This app queries several APIs using a keyword search, and generates a postcard based on the results returned.  The postcard has a picture result on the front, along with the keyword used for the search.  On the back are a snippet from a Wikipedia article and a Twitter tweet.

The data needed to build each postcard are saved to a sqlite3 database so the various postcards can be viewed by other visitors to the site.

## Requirements

* Two modules not in the standard Python library are required to run the application: _wikipedia_, and _tweepy_.  We have found it helpful to invoke python3 directly when loading the application after the modules have been installed; your mileage may vary.
* You will also need your own set of API keys for Pixabay and Twitter.  For security reasons, we are not sharing our keys in this repository.  Your keys should be stored in the APItools directory in a file called APIkeys.py.  The _pixabaykey_ variable should store the Pixabay API key as a string.  The _twitter_keys_ variable should store the various Twitter APIkeys as KEYNAME:value pairs in a dictionary.

## Known issues/bugs

* Audio playback is dependent on the particular combination of OS and browser in use by the end user.  (MP3 vs OGG format is one we know about for sure.)  Future sprints would attempt to tailor file format to the user's OS+browser combination.
* The URLs returned by pixabay are short-lived addresses and those images may not be retrievable via URL after a few days.  Future sprints would download and store the images and save the filename in the database.
* Diagnose and fix the issues with CSS - we get different results across different computers and across different browsers in the same computer.