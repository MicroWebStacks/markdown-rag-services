function fixSvgSize(){
    const svg = document.querySelector('#svgcontainer svg');
    if (svg) {
      // Check if 'width' and 'height' attributes are missing
      if (!svg.hasAttribute('width') || !svg.hasAttribute('height')) {
        const viewBox = svg.getAttribute('viewBox');
        if (viewBox) {
          const sizes = viewBox.split(' ');
          // Typically, the viewBox is "minX minY width height"
          const width = sizes[2];
          const height = sizes[3];
  
          svg.setAttribute('width', width);
          svg.setAttribute('height', height);
        }
      }
    }    
}

async function generateDiagram(){
    const diagramSelector = document.getElementById('diagramSelector').value;
    const diagramSource = document.getElementById('diagramSource').value;
    const url = baseURL +'/'+ diagramSelector + '/svg/'
    console.log(`POST @ ${url}`)
    const response = await fetch(url,{
        method: 'POST',
        body: diagramSource,
        headers: {
          'Content-Type': 'text/plain',
        },
      })
    const svgContent = await response.text();
    //console.log(svgContent)
    const svgContainer = document.getElementById('svgcontainer');

    const old_svg = document.getElementsByTagName("svg")
    //console.log(old_svg)
    if(old_svg.length){
        old_svg[0].remove()
    }
    svgContainer.innerHTML = svgContent;
    fixSvgSize()
}

async function updateExample(){
    let diagSelector = document.getElementById("diagramSelector")
    const format = diagSelector.value
    let textarea = document.getElementById("diagramSource")
    const selectedOption = diagSelector.options[diagSelector.selectedIndex];
    const filename = selectedOption.getAttribute('data-file')
    console.log(window.location.href +'examples/'+ filename)
    document.getElementById("filename").innerText = filename
    document.getElementById("format").innerText = format
    const response = await fetch(window.location.href +'examples/'+ filename)
    textarea.value = await response.text()
    generateDiagram()
}

function export_svg(){
    const svg_element = document.querySelector("svg")
    //console.log(svg_element)
    let s = new XMLSerializer();
    const svg_str = s.serializeToString(svg_element);
    var blob = new Blob([svg_str], {type: 'image/svg+xml'});
    let diagSelector = document.getElementById("diagramSelector")
    const selectedOption = diagSelector.options[diagSelector.selectedIndex];
    const filename = selectedOption.getAttribute('data-file') + ".svg"
    saveAs(blob,filename);
}

function init(){
    let generate = document.getElementById("generate")
    generate.onclick = generateDiagram
    let diagSelector = document.getElementById("diagramSelector")
    let export_button = document.getElementById("save")
    export_button.onclick = export_svg
    diagSelector.onchange = updateExample
    updateExample()

}

init()
