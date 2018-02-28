-- 1
SELECT billing.charged_datetime, SUM(billing.amount) AS revenue
FROM billing
WHERE billing.charged_datetime >= "2012-03-01 00:00:00" AND billing.charged_datetime <= "2012-04-01 00:00:00"
GROUP BY billing.charged_datetime;

-- 2
SELECT clients.client_id, SUM(billing.amount) AS revenue
FROM billing
JOIN clients ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

-- 3
SELECT clients.client_id, sites.domain_name
FROM clients
JOIN sites ON sites.client_id = clients.client_id
WHERE clients.client_id = 10;

-- 4a
SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites, MONTHNAME(sites.created_datetime) as month_created, YEAR(sites.created_datetime) AS year_created
FROM clients
JOIN sites ON sites.client_id = clients.client_id
WHERE clients.client_id = 1
GROUP BY sites.created_datetime;

-- 4b
SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites, MONTHNAME(sites.created_datetime) as month_created, YEAR(sites.created_datetime) AS year_created
FROM clients
JOIN sites ON sites.client_id = clients.client_id
WHERE clients.client_id = 20
GROUP BY sites.created_datetime;

-- 5
SELECT sites.domain_name, leads.registered_datetime, COUNT(sites.domain_name) AS leads_generated
FROM sites
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime < "2011-02-16 00:00:00";

-- 6
SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS number_of_leads, leads.registered_datetime
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime < "2012-01-01 00:00:00";

-- 7 
SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS leads_generated, MONTH(leads.registered_datetime) AS month, YEAR(leads.registered_datetime) AS year
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE MONTH(leads.registered_datetime) BETWEEN 1 AND 6 
AND YEAR(leads.registered_datetime) = 2011;

-- 8a 
SELECT clients.client_id, clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id) AS leads_generated, leads.registered_datetime
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime < "2012-01-01 00:00:00"
ORDER BY clients.client_id;

-- 8b
SELECT clients.client_id, clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id) AS leads_generated, leads.registered_datetime
FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON leads.site_id = sites.site_id
ORDER BY clients.client_id;

-- 9 
SELECT clients.client_id, SUM(billing.amount) AS revenue, MONTH(billing.charged_datetime) as month, YEAR(billing.charged_datetime) AS year
FROM billing
JOIN clients ON clients.client_id = billing.client_id
ORDER BY clients.client_id;

-- 10
SELECT CONCAT(clients.first_name," ",clients.last_name) AS client_name, sites.site_id, GROUP_CONCAT(sites.domain_name)
FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
GROUP BY client_name;