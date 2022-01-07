#!/bin/bash

sudo apt update && sudo apt install -y \
    docker.io docker-compose

sudo systemctl enable --now docker

for file in `ls`
do
    if [ -d "$file" ] && [ "$file" != "nginx" ];
    then
        sudo docker-compose -f "$file/docker-compose.yml" up -d
    fi
done

sudo docker-compose -f "nginx/docker-compose.yml" up -d