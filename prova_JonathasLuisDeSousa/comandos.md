## Nome da Imagem
```shell
jonathassousa035/meu-app-node
```
## Build image
```shell
docker build -t jonathassousa035/meu-app-node .
```
## Execução do container na porta 8080
```shell
docker container run -d -p 8080:8080 jonathassousa035/meu-app-node
```
## Aplicação do deployment
```shell
kubectl apply -f deployment.yaml
```
## Aplicação do service
```shell
kubectl apply -f service.yaml
```
## Port-forward do service
```shell
kubectl port-forward svc/deploy 8080:8080
```