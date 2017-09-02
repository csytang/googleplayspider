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
        self.cur.execute('DROP TABLE IF EXISTS googleplay')

        '''
         Link; Item_name; Updated;
         Author; Filesize; Downloads;
         Version; Compatibility; Content_rating ;
         Author_link; Genre; Price;
         Rating_value; Review_number; Description ;
         IAP; Developer_badge; Physical_address;
         Video_URL;Developer_ID ;
        '''
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS" + " googleplay(link VARCHAR(100),item_name VARCHAR(50),"+
            "last_update VARCHAR(50),author VARCHAR(30), filesize VARCHAR(30), downloads VARCHAR(50),"+
            "version VARCHAR(30),  compatibility VARCHAR(50), content_rating VARCHAR(30),"+
            "author_link VARCHAR(100),  genre VARCHAR(50), price VARCHAR(30),"+
            "rating VARCHAR(20), review_number VARCHAR(30),description VARCHAR(300),"+
            "iap VARCHAR(50), developer_badge VARCHAR(50),physicaladdr VARCHAR(100),"+
            "video_url VARCHAR(50),developer_id VARCHAR(50))"
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
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'INSERT INTO googleplay({}) values({})'
        self.cur.execute(sql.format(col, placeholders), item.values())
        self.con.commit()

        # json
        line = json.dumps(dict(item), ensure_ascii=False, encoding='utf8', indent=4) + ','
        with open(fileName, 'a') as f:
            f.write(line.encode('utf8'))
        return item
