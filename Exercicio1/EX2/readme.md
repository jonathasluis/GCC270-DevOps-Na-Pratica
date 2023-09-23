# **Exercício 2: Nível Intermediário**
## *Objetivo:* Este exercício testa a capacidade de criar e modificar contêineres Docker.
1. Crie um contêiner Docker a partir da imagem oficial do Node.js.
2. Copie um aplicativo Node.js de sua escolha para o contêiner.
3. Exponha uma porta no contêiner para acessar o aplicativo.
4. Crie uma imagem personalizada com o aplicativo Node.js e a configuração da
porta.
5. Inicie um contêiner a partir da imagem personalizada e verifique se o aplicativo está
acessível no navegador.


## Comandos
```
docker build -t teste .
```
```
docker container run -d -p 8080:3000 teste
```
