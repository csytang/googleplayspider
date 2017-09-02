# Google-PlaySpider Tool
# Project: 
  * This tool is under __RGC project__ with Hong Kong Government;
  * The tool will download the App information from Google Play. 
  
# HowTo:
  To run this tool, please use following command:
  ```
  scrapy crawl GooglePlaySpider
  ```
  under any folder of this project.
  
# Environment:
  The project is developed under following environment:
  * Python 3.4
  * sqlite
  * [Scrapy framework](https://scrapy.org)]
  * Mac OSX (10.12)
  The tool should be compatiable with other platform, but not fully tested.
  
# Project Host Page:
  For more information, please visit our project host page at:[RGC-project](http://www.chrisyttang.org/android-instant-app/index.html)
  ## The data structure:
Following data are explored and extracted from Google Play,
1. Link;
2. Name;
3. Late Update;
4. Author;
5. Size;
6. Total Downloads
7. Version;
8. Compatibility;
9. Content Rating;
10. Author Link;
11. Genre;
12. Price;
13. Rating Value;
14. Total Reviews;
15. Description;
16. IAP;
17. Developer Badge;
18. Physical Address
19. Video URL;
20. Developer ID;
 ## Output
 The output will be redirect to the sqlite DB named ```googleplay.db```

  
# Team:
   For help, please contact:
   * __Yutian Tang__  via e-mail chris.yttang@hotmail.com
   
