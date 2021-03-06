import time
import sqllib
import requests
import sys
import random

from fake_useragent import UserAgent
from loguru import logger
from config import MysqlConfig
from utils import ProxyUtil
from lxml import etree

# 控制日志显示级别
logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
handler_id = logger.add(sys.stderr, level="INFO")  # 添加一个可以修改控制的handler


class DMHYSpider(object):
    def __init__(self):
        # last 1500
        # end 4437
        self.start_num = 1500
        self.end_num = 1500
        self.base_url = 'http://dmhy.org/topics/list/sort_id/2/page/{}'
        self.url = ""
        self.ua = UserAgent()
        self.db = MysqlConfig.DB_CONN
        self.cursor = self.db.cursor()
        self.result_set = []
        self.is_ip_pool = False  # 是否启用ip池

        # 基准表达式
        self.base_expression = """//table[@class="tablesorter"]/tbody/tr"""

    def get_html(self):

        if self.is_ip_pool:
            proxy = ProxyUtil.dict_proxy()
            while True:
                try:
                    proxy = ProxyUtil.dict_proxy()
                    if proxy:
                        logger.debug(proxy)
                        html = requests.get(self.url, headers={'user-agent': self.ua.random}, proxies=proxy,
                                            verify=False,
                                            timeout=10).text
                        if html is not None:
                            logger.info("html获取完成")
                            return html
                    else:
                        time.sleep(600)
                except Exception as e:
                    logger.error('请求失败')
                    logger.error(e)
                    ProxyUtil.delete_dict_proxy(proxy)
        else:
            res = requests.get(url=self.url, headers={'User-Agent': self.ua.random})
            logger.info("html获取完成")
            return res.text

    def pares_html(self, html):
        element_list = etree.HTML(html).xpath(self.base_expression)
        logger.debug(element_list)
        logger.debug(len(element_list))
        debug_count = 0
        for element in element_list:
            dd = {}
            try:
                debug_count += 1

                # 内容处理
                dd['publish_date'] = element.xpath(""".//td[@width="98"]/span/text()""")[0]
                # logger.debug(element.xpath(""".//a//font[@color]/text()"""))
                dd['type'] = element.xpath(""".//a//font/text()""")[0]
                dd['url'] = element.xpath(""".//td[@class="title"]/a/@href""")[0]
                # logger.debug(element.xpath(""".//td[@class="title"]/a/text()""")[0].strip())
                dd['name'] = element.xpath(""".//td[@class="title"]/a/text()""")[0].strip()
                dd['magnet'] = element.xpath(""".//td/a[@title="磁力下載"]/@href""")[0]
                dd['size'] = element.xpath(""".//td[contains(text(), "GB") or contains(text(), "MB")]/text()""")[0]
                self.result_set.append(dd)

                logger.debug("当前第{}组数据".format(debug_count))
            except Exception as e:
                print(e)
                logger.error("第{}组数据出错".format(debug_count))
        logger.info("结果处理完成")

    def save_data(self):

        for num in range(len(self.result_set) - 1, -1, -1):
            self.cursor.execute(sqllib.CHECK_SQL_BY_DICT, self.result_set[num])
            check_result = self.cursor.fetchone()
            if check_result[0] != 0:
                del self.result_set[num]
        logger.info("新数据检查完毕")

        self.cursor.executemany(sqllib.INSERT_SQL_BY_DICT, self.result_set)
        self.db.commit()
        logger.info("新增数据 {} 条".format(len(self.result_set)))
        logger.info("结果保存完成")

        self.result_set = []

    def run(self):
        sleep_count = 0
        for page in range(self.start_num, self.end_num + 1):
            self.url = self.base_url.format(page)
            logger.info("正在处理页面：{}".format(self.url))
            html_content = self.get_html()
            self.pares_html(html_content)
            self.save_data()
            time.sleep(random.random() * 5)

            sleep_count += 1
            if sleep_count >= 30:
                time.sleep(10)
                sleep_count = 0

        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    logger.info("开始处理")
    start = time.time()
    spider = DMHYSpider()
    spider.run()
    logger.info("程序处理时间: {}".format(time.time() - start))
