# Google-PlaySpider Tool
## Project 
  * This tool is under __RGC project__ with Hong Kong Government;
  * The tool will download the App information from Google Play. 
  
## HowTo
  To run this tool, please use following command:
  ```
  scrapy crawl GooglePlaySpider
  ```
  under any folder of this project.
  
## Environment
  The project is developed under following environment:
  
  * Python 3.4
  * sqlite
  * [Scrapy framework](https://scrapy.org)
  * OS: Windows, MacOS, Linux.
   
The tool should be compatiable with other platform, but not fully tested.
  
## Project Host Page
  For more information, please visit our project host page at:[RGC-project-Android](http://www.chrisyttang.org/android-instant-app/index.html)
  
## The Data Structure for Data Extracted:
Following data are explored and extracted from Google Play,

1. Link;
2. Name;
3. Late Update;
4. Author;
5. Size;
6. Total Downloads
7. Version;
8. Operation System Supported (Android level);
9. Content Rating(e.g. 7 years old or above);
10. Author Link;
11. Privacy Policy Link (if any);
12. Genre(Categories);
13. Price;
14. App Rating Value;
15. Number of Reviews;
16. Description;
17. IAP(In-app purchase);
18. Developer Badge;
19. Physical Address
20. Video URL;
21. Developer ID;

## Output
The output will be redirect to the sqlite DB named ```googleplay.db```, which could be found under the root of this diretory.
  
## TODO List and ChangeLog

TODO list for new features：[ToDo](./TODO.md)
Change log：[changelog](./changelog.md)
  
## Developer
For help, please contact __Yutian Tang__  via e-mail chris.yttang(AT)hotmail.com or create a new issue with the issue tracker.
  

---
# Google Play爬虫工具（Intro. in simplified Chinese）

## 如何使用
* 首先请下载本项目到本地
* 在项目的根目录下运行命令```scrapy crawl GooglePlaySpider``` 即启动项目

## 环境
本应用程序需要以下运行环境：

  * Python 3.4
  * sqlite
  * [Scrapy 框架](https://scrapy.org)
  * 操作系统：Window，MacOS，Linux.
  
本工具在其他运行环境中也可能正常使用，但是并没有被完全测试。

## 项目主页
  如需获得其他的技术支持及了解更多详情，请访问我们的项目主页:[RGC-project-Android](http://www.chrisyttang.org/android-instant-app/index.html)
  
## 抽取数据的数据结构:
我们从Google Play上抽取有关App的以下信息

1. App的链接;
2. App名称;
3. App最后更新时间;
4. App发布者;
5. App大小;
6. App下载总量；
7. App版本号;
8. App所支持的操作系统 (即Android 版本号);
9. App内容分级（如 7岁或以上）;
10. App的作者链接;
11. App的隐私策略链接 (如果开发者提供的话);
12. App所属的类别（如 动作类）;
13. App价格;
14. App评分;
15. 评论的总个数;
16. App介绍;
17. 是否提供应用程序内购买;
18. 开发者徽章;
19. 开发者的地址;
20. App的介绍视频链接;
21. 开发者ID;

## 结果输出
结果将被存储在一个sqlite数据库中，名称为```googleplay.db```。可以在本项目的根目录下找到。

## 待添加的新功能及版本变更日志
待开发新功能：[ToDo](./TODO.md)
版本变更日志：[changelog](./changelog.md)



## 开发人员
 如需帮助请联系: __Yutian Tang__  通过邮件 e-mail chris.yttang(AT)hotmail.com 或 在Github中创建一个新的Issue。 
