import os
import subprocess

# Diretório do projeto
project_dir = "wordpress-docker"
os.makedirs(project_dir, exist_ok=True)

# Conteúdo do arquivo docker-compose.yml
docker_compose_content = """version: '3.8'

services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - ./wp-content:/var/www/html/wp-content

  db:
    image: mysql:5.7
    container_name: wordpress_db
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - ./db_data:/var/lib/mysql

volumes:
  db_data:
"""

# Caminho para o arquivo docker-compose.yml
docker_compose_path = os.path.join(project_dir, "docker-compose.yml")

# Criar o arquivo docker-compose.yml
with open(docker_compose_path, "w") as file:
    file.write(docker_compose_content)

# Navegar para o diretório do projeto
os.chdir(project_dir)

# Rodar o Docker Compose
subprocess.run(["docker", "compose", "up", "-d"])

print("Setup do WordPress concluído com sucesso!")
print(f"Acesse o WordPress em: http://localhost:8080")
