function getMaleGraphs() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    console.log(`State: ${this.readyState}`);
    // readyState == 4: request is complete, status == 200: request is successful
    if (this.readyState == 4 && this.status == 200) {
      var maleGraphs = JSON.parse(xhttp.responseText);
      var container = document.getElementById('GraphsContainer');
      container.innerHTML = ''; // Clear existing content

      for (var i = 0; i < maleGraphs.length; i++) {
        // Create a container for each row
        if (i % 3 === 0) {
          var rowContainer = document.createElement('div');
          rowContainer.classList.add('row-container');
          container.appendChild(rowContainer);
        }

        var img = document.createElement('img');
        img.src = maleGraphs[i];
        img.alt = `Graph ${i + 1}`;

        // Add each graph to the row container
        var rowContainers = document.querySelectorAll('.row-container');
        rowContainers[rowContainers.length - 1].appendChild(img);
      }
    }
  };

  xhttp.open('GET', 'data/male_graphs.json', true);
  xhttp.send();
}

function getFemaleGraphs() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    console.log(`State: ${this.readyState}`);
    // readyState == 4: request is complete, status == 200: request is successful
    if (this.readyState == 4 && this.status == 200) {
      var femaleGraphs = JSON.parse(xhttp.responseText);
      var container = document.getElementById('GraphsContainer');
      container.innerHTML = ''; // Clear existing content

      for (var i = 0; i < femaleGraphs.length; i++) {
        // Create a container for each row
        if (i % 3 === 0) {
          var rowContainer = document.createElement('div');
          rowContainer.classList.add('row-container');
          container.appendChild(rowContainer);
        }

        var img = document.createElement('img');
        img.src = femaleGraphs[i];
        img.alt = `Graph ${i + 1}`;

        // Add each graph to the row container
        var rowContainers = document.querySelectorAll('.row-container');
        rowContainers[rowContainers.length - 1].appendChild(img);
      }
    }
  };

  xhttp.open('GET', 'data/female_graphs.json', true);
  xhttp.send();
}
