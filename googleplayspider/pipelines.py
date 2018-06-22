# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3

fileName = 'googleplay.json'
db = 'googleplay.db'

class GoogleplayspiderPipeline(object):

    '''
    The item will be returned here, and then, we will
    store the returned item into database
    Link;
    Item_name;
    Updated;
    Author;
    Filesize;
    Downloads;
    Version ;
    Compatibility ;
    Content_rating ;
    Author_link ;
    Genre ;
    Price ;
    Rating_value ;
    Review_number ;
    Description ;
    IAP ;
    Developer_badge ;
    Physical_address ;
    Video_URL ;
    Developer_ID ;


    '''

    def __init__(self):
        # json
        with open(fileName, 'w') as f:
            f.write('[\n')

    def open_spider(self, spider):
        # sqlite
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.con.text_factory = str
        self.cur.execute('DROP TABLE IF EXISTS googleplay')

        '''
         Link; Item_name; Updated;
         Author; Filesize; Downloads;
         Version; Compatibility; Content_rating ;
         Author_link; Privacy_link;Genre;
         Price; Rating_value; Review_number;
         Description ;
         IAP; Developer_badge; Physical_address;
         Video_URL;Developer_ID ;
        '''
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS" + " googleplay(Link VARCHAR(100),Item_name VARCHAR(50), "+
            "Last_Updated VARCHAR(50), Filesize VARCHAR(30), Downloads VARCHAR(50),"+
            "Version VARCHAR(30), Operation_system VARCHAR(50), Content_rating VARCHAR(30),"+
            "Genre VARCHAR(50),"+
            "Review_number VARCHAR(30),"+
            "Description VARCHAR(50000))"
        )



    def close_spider(self, spider):
        # sqlite
        self.con.commit()
        self.con.close()

        # json
        with open(fileName, 'r') as f:
            content = f.read()
        with open(fileName, 'w') as f:
            f.write(content[:-1] + "\n]")

    def process_item(self, item, spider):
        # sqlite
        if str(item['Link']).find('details?id') != - 1:
            col = ','.join(item.keys())
            placeholders = ','.join(len(item) * '?')
            print('insert new value:'+item['Link'])
            sql = 'INSERT INTO googleplay({}) values({})'
            #self.cur.execute(sql.format(col, placeholders), item.values())
            self.cur.execute("INSERT INTO googleplay(Link,Item_name,Last_Updated,"
                             "Filesize,Downloads,Version,Operation_system,"
                             "Content_rating,Genre,Review_number,"
                             "Description)"
                             "values(?,?,"
                             "?,?,?,?,"
                             "?,?,?,?,?)",
                             (item['Link'],item['Item_name'],item['Last_Updated']
                              ,item['Filesize'],item['Downloads'],item['Version'],item['Operation_system'],
                              item['Content_rating'],
                              item['Genre'],
                              item['Review_number'],item['Description']))
            self.con.commit()

            # json
            line = json.dumps(dict(item), ensure_ascii=True, encoding='utf8', indent=4) + ','
            with open(fileName, 'a') as f:
                 f.write(line)
        return item
