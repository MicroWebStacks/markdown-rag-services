# website_services
Copper pipeline for markdown website building

# Usage

run both docker compsoe files from the root and from the `./copper` submodule

```shell
cd copper
docker compose up -d
cd ..
cd markdown
docker compose up -d
```

the root `workflow.yaml` will be executed by the runner that pulishes each action topics and subscribes to wait for the action to finish

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
```

certificate creation in git bash
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./certs/localhost.key -out ./certs/localhost.crt -subj "//CN=localhost"
```