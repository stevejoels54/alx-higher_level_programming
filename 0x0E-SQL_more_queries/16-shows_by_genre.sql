-- 1. List all the tv shows.
SELECT tv_show.`title`, tv_genre.`name`
  FROM `tv_shows` AS tv_show
    LEFT JOIN `tv_show_genres` AS tv_show_genre
    ON tv_show.`id` = tv_show_genre.`show_id`
    LEFT JOIN `tv_genres` AS tv_genre
    ON tv_show_genre.`genre_id` = tv_genre.`id`
 ORDER BY tv_show.`title`, tv_genre.`name`;
