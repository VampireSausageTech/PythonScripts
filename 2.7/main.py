import os


tempdir=os.path.join("C:","Users","admin","Desktop", "imscared", "Enter a great place")
tempdir= r"C:Users\admin\Desktop\imscared\Enter a great place"
print tempdir
tempfiles= os.listdir(tempdir)



for item in tempfiles:
    direc1=os.path.join(tempdir, item)
    #item = item[:-4]
    tempdatafile=open(direc1,"r")
    tempdata = tempdatafile.read()
    tempdatafile.close()
    print tempdata
##    item+=".html"
##    htmlfiledir=os.path.join("HTML",item)
##    htmlfile=open(htmlfiledir, "w")
##    htmlfile.write(template.replace("%%content%%", tempdata))
##    htmlfile.close()
##    
