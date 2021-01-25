import os
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False, help="Input URL")

args = vars(ap.parse_args())
input_url = args["url"]  
path = ""

def write_log_to_file(text):
    f = open(path+'Note.txt', 'a')
    f.write(str(text) + '\n')
    
def save_img(url):
    global path
    save_pic = 1
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find(id='initialTouch').findChildren('img')
    title_final =  soup.find('div', {"class": "buy-content-title-name"}).text

    if not os.path.isdir(title_final):os.mkdir(title_final)
    path = os.getcwd() + '\\' + str(title_final) + '\\'    
    
    # save image 
    for img in images:
        t = img.get('src')
        urllib.request.urlretrieve(t,path + str(save_pic)+'_save.jpg') 
        save_pic+=1

def information():
    global path
    information = []
    r = requests.get(input_url, headers={'User-Agent': 'Custom'})
    soup_info = BeautifulSoup(r.text, 'html.parser')
    
    # Title information
    for info1 in soup_info.findAll('div', {"class": "buy-content-cell"}):
        for title in info1.findAll('div', {"class": "buy-content-cell-title"}):
            for info2 in info1.findAll('div', {"class": "buy-content-cell-body"}):
                write_log_to_file("%s : %s" %(title.text,info2.text))
    
    # Information2
    for test1 in soup_info.findAll('div', {"class": "buy-content-body d-lg-none d-block"}):
        for test in test1.findAll('div', {"class": "buy-content-basic-cell"}):
            write_log_to_file(test.text)
    
if __name__ == '__main__':
    
    save_img(input_url)
    information()