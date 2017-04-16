// define size of chart and create svg element

var w = 800,
    h = 600,
    svg = d3.select("#chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h);
            
// Load the data from the csv file

var data;
d3.csv("timeseries.csv", function(d) { 
    d.Year = +d.Year;
    d.Refugees = +d.Refugees;
    return d;
}, function(error, d) {
    if (error) throw error;
    data = d;
    render();
});

// Render the chart

function render() {
    var formatNum = d3.format("d");
    
    // create x scale
    var x = d3.scaleLinear()
        .domain([1986, 2016])
        .range([50,780]);
        
    // create y scale
    var y = d3.scaleLinear()
        .domain([0, 50000])
        .range([580, 20]);
        
    // create time series line
    var line = d3.line()
        .x(function(d) {return x(d.Year);})
        .y(function(d) {return y(d.Refugees);});
        
    // add group element containing the y axis
    svg.append("g")
        .attr("transform", "translate(50, 0)")
        .call(d3.axisLeft(y).tickFormat(formatNum))
        .select(".domain")
        .remove();
        
    // add group element containing the x axis
    svg.append("g")
        .attr("transform", "translate(0," + (h - 20) + ")")
        .call(d3.axisBottom(x).tickFormat(formatNum));
        
    // add the data line
    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 2.5)
        .attr("d", line);        

    // add descriptive chart title
    render_text("Refugee counts", "20pt", "450", "80");
    render_text("in Switzerland", "20pt", "450", "120");
}

function render_text(text, size, x, y) {
    svg.append("text")
        .attr("font-family", "Arial")
        .attr("font-size", size)
        .attr("fill", "steelblue")
        .attr("font-weight", "bold")
        .attr("x", x)
        .attr("y", y)
        .text(text);
}
