### 爬虫结构
```
dmhy-spider
│  spider.py                主程序
│  README.md
│  requirements.txt         运行环境
│  sqllib.py                sql
├─config
│  MysqlConfig.py           mysql配置文件
└─utils
   ProxyUtil.py             IP池工具
```

### 安装环境
```shell script
pip install -r requirements.txt
```

### 建表语句
```sql
CREATE TABLE `spider_dmhy` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `publish_date` datetime DEFAULT NULL COMMENT '帖子发布日期',
  `type` varchar(10) DEFAULT NULL COMMENT '帖子分类',
  `url` varchar(500) DEFAULT NULL COMMENT '帖子链接',
  `name` varchar(500) DEFAULT NULL COMMENT '帖子名称',
  `magnet` longtext COMMENT '磁力链接',
  `size` varchar(20) DEFAULT NULL COMMENT '大小',
  `create_date` datetime DEFAULT NULL COMMENT '记录插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=582 DEFAULT CHARSET=utf8mb4;
```

### 配置数据库
```
MysqlConfig 文件更改键值对的值即可
```

### 设置爬取页数
spider.py文件
``` python
self.start_num = 1      开始爬取页数
self.end_num = 100      爬取目标页数
```

### 运行程序
```shell script
python spider.py
```
