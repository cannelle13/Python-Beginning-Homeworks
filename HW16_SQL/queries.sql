Create next analytic queries: 

1. Find a user who had the biggest amount of reservations. Return username and user_id
SELECT u.full_name, u.user_id
FROM users u
JOIN reservations r ON u.user_id = r.guest_id
GROUP BY u.user_id, u.full_name
ORDER BY COUNT(r.reservation_id) DESC
LIMIT 1;

2. Find a host who earned the biggest amount of money for the last month. Return hostname and host_id
SELECT u.user_id AS host_id, u.full_name AS hostname
FROM users u
JOIN rooms r ON u.user_id = r.host_id
JOIN reservations res ON r.room_id = res.room_id
JOIN payments p ON res.payment_id = p.payment_id
WHERE p.payment_status = 'Successful'
      AND p.payment_date >= NOW() - INTERVAL '1 month'
GROUP BY u.user_id, u.full_name
ORDER BY SUM(p.total_price) DESC
LIMIT 1;

3. Find a host with the best average rating. Return hostname and host_id
SELECT u.user_id AS host_id, u.full_name AS hostname
FROM users u
JOIN host_reviews hr ON u.user_id = hr.host_id
GROUP BY u.user_id, u.full_name
ORDER BY AVG(hr.rating) DESC
LIMIT 1;