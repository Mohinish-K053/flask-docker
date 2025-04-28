mysql run command

docker run -d --name samu -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345678 -e MYSQL_DATABASE=demo --network demo mysql

docker run -d -p 8088:80 --network demo -e WORDPRESS_DB_NAME=demo -e WORDPRESS_DB_HOST=samu:3306 -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=12345678 wordpress
