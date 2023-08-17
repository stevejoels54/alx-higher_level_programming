-- 1. List all the tv shows. Order them alphabetically.
SELECT tv_show.`title`
  FROM `tv_shows` AS tv_show
    INNER JOIN `tv_show_genres` AS tv_show_genre
    ON tv_show.`id` = tv_show_genre.`show_id`
    INNER JOIN `tv_genres` AS tv_genre
    ON tv_genre.`id` = tv_show_genre.`genre_id`
    WHERE tv_genre.`name` = "Comedy"
 ORDER BY tv_show.`title`;
