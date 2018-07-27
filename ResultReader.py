import json
import io
import math
from PIL import Image, ImageDraw, ImageFont
import Geometrics
f = open('test1_keypoints.json')
result = json.load(f)

def drawTextAndPoint(features, featureName, imgDraw):
    f = features[featureName]
    x = f["x"]
    y = f["y"]
    r = 20 
    imgDraw.ellipse((x, y, x+r, y+r), fill=(255,0,0,128))
    imgDraw.text((x, y), featureName, fill=(255,255,255,255))

if(len(result["people"]) > 1):
    print("Warning: more than one person right now is not supported.")

targetPerson = result["people"][0]
targetKeyPoints = targetPerson["pose_keypoints_2d"]

featureF = open('featureList.txt')
featureNameList = []
for line in featureF:
    feature = line[line.find(',')+3:line.find('}')-1]
    featureNameList.append(feature)

i = 0

features = {}

base = Image.open('./push-ups/test1.jpeg').convert('RGBA')
overLay = Image.new('RGBA', base.size, (255,255,255,0))
overLayDraw = ImageDraw.Draw(overLay)

for name in featureNameList:
    x = targetKeyPoints[i]
    y = targetKeyPoints[i+1]
    confidence = targetKeyPoints[i+2]
    i = i + 3
    features[name] = {"x":x,"y":y, "confidence":confidence}


drawTextAndPoint(features, "RHip", overLayDraw)

drawTextAndPoint(features, "LHip", overLayDraw)

drawTextAndPoint(features, "LAnkle", overLayDraw)

drawTextAndPoint(features, "RAnkle", overLayDraw)

drawTextAndPoint(features, "Neck", overLayDraw)

NeckHipV = [features["Neck"]["x"]- features["RHip"]["x"], features["Neck"]["y"]- features["RHip"]["y"]]
HipAnkleV = [features["RHip"]["x"]- features["RAnkle"]["x"], features["RHip"]["y"]- features["RAnkle"]["y"]]

poseAngle = math.degrees(Geometrics.angle(NeckHipV, HipAnkleV))

if(poseAngle>90):
    poseAngle = 180 - poseAngle

print(poseAngle)

if(poseAngle>10):
    print("Hip is too high")

out = Image.alpha_composite(base, overLay)

out.show()
