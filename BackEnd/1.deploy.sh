#!/usr/bin/env bash

source .env

SERVER_SERVICE=$SERVER_SERVICE
APPNAME=$SVC_MANAGEMENT_NAME
TAG=latest
SERVER_CONFIG=/home/ws/$PROJECT_NAME/$APPNAME/.env
REGISTRY=$REGISTRY/$PROJECT_NAME
PORT=$SVC_MANAGEMENT_PORT
DOCKER_RUN="\
docker pull $REGISTRY/$APPNAME:$TAG;\
docker rm -f $APPNAME; \
docker run -d \
-m 512m \
-p $PORT:$PORT \
--restart always \
--env-file $SERVER_CONFIG \
--name $APPNAME \
--log-opt max-size=50m \
$REGISTRY/$APPNAME:$TAG"

echo "Deploying $REGISTRY/$APPNAME:$TAG"
echo "Use Port: $PORT"

docker build -t $APPNAME . --build-arg appName=$APPNAME
docker tag $APPNAME $REGISTRY/$APPNAME:$TAG
docker push $REGISTRY/$APPNAME:$TAG

# notify-send "WEES" "Remote docker run executing"
echo $DOCKER_RUN

ssh root@$SERVER_SERVICE $DOCKER_RUN