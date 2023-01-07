# Docker basics

## lets start

### Setup docker in linux/ubuntu
```
    sudo apt-get update
    
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    
    sudo mkdir -p /etc/apt/keyrings
    
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    docker run code-hacker
```

### Start Service
```

docker compose build
docker compose -d up

```

### call service start endpoint
```
open http://localhost:8000/get-user/123-test
```


### Thing to remember while working on docker
1. Each service should be in same network(by default services must be in same network), to check use `docker inspect <docker-container-name>`
    and check network name.
2. Call service1 in service2 docker map service1 public ip with service docker-container-name. Example ping service1 or wget http://service1:8000/health-check
3. While working with microservice call must add CORS