Title: PostgresSQL Commands
Date: 2020-10-27 12:00
Category: Postgres
Slug: postgres-commands 

Save backup to dump.sql

```bash
pg_dump --clean -U username database  > dump.sql
```

Restore from  dump.sql

```bash
sudo -i -u postgres psql -d database < dump.sql
```

```bash
psql -U postgres -d database < dump.sql
```

```bash
psql --username username --dbname database -f dump.sql
```


