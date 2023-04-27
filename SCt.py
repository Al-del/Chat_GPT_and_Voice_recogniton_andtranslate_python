import csv
import re
from pandas import *
import speech_recognition as sr
from picamera import PiCamera
import cv2
from skimage.metrics import structural_similarity
from time import sleep
import os
import serial
import time
import serial
import time
from aa import ley
from test import take_photo
from talk import talk_what_we_need
r = sr.Recognizer()
#ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
#ser.setDTR(False)
#time.sleep(1)
#ser.flushInput()
#ser.setDTR(True)

def search_the_thing(the_item_we_search,sthing):
	with open('DB.csv') as csv_file:
		data = read_csv("DB.csv")
		name=data['nume'].tolist()
		mod=data['model'].tolist()
		if(the_item_we_search==name[0]):  
			print("Passed first barrier")
			if(sthing==mod[0]): 
				print("Passed second barrier")
				ley()
		if(the_item_we_search==name[1]):
			if(sthing==mod[1]):
				ley()
def record():
    with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    return audio
def take_foto(nume_poza):
    camera=PiCamera()
    camera.start_preview()
    camera.capture(nume_poza+".jpg")
    sleep(2)
    camera.stop_preview()
def compare_two_photos():
        take_photo("try")
        with open('DB.csv') as csv_file:
                data = read_csv("DB.csv")
                name=data['nume'].tolist()
               # for i in range(0,len(name)):
                if(orb_sim(cv2.imread("creion.jpg"),cv2.imread("try.jpg")<30)):
                        ley()
                        os.remove("try.jpg")
def mai_n():
	 b audio_=record()
	your_words_is=r.recognize_google(audio_,language="ro")
	res = re.findall(r'\w+', your_words_is)  
	if(res[0]=="add"):
            add_data( res[1] , res[2] , res[3],res[4])
            take_foto(res[1])
	elif (res[0]=="search"):
		search_the_thing(res[1],res[2])
	elif (res[0]=="photo"):
            compare_two_photos()
	else:
			talk_what_we_need("I don't know this command")
	 
def add_data(a,b,c,d):
	with open("DB.csv",mode="w",encoding="utf8") as csvfile:
		field_names=["nume","model","masa","RFID"]
		writer=csv.DictWriter(csvfile,fieldnames=field_names)
		writer.writeheader()
		data={"name":a,"model":b,"mass":c,"RFID":d}
		writer.writerow(data)
def orb_sim(img1,img2):
    orb=cv2.ORB_create()
    kp_a,desc_a=orb.detectAndCompute(img1,None)
    kp_b,desc_b=orb.detectAndCompute(img2,None)
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(desc_a,desc_b)
    similar_regions=[i for i in matches if i.distance<50]
    if len(matches)==0:
        return 0
    return len(similar_regions)/len(matches)

mai_n()
