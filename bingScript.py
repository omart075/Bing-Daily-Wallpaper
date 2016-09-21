import urllib
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from subprocess import call
import os
import datetime

#takes in getUrl method to open picture as url as save it as jpg
def getImage(url):
    name = "/Users/omart/Desktop/Python_Programs/bingScript/bing.jpg"
    urllib.urlretrieve(url, name)

#gets url of Bing's XML file for their wallpaper, gets the name
#of the picture for notification and returns url of the picture
def getURL():
    name = "/Users/omart/Desktop/Python_Programs/bingScript/bing.xml"
    urllib.urlretrieve("http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US", name)
    xmlPath = "/Users/omart/Desktop/Python_Programs/bingScript/bing.xml"
    parseFile = ET.parse(xmlPath)
    url = parseFile.getroot()
    global fullURL
    fullURL = "http://bing.com" + url[0][3].text
    global notification
    notification = (url[0][5].text)
    return fullURL

#sets the wallpaper through an os command
def setWallpaper():
    #os.system("defaults write com.apple.desktop Background '{default = {ImageFilePath = \"/Users/omart/Desktop/Python_Programs/bingScript/bing.jpg\"; };}'")
    os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"/Users/omart/Desktop/Python_Programs/bingScript/bing.jpg\"'")
    call(["killall", "Dock"])

#formats the information of the picture as preferred
def word(notification):
    splitWord = notification.split("(")
    return splitWord[0]

#displays information of picture as a notification
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s])))

#gets the date in mm/dd/yyyy format
def date():
    now = datetime.datetime.now()

    month = now.month
    x = str(month)

    day = now.day
    y = str(day)

    year = now.year
    z = str(year)

    finalDate = x + "/" + y + "/" + z + " - "
    return finalDate

#write info of the picture onto the picture
def writeToImage():
    img = Image.open("/Users/omart/Desktop/Python_Programs/bingScript/bing.jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("/Users/omart/Desktop/Python_Programs/bingScript/Fonts/Helvetica.ttf", 18)
    text = word(notification)
    w, h = font.getsize(text)
    imgWidth, imgHeight = img.size
    x = (imgWidth/2)-(w/2)
    y = imgHeight-19
    x, y = (x, y)
    draw.rectangle((x, y, x+w, y+h), fill='black')
    draw.text((x,y), text, fill = (209,239,8), font=font)
    draw = ImageDraw.Draw(img)
    img.save("/Users/omart/Desktop/Python_Programs/bingScript/bing.jpg")

#opens a file and prints date and picture information
def writeFile():
    f = open('/Users/omart/Desktop/Python_Programs/bingScript/pictures.txt', 'a')
    f.write(date() + word(notification))
    f.write("\n")
    f.close()

#save image of the day to a website
def website(picHtml, picInfo):
    #html needed to add a new picture to the website
    htmlStr = """
      <div class="img">
        <a target="_blank" href=" """ + picHtml + """ ">
          <img src=" """ + picHtml + """ " alt="img" width="300" height="200">
        </a>
        <div class="desc"> """ + picInfo + """</div>
      </div>
    """

    #reads txt file to write new image to html
    f = open("/Users/omart/Desktop/Python_Programs/bingScript/bingCode.txt", "r")
    htmlFile = open("/Users/omart/Desktop/Python_Programs/bingScript/omart075.github.io/index.html", "w")
    for line in f:
        if "<body>" in line:
            htmlFile.write(line)
            htmlFile.write(htmlStr)
        else:
            htmlFile.write(line)
    f.close()
    htmlFile.close()

    #reads html to write updated html to txt file so it is not lost
    f = open("/Users/omart/Desktop/Python_Programs/bingScript/bingCode.txt", "w")
    htmlFile = open("/Users/omart/Desktop/Python_Programs/bingScript/omart075.github.io/index.html", "r")
    for line in htmlFile:
        f.write(line)
    f.close()
    htmlFile.close()

    #UNIX commands to push changes onto github and update website
    os.chdir("/Users/omart/Desktop/Python_Programs/bingScript/omart075.github.io")
    call(["git", "add", "--a"])
    call(["git", "commit", "-m", "\"Commit\""])
    call(["git", "push", "-u", "origin", "master"])


#checks if there is a connection to wifi in order to process code
connected = False
while connected == False:
    try:
        #opens terminal in order to create notification and then makes notification
        #terminalPath = "/Applications/Utilities/Terminal.app"
        #os.system("open " + terminalPath)
        getImage(getURL())
        writeToImage()
        setWallpaper()
        website(fullURL, word(notification))
        connected = True
    except:
        pass

print "haaaan"

#opens terminal in order to create notification and then makes notification
#terminalPath = "/Applications/Utilities/Terminal.app"
#os.system("open " + terminalPath)
'''
#sends notification with picture info. Issues with osx 10.11.5
notify(title = 'Bing Image Description',
subtitle = '',
message = word(notification))
'''
