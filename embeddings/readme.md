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

## excutions
|memory |cold | warm |
|------|-----|-----|
|780 / 2048  MB| 17 s | 13 ms|

First boot

* Duration: 9231.42 ms
* Billed Duration: 17242 ms
* Memory Size: 2048 MB
* Max Memory Used: 779 MB
* Init Duration: 8009.97 ms
* model load 600 ms
* first encode call 9 s : this is a cloud only delay => Init Duration

Cold reboot
* Duration: 534.84 ms
* Billed Duration: 5461 ms
* Memory Size: 2048 MB
* Max Memory Used: 779 MB
* Init Duration: 4926.14 ms	
