-- 1. List all the genres in the database, return desending order
SELECT tv_genre.`name` AS `genre`,
    COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS tv_genre
    INNER JOIN `tv_show_genres` AS tv_show_genre
    ON tv_genre.`id` = tv_show_genre.`genre_id`
 GROUP BY tv_genre.`name`
 ORDER BY `number_of_shows` DESC;