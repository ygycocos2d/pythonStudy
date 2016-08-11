#coding=utf-8
import urllib
import urllib2
import re

def getHTML(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getHTML2(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
    headers = { 'User-Agent' : user_agent } 
    page = urllib2.urlopen(url,headers)
    html = page.read()
    return html

def getHTML3(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}  
    req = urllib2.Request(url=url,headers=headers)  
    page = urllib2.urlopen(req)  
    html = page.read()  
    page.close()
    return html
    
def getXiaoHua(html):
    pattern = '''<div\sclass="article\sblock\suntagged\smb15"\sid='qiushi_tag_\d+'> # 这里匹配开头
                     .*?                         # 这里匹配开头到段子前标记之间的内容，注意要用非贪婪匹配?
                     <div\sclass="content">\\n*  # 这里是段子开始的标记，包括段子前的空行
                     ([^(?:</div>)]*?)           # 这里是段子内容，最外边的括号是分组，里边的只是整体作用
                     \\n*</div>                  # 这里是段子结束的标记，包括段子后的空行
                     \\n*
                     <div\sclass="stats">        # 只匹配不含图片的段子。
        '''
    reg = '<div class="content">\\n*(.*)\\n*</div>'
    #reg = '<div\sclass="content">\\n*(.*?)\\n*</div>'
    myItems = re.findall(reg,html)
    file_object = open("xiaohua.txt", 'w+')
    for x in myItems:
        x = x.replace("\s","")
        x = x.replace("<br/>","\n")+"\n"
        print x
        file_object.write(x)
    file_object.close()


def write2file(path,txt):
    file_object = open(path, 'w+')
    file_object.write(txt)
    file_object.close()
    
def getImg(html):
    reg = '<img src="(.+?\.jpg|.+?\.png)"'
    imglist = re.findall(reg,html)
    x = 0
    for imgurl in imglist:
        print x
        try: 
            urllib.urlretrieve(imgurl,'%s.jpg' % x)
        except Exception,e:
            print e
        x+=1
def getXiaoHua2file(fileObj,html):
    reg = '<div class="content">\\n*(.*)\\n*</div>'
    myItems = re.findall(reg,html)
    for x in myItems:
        x = x.replace("\s","")
        x = x.replace("<br/>","\n")+"\n"
        print x
        fileObj.write(x)

fileObj = open("xiaohua.txt", 'w+')
for i in range(1,10):
    try:
        url = "http://www.qiushibaike.com/hot/page/"+str(i)
        html = getHTML3(url)
        #print html
        #getXiaoHua(html)
        getXiaoHua2file(fileObj,html)
    except Exception,e:
        print "--------------------------------------",e

fileObj.close()

#html = getHTML3("http://www.danlu.com/main/index.html")
#print html
#getImg(html)
