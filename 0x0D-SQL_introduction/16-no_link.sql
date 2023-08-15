-- Lists all records of second_table having a name value with descending score.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
