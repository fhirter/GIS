- from data.json: 

```sql
SELECT  DISTINCT  OWNER FROM raw order by OWNER;
```

```sql
SELECT DISTINCT kanton.*, unlock.*
FROM raw as unlock
JOIN main.greika as kanton
    ON kanton.EGRID = unlock.EGRID;
```