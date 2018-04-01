$(function(){
  $.get('/graph', function(result) {
    var style = [
      { selector: 'node[label = "tag1"]', css: {'background-color': '#fc1c20'}},
      { selector: 'node[label = "tag2"]', css: {'background-color': '#5bb5f5'}},
      { selector: 'edge',
        css: {
        //'target-arrow-shape': 'triangle',
        //'width': 1,
        'line-color': '#000000',
        //'target-arrow-color': '#000000'
        }
      }
    ];

    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: style,
      layout: { name: 'cose', fit: true },
      elements: result.elements
    });
  }, 'json');  
})