import os

htmldir= "Html"
tempdir= "TemplateData"
tempfiles= os.listdir(tempdir)
templatefile=open("template.html","r")
template = templatefile.read()
templatefile.close()
print template

for item in tempfiles:
    direc1=os.path.join("TemplateData", item)
    item = item[:-4]
    tempdatafile=open(direc1,"r")
    tempdata = tempdatafile.read()
    tempdatafile.close()
    item+=".html"
    htmlfiledir=os.path.join("HTML",item)
    htmlfile=open(htmlfiledir, "w")
    htmlfile.write(template.replace("%%content%%", tempdata))
    htmlfile.close()
    
