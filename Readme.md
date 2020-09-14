# Sistema SHM Streamlit MQTT e MongoDB

## Run Streamlit, MQTT subscriber

Sistema de simulação de sensoriamento e servidor que armazena as informações no banco de dados não estruturado MongoDB.

![funcionamento](/funcionamento.gif)


### Run

## MongoDb

O primeiro passo será baixar a imagem do mongoDB, caso você faça uma pesquisa no Docker Hub, irá encontrar muitas imagens, mas eu particularmente gosto de utilizar a tutum/mongod.
```
sudo docker pull tutum/mongodb
```
Com a imagem do docker no seu host, vamos criar um container de servidor de banco de dados. Para isso, você pode escolher uma das duas instruções abaixo:
Criação de servidor sem senha, recomendado para ambiente de desenvolvimento
```
sudo docker run -d -p 27017:27017 -p 28017:28017 -e AUTH=no tutum/mongodb
```
Criação de servidor especificando uma senha
```
sudo docker run -d -p 27017:27017 -p 28017:28017 -e MONGODB_PASS="mypass" tutum/mongodb
```
O próximo passo será subir o seu servidor mongo. Para isso, execute os passos abaixo:

***CASO JA TENHA A IMAGEM BASTA LISTAR AS IMAGENS COM O COMANDO ABAIXO E DAR UM docker start 'CONTAINER ID'***
```
sudo docker ps -a
```
Esse comando irá listar os seus containers que não estão em execução, copie o containerID do mongo e execute o comando abaixo no seu terminal:
```
sudo docker start 77b903780b83
```

Agora para verificar se tudo foi configurado corretamente, execute ***mongo*** no seu terminal para acessar o client do seu servidor.

***PARA EXECUTAR O COMANDO mongo DEVE INSTALAR O PACOTE***
```
sudo apt-get install -y mongodb-org-shell
```

## MQTT


Executar `sudo docker-compose build` 
Em seguida `sudo docker-compose up`

## Simulando Sensores

Abra dois terminais e execute os scripts pub_client_1.py e pub_client_2.py:

```
python3 pub_client_1.py
```
python3 pub_client_2.py
```

## Simular a parametrização e a coleta das assinaturas de impedância dos sensores


Abra ![localhost:8501/?name=main](http://localhost:8501/?name=main) no navegador. 


