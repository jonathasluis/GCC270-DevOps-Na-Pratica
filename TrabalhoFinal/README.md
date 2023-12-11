# Trabalho Final de GCC270 - DEVOps na Prática.

## Passo 1: Desenvolvimento de uma Aplicação TODO List
Código TodoList adaptado para não utilizar banco de dados.
 - Adaptado: [TodoList - adaptado](./app/app.py)
 - Original: [TodoList - Original](../ToDoList/)

## Passo 2: Criação do Dockerfile
[Dockerfile](./Dockerfile)

## Passo 3: Publicação no Docker Hub

### Criação da Imagem
```shell
docker build -t jonathassousa035/trabalhofinal:v1 .
```
### Enviar para Docker Hub
```shell
docker push jonathassousa035/trabalhofinal
```

## Passo 4: Criação de Artefatos no Kubernetes com Helm
```shell
helm create trabalhofinal
```
```shell
helm install trabalhofinal ./trabalhofinal
```
```shell
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=trabalhofinal,app.kubernetes.io/instance=trabalhofinal" -o jsonpath="{.items[0].metadata.name}")
```
```shell
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
```
```shell
kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```