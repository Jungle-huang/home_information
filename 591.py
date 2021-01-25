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
    f = open(path+'test.txt', 'a',encoding="utf-8")
    f.write(str(text) + '\n')
    f.close

def save_img(url):
    global path
    save_pic = 1
    r = requests.get(url, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find('div', {"class": "house-pic-box"}).findChildren('img')
    title =  soup.find('div', {"class": "detail-title-container"}).findChildren('h1')
    
    for titles in title:
        title_final = titles.text.replace("\n", "").strip().replace("/","")

    if not os.path.isdir(title_final):os.mkdir(title_final)
    path = os.getcwd() + '\\' + str(title_final) + '\\'

    # save image 
    for img in images:
        t = img.get('data-original')
        urllib.request.urlretrieve(t,path + str(save_pic)+'_save.jpg') 
        save_pic+=1

def information():
    global path

    r = requests.get(input_url, headers={'User-Agent': 'Custom'})
    soup_info = BeautifulSoup(r.text, 'html.parser')
    info = (soup_info.find('div', {"class": "info-box"}).text).replace(" ","")
    write_log_to_file(str(info))

def define_document():
    global path
    
    file_ = path+'test.txt'
    file_p = path+'Note.txt'
    file2 = open(file_p, "a",encoding="utf-8")
    
    
    with open(file_, "r",encoding="utf-8") as r_file:
        for line in r_file.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
        
    file2.close
    r_file.close
    os.remove(file_)

    
if __name__ == '__main__':
    
    save_img(input_url)
    information()
    define_document()









    
# def get_object():
    # url = "https://sale.591.com.tw/?shType=list&price=$_600$&regionid=4&order=posttime_desc"
    # # url = 'https://sale.591.com.tw/'
    # r = requests.get(url, headers={'User-Agent': 'Custom'})
    # soup = BeautifulSoup(r.text, 'html.parser')
    
    # object = soup.find('script', type="text/javascript")
    # # .findChildren('href')
    # print(object)
    
    # text = r.text.encode('UTF-8')
    # f = open('123.txt', 'a')
    # f.write(str(text))
    # f.close

# my request
# https://sale.591.com.tw/?shType=list&price=$_600$&regionid=4&order=posttime_desc