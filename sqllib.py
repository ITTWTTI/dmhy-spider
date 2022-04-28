INSERT_SQL = """
INSERT INTO `spider_dmhy`(`md5`, `publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, now());
"""

INSERT_SQL_BY_DICT = """
INSERT INTO `spider_dmhy`(`md5`, `publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) \
VALUES (%(md5)s, %(publish_date)s, %(type)s, %(url)s, %(name)s, %(magnet)s, %(size)s, now());
"""

CHECK_SQL = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	`type` = %s
	AND md5 = %s;
"""

CHECK_SQL_BY_DICT = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	`type` = %(type)s
	AND md5 = %(md5)s;
"""

