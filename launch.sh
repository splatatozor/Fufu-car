#!/bin/sh

ps auxw | grep flask | grep -v grep > /dev/null

if [ $? != 0 ]
then
        cd Fufu-car-api/
        export FLASK_APP=api.py
        flask run --host=0.0.0.0
fi