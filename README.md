# MOVIE REVIEWS.

[![Build Status](https://travis-ci.org/Shais14/cicd-movielist.svg?branch=master)](https://travis-ci.org/Shais14/cicd-movielist)

This is a pyhton web app that provides reviews about movies. The app is still in development phase and will be updated frequetnly. As of now, this app provides random reviews for a bunch of movies. 

## TechStack

This application is developed in python. I use pytest to test the application. Travis CI is used as a build manager and CI tool. The applicaion is deployed on Heroku. Every commit/pull request on master branch triggers a build and if the build is successful, a new docker image of the application is made and registered on the dockerhub registry, which is then pulled to deploy on Heroku. 

## Demo app

https://cicd-moviereview.herokuapp.com/ 
