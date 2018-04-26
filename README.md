## docker-ansible-devops

#### Build Stage



#### Release Stage

```
docker-compose up agent
docker-compose run app manage.py collectstatic
docker-compose run app manage.py migrate
docker-compose run nginx

```