# Markdown Service
markdown data parser and website builder

Service that parses Markdown for data extraction and rendering

# API
## Topics
* `markdown/build` topic to trigger build
```json
{
    "resource": "raspi-website",
    "path": "/fetch/repos/HomeSmartMesh/website/content/3dprinting"
}
```

* `markdown/status` connected / disconnected

# Internal variable
## Environment variables
* `CONTENT`     : source markdown content directory
* `STRUCTURE`   : output of the indexed markdown structure
* `PUBLIC_BASE` : base url of the website to be generated
* `OUT_DIR`     : output of the generated website
