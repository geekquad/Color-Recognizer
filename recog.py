#importing necessary libraries
import numpy as np
import pandas as pd
import cv2

#loading the image
img = cv2.imread("img/sample_1.jpg")

#teaching the colors
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


clicked = False
r = g = b = xpos = ypos = 0

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
