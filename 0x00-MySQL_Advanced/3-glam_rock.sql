-- Write a SQL script that lists all bands with Glam rock
SELECT
  band_name,
  IFNULL (split, 2022) - formed As lifespan
FROM
  metal_bands
WHERE
  style LIKE '%Glam rock%'
ORDER BY
  lifespan DESC;
