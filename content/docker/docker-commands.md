Title: Docker Commands
Date: 2020-10-27 12:00
Category: Docker
Slug: docker-commands 

Build image

```bash
docker build . -t tagname
```

Shell inside container, etc...

```bash
docker exec -it image sh
```

Grep logs

```bash
docker logs image 2>&1 | grep "string"
```

Get dump.sql from container

```bash
docker exec -it image pg_dump -U username database > dump.sql
```

Restore from  dump.sql to container

```bash
cat dump.sql | docker exec -i image psql -U username -d database
```

Clear old image

```bash
docker system prune -a
```