# sifos
Sistema de Gestión Forestal Sostenible

## Documentation

### Requirements

[Requirements](https://drive.google.com/open?id=1oiQh0QQZMWD-ptlE9fQ2_5NQgC7TS5BWRZcsKb-Hp2k)

### Mockups

[Mockups](https://drive.google.com/open?id=1flKTkbqYR01N30gm7wugDByb4mloGO7i)

### Class diagram

[Class diagram](https://drive.google.com/open?id=1mZY2_OF6Fe3bRvz97R9OUrwiKV6pyqTZ)

## Requirements specification document, mockups and class diagram.

 [Especificación de Requisitos de Software del Sistema de Gestión Forestal sostenible - SIFO](https://drive.google.com/open?id=1NP-dPYXarNpQv6mZu3DLxRIvlqEU1YBk)

## Docker

### Requirements

Docker - Container Framework
### Run local environments Docker

docker-compose up -d && docker restart web_web_1
### Restart and run migrations

docker restart web_web_1
### View Docker logs

docker logs --tail=100 -f web_web_1
### Install requirements

Modify requirements.txt
docker stop web_web_1
docker rm web_we
docker rmi web_web
docker-compose up -d
### Run Prod

docker build -t web_web .
docker run -d -p 80:8001 --name sifos_prod -e DATABASE_NAME=sifos -e DATABASE_USER=sifos -e DATABASE_PASSWORD=A12345678 -e DATABASE_HOST=localhost -e DATABASE_PORT=5432 web_web sh start.sh

## Wiki

[Entra a la wiki](https://github.com/jmencisom/sifos/wiki)


