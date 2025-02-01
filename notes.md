- from data.json: 

```sql
SELECT  DISTINCT  OWNER FROM raw order by OWNER;
```

## joins

select all from greika/kanton then add owner data from unlock as a comma separated column `OWNERS`
```sql
SELECT 
    kanton.*,
    GROUP_CONCAT(unlock.OWNER, ', ') AS OWNERS
FROM 
    main.greika as kanton
LEFT JOIN 
    main.raw as unlock
ON 
    kanton.EGRID = unlock.EGRID
GROUP BY 
    kanton.EGRID
```

