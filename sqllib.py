INSERT_SQL = """
INSERT INTO `spider_dmhy`(`publish_date`, `type`, `url`, `name`, `magnet`, `size`, `create_date`) VALUES (%s, %s, %s, %s, %s, %s, now());
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
	`type` = %s
	AND url = %s;
"""

CHECK_SQL_BY_DICT = """
SELECT 
	count(1)
FROM
	spider_dmhy
WHERE
	`type` = %(type)s
	AND url = %(url)s;
"""

