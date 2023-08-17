-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows, records are ordered by ascending genre name.
SELECT tv_genre.`name`
  FROM `tv_genres` AS tv_genre
    INNER JOIN `tv_show_genres` AS tv_show_genre
    ON tv_genre.`id` = tv_show_genre.`genre_id`

    INNER JOIN `tv_shows` AS tv_show
    ON tv_show.`id` = tv_show_genre.`show_id`
    WHERE tv_show.`title` = "Dexter"
 ORDER BY tv_genre.`name`;