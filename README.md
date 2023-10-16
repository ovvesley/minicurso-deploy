## Instalação do postgress

# Create the file repository configuration:
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql


# iniciando o servico

sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service
sudo systemctl status postgresql.service
sudo systemctl restart postgresql.service


## Criando usuario do banco



conectar no banco
# sudo -u postgres psql

cria o usuario

```sql
CREATE DATABASE minicurso;
CREATE USER pythonapp WITH ENCRYPTED PASSWORD 'admin123';
GRANT ALL PRIVILEGES ON DATABASE minicurso TO pythonapp;
```


# liberar conexões externas ao banco


sudo vim /etc/postgresql/16/main/postgresql.conf

modificar o listenaddress para *

e adicionar a linha
host    all             all             0.0.0.0/0               md5

* isso libera conexão de qualquer usuario com acesso ao address

# restart postgress
sudo systemctl restart postgresql.service


# install docker

curl -sSL https://get.docker.com/ | sh

# resolver usuario root

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world


# configurar docker swarm

touch docker-swarm.yml


# docker swarm

# docker init 

# realizar o deploy
docker stack deploy --compose-file docker-swarm.yml stackminicurso


# visualizar a stack
docker stack ps stackminicurso --no-trunc


