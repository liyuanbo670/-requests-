import requests
from lxml import etree
url = "http://www.xbiquge.la/13/13959/" # 设置初始url
response = requests.get(url) # 通过requests.get方法获取原网页
print(type(response))
html = etree.HTML(response.content) # 通过lxml构建html对象
# 使用xpath语法从html中提取各章节url，他不是一个完整的url而是残缺的
a_lst = html.xpath(".//div[@id='list']/dl/dd/a/@href")
url_lst = [] # 创建新的url列表
i = 0 # 设置初始循环值，主要在循环中指示下载了多少章节内容
# 从a_lst中循环取残缺的url
for a in a_lst:
    # 将残缺的url补充问完整的url并添加到url_lst中，完整的url是每一章节的详细地址
    url_lst.append("http://www.xbiquge.la"+a)
# 循环爬取所有完整url页面的祥细信息
for detial_url in url_lst:
    # 获取祥情页面
    r1 = requests.get(detial_url)
    # 设置html对象
    h1 = etree.HTML(r1.content)
    # 利用xpath获取章节题目标签
    title = h1.xpath(".//div[@class='bookname']/h1/text()")
    # 将title转换为字符串数据类型
    title_str = "".join(title)
    # 获取正文内容
    content = h1.xpath(".//div[@id='content']/text()")
    # 讲正文转换为字符串内容
    content_str = "".join(content)
    # 按章节写入文件，每个文件的文件名是章节名
    with open(title_str+".txt","a",encoding="utf8") as f:
        f.write(title_str+"\n"+content_str)
        f.flush()
        f.close()
        # 提示下载了多少章节
        i+=1
        print("下载了%s章"%i)


