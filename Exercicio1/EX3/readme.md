# **Exercício 3: Nível Avançado**
## *Objetivo:* Este exercício requer conhecimento avançado de Docker Compose para gerenciar aplicativos multi-container.
1. Crie um arquivo Docker Compose para orquestrar três contêineres: um para um
banco de dados PostgreSQL, outro para um servidor de aplicativos Node.js e um
terceiro para um servidor web Nginx.
2. Configure as dependências corretamente de forma que o servidor Node.js só inicie
após o banco de dados PostgreSQL estar pronto.
3. Exponha as portas apropriadas para acessar o servidor Node.js e o servidor web
Nginx a partir da máquina host.
4. Crie uma rede Docker personalizada para os contêineres se comunicarem.
5. Inicialize a pilha de contêineres usando o Docker Compose e verifique se todos os
serviços estão funcionando corretamente.


## Comandos
```
docker compose up -d --build
```

