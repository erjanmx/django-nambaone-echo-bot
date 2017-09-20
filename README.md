# Django Namba-One Bot

Docker: Django, uWSGI and Nginx in a container, using Supervisord

### Build and run
#### Build with python3
* `docker build -t webapp .`
* `docker run -d -p 80:80 webapp`
* go to 127.0.0.1 to see if works

#### Build with python2
* `docker build -f Dockerfile-py2 -t webapp .`
* `docker run -d -p 80:80 webapp`
* go to 127.0.0.1 to see if works
