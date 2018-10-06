function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`

    // Use `.html("") to clear any existing metadata

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
    // console.log(JSON.stringify(sample));
}

function buildCharts(sample) {
  var pieplace=d3.select("#pie"); 
  d3.json(`/samples/${sample}`).then((datad)=>{
    var aid=datad["otu_ids"];
    var alb=datad["otu_labels"];
    var asv=datad["sample_values"];
    var ids=datad["otu_ids"].slice(0,10);
    var lb=datad["otu_labels"].slice(0,10);
    var sv=datad["sample_values"].slice(0,10);
    console.log(sample)
    console.log(datad);
    console.log(ids);
    console.log(lb);
    console.log(sv);
    var trace1 = {
    labels: ids,
    values: sv,
    hovertext:lb,
    type: 'pie'
      };
    var trace2={
      x:aid,
      y:asv,
      hovertext:alb,
      mode:"markers",
      marker:{
        size:asv,
        color:aid
      }
    }
var data = [trace1];
var data2=[trace2];

Plotly.newPlot("pie", data);
Plotly.newPlot("bubble", data2);
    

   
  });
  // @TODO: Use `d3.json` to fetch the sample data for the plots

    // @TODO: Build a Bubble Chart using the sample data

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // const left = names.slice(0, 2);
    // otu_ids, and labels (10 each).
}
// id.append(h2).text.(retuned.json)

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    // console.log(firstSample);
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
