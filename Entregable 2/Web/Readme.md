#SIFOS

##Overview
This microservice ....

##Requirements
- Docker - Container Framework

##Run local environments Docker
- docker-compose up -d && docker restart web_web_1

##Restart and run migrations
- docker restart web_web_1

##View Docker logs
- docker logs --tail=100 -f web_web_1

##Install requirements
- Modify requirements.txt
- docker stop web_web_1
- docker rm web_we
- docker rmi web_web
- docker-compose up -d

##Run Prod
- docker build -t web_web .
- docker run -d -p 80:8001 --name sifos_prod -e DATABASE_NAME=sifos -e DATABASE_USER=sifos -e DATABASE_PASSWORD=A12345678 -e DATABASE_HOST=localhost -e DATABASE_PORT=5432 web_web sh start.sh
