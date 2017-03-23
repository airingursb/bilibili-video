# -*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
import sys
import re
import json
import MySQLdb

reload(sys)

sys.setdefaultencoding('utf-8')

# id av cid title tminfo time click danmu coins favourites duration honor_click honor_coins honor_favourites
# mid name article fans tags[3] common

urls = []

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

time1 = time.time()

for i in range(17501, 100000):
    url = 'http://bilibili.com/video/av' + str(i)
    urls.append(url)


def spider(url):
    html = requests.get(url, headers=head)
    selector = etree.HTML(html.text)
    content = selector.xpath("//html")
    for each in content:
        title = each.xpath('//div[@class="v-title"]/h1/@title')
        if title:
            av = url.replace("http://bilibili.com/video/av", "")
            title = title[0]
            tminfo1_log = each.xpath('//div[@class="tminfo"]/a/text()')
            tminfo2_log = each.xpath('//div[@class="tminfo"]/span[1]/a/text()')
            tminfo3_log = each.xpath('//div[@class="tminfo"]/span[2]/a/text()')
            if tminfo1_log:
                tminfo1 = tminfo1_log[0]
            else:
                tminfo1 = ""
            if tminfo2_log:
                tminfo2 = tminfo2_log[0]
            else:
                tminfo2 = ""
            if tminfo3_log:
                tminfo3 = tminfo3_log[0]
            else:
                tminfo3 = ""
            tminfo = tminfo1 + '-' + tminfo2 + '-' + tminfo3
            time_log = each.xpath('//div[@class="tminfo"]/time/i/text()')
            mid_log = each.xpath('//div[@class="b-btn f hide"]/@mid')
            name_log = each.xpath('//div[@class="usname"]/a/@title')
            article_log = each.xpath('//div[@class="up-video-message"]/div[1]/text()')
            fans_log = each.xpath('//div[@class="up-video-message"]/div[2]/text()')

            if time_log:
                time = time_log[0]
            else:
                time = ""
            if mid_log:
                mid = mid_log[0]
            else:
                mid = ""
            if name_log:
                name = name_log[0]
            else:
                name = ""
            if article_log:
                article = article_log[0].replace(u"投稿：","")
            else:
                article = "-1"
            if fans_log:
                fans = fans_log[0].replace(u"粉丝：","")
            else:
                fans = "-1"

            tag1_log = each.xpath('//ul[@class="tag-list"]/li[1]/a/text()')
            tag2_log = each.xpath('//ul[@class="tag-list"]/li[2]/a/text()')
            tag3_log = each.xpath('//ul[@class="tag-list"]/li[3]/a/text()')
            if tag1_log:
                tag1 = tag1_log[0]
            else:
                tag1 = ""
            if tag2_log:
                tag2 = tag2_log[0]
            else:
                tag2 = ""
            if tag3_log:
                tag3 = tag3_log[0]
            else:
                tag3 = ""

            cid_html_1 = each.xpath('//div[@class="scontent"]/iframe/@src')
            cid_html_2 = each.xpath('//div[@class="scontent"]/script/text()')
            if cid_html_1 or cid_html_2:
                if cid_html_1:
                    cid_html = cid_html_1[0]
                else:
                    cid_html = cid_html_2[0]

                cids = re.findall(r'cid=.+&aid', cid_html)
                cid = cids[0].replace("cid=", "").replace("&aid", "")
                info_url = "http://interface.bilibili.com/player?id=cid:" + str(cid) + "&aid=" + av
                video_info = requests.get(info_url)
                video_selector = etree.HTML(video_info.text)
                for video_each in video_selector:
                    click_log = video_each.xpath('//click/text()')
                    danmu_log = video_each.xpath('//danmu/text()')
                    coins_log = video_each.xpath('//coins/text()')
                    favourites_log = video_each.xpath('//favourites/text()')
                    duration_log = video_each.xpath('//duration/text()')
                    honor_click_log = video_each.xpath('//honor[@t="click"]/text()')
                    honor_coins_log = video_each.xpath('//honor[@t="coins"]/text()')
                    honor_favourites_log = video_each.xpath('//honor[@t="favourites"]/text()')

                    if honor_click_log:
                        honor_click = honor_click_log[0]
                    else:
                        honor_click = 0
                    if honor_coins_log:
                        honor_coins = honor_coins_log[0]
                    else:
                        honor_coins = 0
                    if honor_favourites_log:
                        honor_favourites = honor_favourites_log[0]
                    else:
                        honor_favourites = 0

                    if click_log:
                        click = click_log[0]
                    else:
                        click = -1
                    if danmu_log:
                        danmu = danmu_log[0]
                    else:
                        danmu = -1
                    if coins_log:
                        coins = coins_log[0]
                    else:
                        coins = -1
                    if favourites_log:
                        favourites = favourites_log[0]
                    else:
                        favourites = -1
                    if duration_log:
                        duration = duration_log[0]
                    else:
                        duration = ""

                    json_url = "http://api.bilibili.com/x/reply?jsonp=jsonp&type=1&sort=0&pn=1&nohot=1&oid=" + av
                    jsoncontent = requests.get(json_url, headers=head).content
                    jsDict = json.loads(jsoncontent)
                    if jsDict['code'] == 0:
                        jsData = jsDict['data']
                        jsPages = jsData['page']
                        common = jsPages['acount']
                        try:
                            conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset='utf8')
                            cur = conn.cursor()
                            conn.select_db('python')
                            cur.execute('INSERT INTO video VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                                [str(av), str(av), cid, title, tminfo, time, click, danmu, coins, favourites, duration,
                                                 mid, name, article, fans, tag1, tag2, tag3, str(common), honor_click, honor_coins, honor_favourites])

                            print "Succeed: av" + str(av)
                        except MySQLdb.Error, e:
                            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                    else:
                        print "Error_Json: " + url
            else:
                print "Error_noCid:" + url
        else:
            print "Error_404: " + url


pool = ThreadPool(10)
# results = pool.map(spider, urls)
try:
    results = pool.map(spider, urls)
except Exception, e:
    # print 'ConnectionError'
    print e
    time.sleep(300)
    results = pool.map(spider, urls)

pool.close()
pool.join()
