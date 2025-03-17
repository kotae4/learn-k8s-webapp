# kubernetes-experiment-webapp

**A simple webapp built with flask.**

Learning about kubernetes core concepts with a simple, microservice-based application. It's very messy and a lot of stuff is hardcoded, but that's okay because it's just for learning.

The **learn-k8s-webapp** microservice, its own deployment in the k8s cluster, is a flask app that serves the frontend and talks to the API.<br>
The [learn-k8s-apiserver-net](https://github.com/kotae4/learn-k8s-apiserver-net) microservice, a separate deployment in the cluster, is an asp.net app that handles requests from the webapp backend and talks to the database.<br>
The database is external (exists outside the cluster). This example will use a local mariadb DB, but could be adapted to use AWS RDS or some other cloud provider's RDBMS.<br>

## Notes on running

It expects the [learn-k8s-apiserver-net](https://github.com/kotae4/learn-k8s-apiserver-net) microservice to be available at `http://api.testing.private:27525`.

## Containerization

Networking:
```bash
# to begin:
docker network create learn-k8s-network
# once done:
docker network remove learn-k8s-network
```

Building:
```bash
docker build -t learning-k8s-webapp:latest .
```

Running:
```bash
docker run --rm -d --name webapp --network learn-k8s-network -p 80:80 -e BACKEND_HOST=apiserver -e BACKEND_PORT=8080 learning-k8s-webapp
```

## Locally

Create a .flaskenv file with this:
```
FLASK_APP=learn-k8s-webapp
FLASK_RUN_PORT=27580
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
```

Then invoke:
`flask --app learn-k8s-webapp run --debug`.

## Regenerating votingApi client

1. Run [learn-k8s-apiserver-net](https://github.com/kotae4/learn-k8s-apiserver-net) and open up <apiserver>/swagger/v1/swagger.json.
2. Download swagger-codegen-cli (change version number if needed, [see here](https://github.com/swagger-api/swagger-codegen))
    ```
    # wget available
    wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.50/swagger-codegen-cli-3.0.50.jar -O swagger-codegen-cli.jar
    # windows powershell (no wget)
    Invoke-WebRequest -OutFile swagger-codegen-cli.jar https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.50/swagger-codegen-cli-3.0.50.jar
    ```
3. Point your terminal at the `learn-k8s-apiserver-net` directory
4. `java -jar .\swagger-codegen-cli-3.0.47.jar generate -i openapi.json -l python -o votingApi -DpackageName=votingApi`
5. Copy the votingApi directory back into `learn-k8s-webapp` directory
6. Remove all code dealing with multiprocessing in `votingApi/api_client.py` if needed (AWS Lambdas)
7. Open `votingApi/configuration.py` and make sure the host matches expectations (default: `http://api.testing.private:27525`)
