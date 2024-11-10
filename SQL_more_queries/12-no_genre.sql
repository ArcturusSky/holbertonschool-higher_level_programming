-- Script that lists all shows contained in "hbtn_0d_tvshows" without a genre.

SELECT tv_shows.title, tv_show_genres.genre_id   -- Selecting the show's title and genre_id (will be NULL for shows without a genre)
FROM tv_shows                                    -- Starting with the "tv_shows" table as the main source of data
LEFT JOIN tv_show_genres                          -- Using LEFT JOIN to keep all shows, even if they don't have a genre linked
ON tv_show_genres.show_id = tv_shows.id           -- Matching each show’s ID in "tv_shows" to "show_id" in "tv_show_genres"
WHERE tv_show_genres.genre_id IS NULL             -- Filtering to only include shows where genre_id is NULL (no genre linked)
ORDER BY tv_shows.title ASC;                      -- Sorting the results alphabetically by show title
