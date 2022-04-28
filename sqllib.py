INSERT_SQL_MD5 = """
INSERT INTO `spider_dmhy`(`md5`, `publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, now());
"""

INSERT_SQL = """
INSERT INTO `spider_dmhy`(`publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) VALUES ( %s, %s, %s, %s, %s, %s, now());
"""

INSERT_SQL_BY_DICT_MD5 = """
INSERT INTO `spider_dmhy`(`md5`, `publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) \
VALUES (MD5(%(url)s), %(publish_date)s, %(type)s, %(url)s, %(name)s, %(magnet)s, %(size)s, now());
"""

INSERT_SQL_BY_DICT = """
INSERT INTO `spider_dmhy`(`publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) \
VALUES (%(publish_date)s, %(type)s, %(url)s, %(name)s, %(magnet)s, %(size)s, now());
"""

CHECK_SQL = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	AND url = %s;
"""

CHECK_SQL_MD5 = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	`type` = %s
	AND md5 = MD5(%s);
"""

CHECK_SQL_BY_DICT = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	url = %(url)s;
"""

CHECK_SQL_BY_DICT_MD5 = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	md5 = MD5(%(url)s);
"""

