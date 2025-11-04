#!/bin/bash
# Script to check Heroku app status
echo "Checking Heroku app status..."
heroku apps:info --app mcq-reader

echo "Checking dyno types and status..."
heroku ps --app mcq-reader

echo "Checking installed buildpacks..."
heroku buildpacks --app mcq-reader

echo "Checking environment variables..."
heroku config --app mcq-reader

echo "Checking most recent releases..."
heroku releases --app mcq-reader