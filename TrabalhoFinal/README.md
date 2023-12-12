# Trabalho Final de GCC270 - DEVOps na Prática.

## Passo 1: Desenvolvimento de uma Aplicação TODO List

A aplicação desenvolvida foi feita em Python, utilizando o framework 'Flask' para criar uma aplicação web básica. A aplicação permite criar, alterar, excluir e visualizar listas de tarefas.

Esse código é uma adapatação do código da atividade de Docker Compose, que tinha que fazer uma TodoList que integrava com um banco de dados, com a adaptação os dados são persistidos em memória sem a necessidade de um BD.

Em resumo, este código cria uma aplicação web simples para gerenciar listas de tarefas usando Flask, com operações básicas de CRUD (Create, Read, Update, Delete) para listas de tarefas e tarefas individuais. A interface web é mínima e utiliza templates HTML para exibir as informações.
 - [TodoList - Adaptado](./app/app.py)
 - [TodoList - Original](../ToDoList/)

## Passo 2: Criação do Dockerfile
O Dockerfile para construir a imagem dessa aplicação é bem simples. A partir da imagem do 'Python 3.11.5-alpine3.17' (uma versão mais leve), se copia tudo que está no diretório [/app](./app) (aplicação, requerimentos e template) para a pasta **/app** dentro da imagem, que é definida como diretório de trabalho.

Após isso, é executado o comando *pip install* para baixar as dependencias que estão no arquivo [requirements.txt](./app/requirements.txt)

Em seguida, informa ao Docker que a aplicação dentro do contêiner estará ouvindo na porta 3000. Isso não publica automaticamente a porta para o host, mas é uma convenção para documentar as portas que a aplicação espera serem expostas.

E por fim, define-se o comando padrão a ser executado quando o contêiner for iniciado. Neste caso, executa o script Python chamado app.py.

[Dockerfile](./Dockerfile)

## Passo 3: Publicação no Docker Hub

### Criação da Imagem
```shell
docker build -t jonathassousa035/trabalhofinal:v1 .
```
### Enviar para Docker Hub
```shell
docker push jonathassousa035/trabalhofinal:v1
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
