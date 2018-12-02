Enterprise Employee management
add client_secrets.json
export FLASK_APP="server.py" 
export FLASK_DEBUG=1 
flask run


----
To build on Docker image: 
1) docker build -t project .
2) docker run -p 5000:80 project

To place on docker container: 
1) docker run -d -p 5000:80 project
3) go to localhost:5000


-----
Docker notes: 
1) View docker containers: 
docker container ls

2) Stop docker container: 
docker container stop <container id> 