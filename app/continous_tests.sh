#!/bin/bash

counter=1
while [ $counter -le 1000 ]
  do
    echo $counter
    ((counter++))
    docker-compose exec web pytest -s -p no:warnings
    sleep 5
  done
echo 1000 test cycle Completed
osascript -e 'display notification "1000 test cycle Completed"'
