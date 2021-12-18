# sudo docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root-password \
#  -e MYSQL_DATABASE=ssi \
#  -e MYSQL_USER=ahmed \
#  -e MYSQL_PASSWORD=ahmed \
#  -d mysql:latest

sudo docker-compose up -d