# -*coding:utf-8*-
import re
import requests
from pyquery import PyQuery as pq


#main函数，分别解析每个页面
def main(offset):
    url = 'http://jinyongxiaoshuo.com/old_yitiantulongji/'+str(offset)+'.html'
    headers={
            'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    html=requests.get(url,headers=headers)
    html.encoding = "utf-8"
    #print(html.encoding)
    doc=pq(html.text)
    title = doc('h1')
    paper =doc('p')
    #print(paper)
    write_to_file_tittle(title.text())
    #listpaper=doc('p')
    #print(paper.text())
    paperlist=paper.items()
    #print(paperlist)
    #print(type(paperlist))
    list1=list(paperlist)
    #print(type(list1))
    for j in range(4):
        list1.pop()
        #print(list1.pop())
   
    for i in list1:
        write_to_file_paper(i.text())
    #print(type(paper))
    #print(title)


#向文件中写入章节标题
def write_to_file_tittle(title):
    with open (r'C:\Users\zhoul\Desktop\yitiantulongji.txt','a',encoding = 'utf-8') as f:
        f.write('\n\n\n\n\n\n')
        f.write(title+'\n')
        f.write('==================================='+'\n\n')

#向文件中写入章节段落
def write_to_file_paper(paper):
    with open (r'C:\Users\zhoul\Desktop\yitiantulongji.txt','a',encoding = 'utf-8') as f:
        f.write('      ')
        f.write(paper+'\n')

        
#遍历所有的页面
if __name__=='__main__':
    for i in range(1103,990,-1):
        print(i)
        main(i);
