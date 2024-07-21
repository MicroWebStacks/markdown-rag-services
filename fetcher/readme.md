# Fetcher
Service for fetching data and storing it in cache. Fetcher offers an MQTT API endpoint.

# Fectch Actions
Actions represent a way how to trigger fetches from an external service through an MQTT topic

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

# Auto Fetch
In addition to data being always fetched once on startup, auto fetching will be performed in two possbile modes :
* Polling : on startup and based on a schedule
* Event triggered : this is source specific
  * Github : through webhooks
  * S3 : Through Simple Notification Service

In every situation where the data is updated (after polling or source specific event), a notification will be published on the local MQTT broker. Fetch config is taken from a `manifest.yaml`, and notifications are published on `fetcher/resources/<key>`.

## Github
The github webhooks url is defined as `/fetcher/github/`, and needs to be activated in the config.

```yaml
fetcher:
  - type: github
    repository: MicroWebStacks/astro-big-doc
    ref: main
    filter: content/*
    dest: test-website
    webhook: true
```

It is also possible to poll github with a global schedule or a repo based schedule

```yaml
schedule: 0 2 * * 1-5
fetcher:
  - type: github
    repository: MicroWebStacks/astro-big-doc
    ref: main
    filter: content/*
    id: test-website
    schedule: global
```

```yaml
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
The AWS bucket events are fixed to
```yaml
events:
  - s3:ObjectCreated:*
  - s3:ObjectRemoved:*
```
An event based fetching requires the sns topic
```yaml
fetcher:
  - type: aws_s3
    bucket: <bucket-name>
    key: <key-pattern>  # This could be a specific key or a wildcard pattern
    sns_topic: <sns-topic-arn>
```

as a fallback, it is also possible to configure an S3 fetcher with a polling schedule

```yaml
fetcher:
  - type: aws_s3
    bucket: <bucket-name>
    key: <key-pattern>  # This could be a specific key or a wildcard pattern
    schedule: 45 8-17 * * 1-5 # 'global' or a cron job notation string
```
