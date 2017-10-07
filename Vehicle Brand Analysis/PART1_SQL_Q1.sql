SELECT
DISTINCT c.city_name,
--Percentile between predicted and actual
PERCENTILE_DISC(0.9) WITHIN GROUP (ORDER BY predicted_eta) OVER (PARTITION BY c.city_name) AS Pred,
PERCENTILE_DISC(0.9) WITHIN GROUP (ORDER BY actual_eta) OVER (PARTITION BY c.city_name) AS Actual,

--Difference
(PERCENTILE_DISC(0.9) WITHIN GROUP (ORDER BY predicted_eta) OVER (PARTITION BY c.city_name)
-PERCENTILE_DISC(0.9) WITHIN GROUP (ORDER BY actual_eta) OVER (PARTITION BY c.city_name)) AS Difference

FROM trips t
JOIN cities c ON t.city_id = c.city_id

WHERE c.city_name IN ('Qarth','Meereen') 
AND t.request_at::timestamp AT TIME ZONE 'UTC' BETWEEN '{{EndDate}}'- INTERVAL '30 Days' AND '{{EndDate}}23:59:59'
AND t.status='completed'
GROUP BY c.city_name

ORDER BY c.city_name ASC
