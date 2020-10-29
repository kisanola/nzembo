#!/bin/sh
echo POSTGRES_HOST=$POSTGRES_HOST >> .env.production
echo SHA=$SHA >> .env.production
echo POSTGRES_DATABASE=$POSTGRES_DATABASE >> .env.production
echo POSTGRES_USER=$POSTGRES_USER >> .env.production
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env.production
echo DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY >> .env.production
echo DJANGO_ADMIN_URL=$DJANGO_ADMIN_URL >> .env.production
echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .env.production
