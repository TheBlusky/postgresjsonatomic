#!/bin/sh
apk add curl

while [ "$(curl http://django:8000/create_model/ 2>/dev/null)" != "Ok" ]; do
  sleep 10;
done;

curl http://django:8000/append_data/\?some_value\=1 &
curl http://django:8000/append_data/\?some_value\=2 &
curl http://django:8000/append_data/\?some_value\=3 &
curl http://django:8000/append_data/\?some_value\=4 &
curl http://django:8000/append_data/\?some_value\=5 &
curl http://django:8000/append_data/\?some_value\=6 &
curl http://django:8000/append_data/\?some_value\=7 &

sleep 3600