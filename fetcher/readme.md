# Fetcher
Service for fetching data and storing it in cache. Fetcher offers an MQTT API endpoint.

# Actions
Actions are an active way how to request a fetch through an MQTT topic

## Topics API Endpoints

* `fetcher/status` : publishes readiness on startup
* `fetcher/fetch` : subscribes to handle a fech process
* `fetcher/fetch/start` : publishes job start confirmation
* `fetcher/fetch/finish` : publishes job finish confirmation
* `fetcher/resources/<id>` : publishes details of each fetched resource
* `fetcher/error` : publishes errors e.g. unhandled exception

## JSON request

example publish on `fetcher/fetch`

```json
{
    "type": "github",
    "repository": "MicroWebStacks/astro-big-doc",
    "ref": "main",
    "filter": "content/*",
    "dest": "test-website"
}
```

parameters

* `type` : source fetch service
* `repository` : `<Organization>/<repo>`
* `ref` : branch
* `filter` : optional for filtering content
* `dest` : dest folder under `/fetch/`

# Watch
Watch is an event driven approach to enable the fetcher to fetch the data and notify when it is updated. Fetch config is taken from a `manifest.yaml`, and notifications are published on `fetcher/resources/<key>`.

## Github
By default, the fetcher always fetches the data once on startup, then listens to optional github webhooks on `/fetcher/github/`

```yaml
fetcher:
  - type: github
    repository: MicroWebStacks/astro-big-doc
    ref: main
    filter: content/*
    dest: test-website
```
It is also possible to poll github with a glboal schedule or a repo based schedule

```yaml
schedule: 0 2 * * 1-5
fetcher:
  - type: github
    repository: MicroWebStacks/astro-big-doc
    ref: main
    filter: content/*
    id: test-website
    schedule: 45 8-17 * * 1-5
```

before fetching github data, the fetcher first checks the `commit` and only do an actual fetch if it was updated. Then after fetching, the content `hash` is checked. Only if both have changed, a notification will be published on `fetcher/resources/<key>`.

## AWS S3

```yaml
fetcher:
  - type: aws_s3
    bucket: tbd
    key: tbd
```
