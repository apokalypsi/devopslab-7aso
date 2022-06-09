## Laboratório DevOps
 
[![DevOpsLab Pipeline](https://github.com/apokalypsi/devopslab-7aso/actions/workflows/pipeline.yml/badge.svg)](https://github.com/apokalypsi/devopslab-7aso/actions/workflows/pipeline.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=apokalypsi_devopslab-7aso&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=apokalypsi_devopslab-7aso)


Aplicação Simples em Python/Flask com teste usando Unittest.

Diego Batista Pereira da Silva



### Ciar nosso container Docker:

`$ docker ps -a`

`$ docker images`

`$ docker build -t myapp:v1.0  .`

`$ docker images`

`$ docker run --name myapp --expose 80 --env PORT=80  -td myapp:v1.0`

`$ docker inspect myapp`

`$ curl 172.17.0.2`