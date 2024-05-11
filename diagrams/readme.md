# Overview
text to diagram generator.

provided services
* REST API for direct text to diagram requests
* MQTT API endpoint for batch job
* web UI with a text editor to test diagrms generation with examples

target engines

* kroki : https://kroki.io/
* plantuml
* graphviz
* mermaid : https://www.mermaidchart.com/
* drawio

given that kroki has the same goal of wrapping multiple diagram generators engines, focus will be on kroki integration

# REAS API
Post to

```js
    const response = await fetch("http://localhost:7000/graphviz/svg",{
        method: 'POST',
        body: diagramText,
        headers: {
          'Content-Type': 'text/plain',
        },
      })
```
