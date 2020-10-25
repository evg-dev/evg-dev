Title: Ubuntu/Debian install PostgresSQL
Date: 2020-10-25 12:00
Category: Postgres
Slug: install-postgres 

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```
Check install

```bash
sudo -i -u postgres psql
```

Create user in linux

```bash
sudo adduser username
```

Add user in postgres 

```bash
sudo -u postgres createuser --interactive
```
And see

```bash
Enter name of role to add: username
Shall the new role be a superuser? (y/n) y
```

Create database

```bash
sudo -u postgres createdb username
```

Enter on postgres

```bash
sudo -u username psql
```

Set privileges

```postgresql
GRANT ALL PRIVILEGES ON DATABASE  dbname TO username;
```

Set password for user

```postgresql
ALTER USER username WITH PASSWORD 'password';
```
Set owner

```postgresql
ALTER DATABASE dbname OWNER TO username;
```