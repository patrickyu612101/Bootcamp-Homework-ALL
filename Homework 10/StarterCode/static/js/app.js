// from data.js
var tbody = d3.select("tbody");

var tableData = data;
data.forEach((tableData) => {
    var row = tbody.append("tr");
    
    Object.entries(tableData).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });

// YOUR CODE HERE!
var submit = d3.select("#submit");

submit.on("click", function() {
d3.event.preventDefault();

var inputElement = d3.select("#patient-form-input");

var inputValue = inputElement.property("value");

var filteredData = tableData.filter(tdate => tableData.datetime === inputValue);


});


