# Local test

```bash
docker run -p 9000:8080 text-embedding
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"sentence":"This is a command line curl sentence!"}'
```


# AWS Lambda
* Step 1 : upload the image to ECR

```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 031028648877.dkr.ecr.eu-central-1.amazonaws.com

docker build -t text-embedding .

docker tag text-embedding:latest 031028648877.dkr.ecr.eu-central-1.amazonaws.com/microweb-containers:embed-latest

docker push 031028648877.dkr.ecr.eu-central-1.amazonaws.com/microweb-containers:embed-latest

```

* Step 2 : Create and Configure the Lambda
    * Memory size tbd e.g. 512 BM
    * env var HF_HOME = /tmp

## excutions
* 512MB  44s
* 1024MB 10s
* 2048MB  7s

* 2048MB
    * init duration : 22s: model load 3.5s, encode 11.5s
    * folloups 15ms

cold starts : 22s ~ 17s
warm starts : 14ms ~ 20ms

