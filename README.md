# Markdown RAG Services
markdown parser and llm embeddings for a website generator with instant search and retrieval augmented generation.

# Usage

```shell
docker compose up -d
```

# How does it work

the root `workflow.yaml` will be executed by the runner service that pulishes each action topics and subscribes to wait for the action to finish

example
```yaml
- action: fetcher/fetch
  type: github
  repository: MicroWebStacks/astro-big-doc
  ref: main
  filter: content/*
  resource: test-website
- action: markdown/build
  resource: test-website
  path: /fetch/test-website/content
- ...
```

# Services
* mosquitto : MQTT broker to manage services end points
* runner : bootstraps execution of actions from a yaml workflow file
* fetcher : executes fetch actions such as retrieve repos from github
* markdown : parse, index and render markdown
* diagrams-viewer : a webapp to test diagrams generation
* kroki as diagrams generator with REST API. supported formats (plantuml, graphviz, mermaid, drawio,...). It also uses the following services
  * blockdiag
  * mermaid
  * bpmn
  * diagramsnet
* typesense : instance search engine
* search : service that collects elements from documents and injects them in the typesense database.
* llm : embeddings generation and retrieval augmented generation

# Development
all services can also run without containers, as the directories mapping respect the same relative path usage outside and inside the containers.

example
```shell
cd fetcher
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
(venv)# python fetcher.py
```

# Administration

example creation of self signed certificates for testing purpose

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./certs/localhost.key -out ./certs/localhost.crt -subj "//CN=localhost"
```

