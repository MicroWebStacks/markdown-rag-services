# Fetcher
Service for fetching data and storing it in cache. Fetcher offers an MQTT API endpoint.

## Topics API Endpoints

* `fetcher/status` : publishes readiness on startup
* `fetcher/fetch` : subscribes to handle a fech process
* `fetcher/fetch/start` : publishes job start confirmation
* `fetcher/fetch/finish` : publishes job finish confirmation
* `fetcher/resources/<resource-id>` : publishes details of each fetched resource
* `fetcher/error` : publishes errors e.g. unhandled exception

## JSON request

example

```json
{
    "type": "github",
    "repository": "MicroWebStacks/astro-big-doc",
    "ref": "main",
    "filter": "content/*",
    "resource": "test-website"
}
```

parameters

* `type` : source fetch service
* `repository` : `<Organization>/<repo>`
* `ref` : branch
* `filter` : optional for filtering content
* `resource` : a unique id between all requested resources
