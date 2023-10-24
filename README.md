# fastapi-docker-template

To run the project

```
$ docker-compose build
$ docker-compose up -d
```

Navigate to http://localhost:8004/ping.

JSON response:

```
{
  "ping": "pong!",
  "environment": "dev",
  "testing": false
}
```
