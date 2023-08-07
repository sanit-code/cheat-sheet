/* Select examples */
SELECT
        CASE /* Show data in column depending on cases */
            WHEN 50 < t1.population OR t1.resources < 30 THEN 'Classification 1'
            WHEN t1.city='City example' THEN 'Classification 2'
            WHEN t1.city IN (SELECT t2.city FROM t2) THEN 'Classification 3' /* When with subquery */
            ELSE 'Classification 4'
        END AS Classification, /* Name column */
        CONCAT(t1.state, ' - ', t1.city) AS Location, /* Concat example */
        t1.* /* Select all columns of t1 */
    FROM t1
    WHERE
        t1.population > 10 AND /* Basic comparison */
        MOD(t1.resources,2)=0 AND /* Modulo example */
        UPPER(SUBSTRING(t1.city,1,1)) IN ('A','B','C') AND /* Substring example */
        UPPER(RIGHT(t1.state,1)) IN ('E', 'F')  /* Suffix example */
;
/*
    Sample output:
    Classification      Location        ...
    Classification 1    State1 - City1  ...
    Classification 3    State1 - City2  ...
    Classification 2    State2 - City3  ...
    ...
*/

/* Count+Distinct example */
SELECT count(*)-count(distinct t1.state) FROM t1;
/*
    Sample output:
    34
*/

/* Sort by count */
SELECT
        CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.')
    FROM OCCUPATIONS
    GROUP BY Occupation
    ORDER BY Count(*);
/*
    Sample output:
    There are a total of 5 doctors.
    There are a total of 5 teachers.
    ...
*/

/* Union example */
SELECT * FROM (
    SELECT t1.population, t1.city FROM t1 ORDER BY t1.population, t1.city LIMIT 1 /* Smallest city */
) UNION (
    SELECT t1.population, t1.city FROM t1 ORDER BY t1.population DESC, t1.city LIMIT 1 /* Largest city */
);
/*
    Sample output:
    population      city
    120000          City1
    321000          City2
*/

/* Window functions */
SELECT
        ROW_NUMBER() OVER (PARTITION BY t1.state ORDER BY t1.id) AS row_number, /* Rows will have their position on each state's order */
            /* RANK() and DENSE_RANK() are like ROW_NUMBER(), but */
            /* Ties have the same number, and ranks might be skipped when ties occur depending on the function */
            /* RANK() -> 1,2,2,2,5 */
            /* DENSE_RANK() -> 1,2,2,2,3 */
        SUM(t1.resources) OVER () AS total, /* Rows will have total amount of all data */
        SUM(t1.resources) OVER (PARTITION BY t1.state) AS state_total, /* Rows will sum of all data in same state */
        SUM(t1.resources) OVER (ORDER BY t1.id) AS accumulated_resources, /* ith row will have the sum from first to ith */
        SUM(t1.resources) OVER (PARTITION BY t1.state ORDER BY t1.id)
                AS accumulated_resources_by_state, /* for each state, ith element will have the sum from first to ith in that partition */
        t1.resources - LAG(t1.resources, 1) OVER partition_state_order_id
                AS resource_difference /* LAG obtains the previous value, LEAD the next one in the window */
    FROM t1
    WHERE t1.population > 0
    WINDOW partition_state_order_id AS (PARTITION BY t1.state ORDER BY t1.id) /* Can alias the window */
;
/*
    Sample output:
    row_number      total           state_total         accumulated_resources       accumulated_resources_by_state  resource_difference
    1               1,000,000       100,000             50,000                      50,000                          null
    2               1,000,000       100,000             100,000                     100,000                         50,000
    1               1,000,000       70,000              130,000                     30,000                          null
    2               1,000,000       70,000              150,000                     50,000                          20,000
    3               1,000,000       70,000              170,000                     70,000                          20,000
    ...
*/

/* Window functions : Rows clause */
/* This 3 are equivalent */
SELECT t1.resoureces OVER (PARTITION BY t1.state ORDER BY t1.population) FROM t1;
SELECT t1.resoureces OVER (PARTITION BY t1.state ORDER BY t1.population ROWS BETWEEN UNBOUNDED PRECEDING) FROM t1; /* current row is optional */
SELECT t1.resoureces OVER (PARTITION BY t1.state ORDER BY t1.population ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM t1;
/* This 2 are equivalent */
SELECT t1.resoureces OVER (PARTITION BY t1.state) FROM t1;
SELECT t1.resoureces OVER (PARTITION BY t1.state ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) FROM t1;
/*
 Options for bounds:
 - UNBOUNDED PRECEDING: All rows before current row
 - n PRECEDING: n rows before current row
 - CURRENT ROW: Just the current row
 - n FOLLOWING: n rows after current row
 - UNBOUNDED FOLLOWING: All rows after current row
*/

/* EXPLAIN */
EXPLAIN
SELECT teams.conference AS conference,
       players.school_name,
       COUNT(1) AS players
    FROM benn.college_football_players players
         JOIN benn.college_football_teams teams
              ON teams.school_name = players.school_name
    GROUP BY 1,2;
/* Depending on implementation it will show the query plan: an approximation of what will happen when you run the query */
/* The query plan is executed from bottom to top, so you might what to reduce the number of rows wherever possible to increase performance */