htmlStr = """
  <div class="img">
    <a target="_blank" href="http://bing.com/az/hprichbg/rb/RedSeaWhip_EN-US9130505730_1366x768.jpg">
      <img src="http://bing.com/az/hprichbg/rb/RedSeaWhip_EN-US9130505730_1366x768.jpg" alt="img" width="300" height="200">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
"""

f = open("/Users/omart/Desktop/Python_Programs/bingScript/bingCode.txt", "r")
htmlFile = open("/Users/omart/Desktop/Python_Programs/bingScript/bingPics.html", "w")
for line in f:
    if "<body>" in line:
        htmlFile.write(line)
        htmlFile.write(htmlStr)
    else:
        htmlFile.write(line)
f.close()
htmlFile.close()

f = open("/Users/omart/Desktop/Python_Programs/bingScript/bingCode.txt", "w")
htmlFile = open("/Users/omart/Desktop/Python_Programs/bingScript/bingPics.html", "r")
for line in htmlFile:
    f.write(line)
f.close()
htmlFile.close()



'''
f = open("/Users/omart/Desktop/Python_Programs/bingScript/bingCode.txt", "r")
htmlFile = open("/Users/omart/Desktop/Python_Programs/bingScript/bingPics.html", "w")
for line in f:
    if "<div class=" in line:
        htmlFile.write(htmlStr)
    htmlFile.write(line)
f.close()
htmlFile.close()
'''
