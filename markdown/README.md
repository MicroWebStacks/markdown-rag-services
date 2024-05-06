# Markdown Service
markdown data parser and website builder

Service that parses Markdown for data extraction and rendering

# Triggers
* `markdown/build` active trigger
* `fetcher/resources/markdown-content/#` auto trigger from fetcher

# API
* markdown/build
```json
{
    "resource": "raspi-website",
    "path": "/fetch/repos/HomeSmartMesh/website/content/3dprinting"
}
```
