#!/usr/bin/env sh
if docker network ls | grep net; then
    echo "Network with net name was found. Skipping network creation."
else
    docker network create net
fi
