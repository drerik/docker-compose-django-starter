# Docker django starter

NOTE: This is a work in progress. See [TODO.md](TODO.md)

This is a starter project to get up and running fast with django. Everything is packages with docker and docker-compose.


## Containers
The following applications is included in the basic docker setup.

### Nginx
Nginx is configured to automatically forward all traffic to the python app. uwsgi init file is mounted from the app container.

#### SSL certificates
We have added let's encrypt to generate certificates at build time. To renew your certificates, all you have to do is to do a new build of the docker container.

### PostgreSQL
We have set up a PostgreSQL database for your project. Access is configured trough the `docker-compose.yml` file.

### App (Python 3)
The default configuration to the containers is "in dev mode". Here we mount up the current directory over the `/usr/src/app` directory. You can now develop your application without having to rebuild the containers every time you do some changes to your code.


To make the installation "production" friendly, or if you need to run the application on an external server, you'll have to uncomment the following configuration in the `app` section in the `docker-compose.yml` config:
```
volumes:
  - "$PWD/app:/usr/src/app"
```

### Storage
A persistant storage volume is mounted on `/storage` in the app container. Store your persistent data here.

## Startup

### Startup in dev mode:

```
docker-compose build && docker-compose up -d postgres
docker-compose run --rm --no-deps -p 8000:8000 app bash
```

### Startup in production
Comment out the part in `docker-compose.yml` that mounts up current directory as the app path ( se the "App" section above ).

### Initial startup
```
docker-compose build
docker-compose up -d
```

### Upgrade ( preserving the storage containers )
```
docker-compose build
docker-compose up -d --no-deps app nginx postgres
```

## Links:
- http://www.django-rest-framework.org/
- http://uwsgi-docs.readthedocs.io/en/latest/index.html
