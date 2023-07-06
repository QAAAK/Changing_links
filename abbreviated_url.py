
import pyshorteners


def URL():
    s_url = pyshorteners.Shortener
    url = input('Enter URL: ')
    url_new = s_url.tinyurl.short(url)
    return url_new




