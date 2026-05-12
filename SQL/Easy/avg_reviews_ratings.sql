SELECT ROUND(AVG(stars), 2) AS avg_stars, product_id, EXTRACT(MONTH FROM submit_date) AS mth FROM reviews
GROUP BY mth, product_id ORDER BY mth, product_id;
