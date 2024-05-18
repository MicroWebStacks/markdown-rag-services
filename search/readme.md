
# Actions
```yaml
- action: search/collect
  resource: test-website
- action: search/inject
  resource: test-website
```

## Collect
breaks document_list using a schema into into elements of type :
* headings
* tables
* images
* codes
* paragraphs

keeps heading and references to the original document

## Inject

