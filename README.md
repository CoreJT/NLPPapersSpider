# NLPPapersSpider
在日常的科研生活中，不可避免地需要大量查找和阅读相关领域的文献来寻找idea，如何高效并大规模地搜集相关领域的科研文献至关重要，为了避免额外的人力、节约时间，加之博主是做自然语言处理的，所以这款NLP论文爬取系统应用而生，他可以自动地对满足要求的文献进行爬取，并保存在本地指定位置。相比于人工输入关键词检索，对检索结果逐个点击下载；这个自动化工具，可以帮我们省掉一些费时费力的重复操作，我们完全可以在此期间作其他事情，过一段时间直接查看爬取结果就OK了.

该NLP论文爬取系统基于dblp，一个计算机领域的文献数据库。大体原理如下：

1）构造dblp查询url(包含文献关键词、会议名称、年份等信息)，爬取该url对应的页面，并解析出每篇论文的页面url。

2）对每篇论文url对应的页面进行爬取，并解析出每篇论文的pdf对应的下载链接。

3）爬取每篇论文pdf，并保存在本地的指定位置。

目前该NLP论文爬取系统支持NLP全系列会议论文的爬取(包括 ACL、EMNLP、COLING、NAACL、EACL、CoNLL等)以及AAAI和IJCAI会议论文的爬取。该系统的原理和实现细节以及项目文件组织方式可以查看我的博客专栏：https://blog.csdn.net/sdu_hao/category_9626671.html


# 使用方式
1）打开命令行，进入spider.py文件所在的路径下。

2）执行以下命令：

python spider.py spider  #此时将使用config.py中的默认配置

可以在config.py中修改配置，再次运行上面的命令。也可以在命令行传入新的参数对其进行覆盖：

#爬取ACL系列会议论文(ACL、EMNLP、COLING、NAACL、EACL、CoNLL等等) 

#爬取ACL

python spider.py spider --spiderTool='ACLSeries' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='ACL' --path='/Users/apple/Desktop' 

#爬取EMNLP

python spider.py spider --spiderTool='ACLSeries' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='EMNLP' --path='/Users/apple/Desktop' 
 
#爬取AAAI会议论文

python spider.py spider --spiderTool='AAAI' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='AAAI' --path='/Users/apple/Desktop' 
 
 
#爬取IJCAI会议论文

python spider.py spider --spiderTool='IJCAI' --Keywords=['dialog','conversation','chatbot'] --Years=[2016,2017,2018,2019] --Field='对话' --Meeting='IJCAI' --path='/Users/apple/Desktop' 









