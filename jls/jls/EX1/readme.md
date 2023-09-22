# **Exercício 1: Nível Básico**
## *Objetivo:* Este exercício destina-se a verificar a compreensão básica do Docker.
1. Crie um contêiner Docker a partir da imagem oficial do Ubuntu.
2. Dentro do contêiner, instale o aplicativo "curl" usando o gerenciador de pacotes
"apt".
3. Verifique se o "curl" está instalado corretamente dentro do contêiner e imprima a
versão do "curl" na saída padrão.

## Resolução
### No terminal do host
```
docker pull ubuntu
```
```
docker run -it ubuntu /bin/bash
```
### No bash do container
```
apt update
```
```
apt install curl
```
```
curl --version
```
