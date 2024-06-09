# Markdown RAG Services
Markdown Retrieval Augmented Generation Services.

understand the structure of markdown and its elements (tables, diagrams,...) for search and retrieval augmented generation.

Makrdown documents are parsed, the Abstract Syntax Tree is then used for rendering and for creating an intermediate document model that includes elements of types 
* meta data (from the md front matter and others e.g. path, level, order,...)
* headings
* tables
* images
* code blocks
* paragraphs
* links
* references

Those elements are the basis of a rich search using a schema and a smart LLM embeddings that allows the models to extract proper information from those elements.

# Usage
start all services
```shell
docker compose up -d
```

or just the runner which will start all other services it depends on (mosquitto, fetcher, markdown, search)

```shell
docker compose run --rm runner
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
  * Markdown Content Parser https://github.com/MicroWebStacks/content-structure
  * Markdown Renderer https://github.com/MicroWebStacks/astro-big-doc
* diagrams-viewer : a webapp to test diagrams generation
* kroki https://kroki.io/ as diagrams generator with REST API. supported formats (plantuml, graphviz, mermaid, drawio,...). It also uses the following services
  * blockdiag
  * mermaid
  * bpmn
  * diagramsnet
* typesense : instant search engine https://typesense.org/docs/
* search : service that collects elements from documents and injects them in the typesense database.
* llm : embeddings and retrieval augmented generation

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
# Survey of related projects

* https://github.com/deepset-ai/haystack
  * embedding of markdown documents as plain text
  * optional embedding of meta data for each document
  * tables as structured element inside documents
