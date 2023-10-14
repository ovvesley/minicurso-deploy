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

sudo apt-get update -y 
sudo apt-get install ca-certificates curl gnupg -y 
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y 



# install last version docker

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


# inciiar o servico do docker
sudo service docker start
sudo docker run hello-world

---


# ativar docker sem root
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world


# habilitar o servico

sudo systemctl enable docker.service
sudo systemctl enable containerd.service