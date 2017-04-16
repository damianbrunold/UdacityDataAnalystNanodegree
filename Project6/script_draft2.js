// define size of chart and create svg element and x and y axes

var w = 800,
    h = 600,
    svg = d3.select("#chart")
            .append("svg")
            .attr("width", w)
            .attr("height", h),
    x = d3.scaleLinear().domain([1986, 2016]).range([50,780]),
    y = d3.scaleLinear().domain([0, 50000]).range([580, 20]);
            
// Load the data from the various csv files

var data, c1990, c1991, c1998, c1999, c2015;
d3.csv("timeseries.csv", function(d) { 
    d.Year = +d.Year;
    d.Refugees = +d.Refugees;
    return d;
}, function(error, d) {
    if (error) throw error;
    data = d;
    d3.csv("countries.csv", function(d) {
        d.Refugees = +d.Refugees; 
        d.Year = +d.Year;
        return d;
    }, function (error, d) {
        if (error) throw error;
        c1990 = filter_year(d, 1990);
        c1991 = filter_year(d, 1991);
        c1998 = filter_year(d, 1998);
        c1999 = filter_year(d, 1999);
        c2015 = filter_year(d, 2015);
        render();
    });
});
    
function filter_year(data, year) {
    return data.filter(function(d) { return d.Year == year; });
}
    
// Render the chart

function render() {
    var formatNum = d3.format("d");

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
    
    // add peak highlights using circles
    render_circle(4);
    render_circle(5);
    render_circle(12);
    render_circle(13);
    render_circle(29);
    
    // add peak values using labels
    render_label(4);
    render_label(5);
    render_label(12);
    render_label(13);
    render_label(29);
    
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

function render_circle(i) {
    svg.append("circle")
        .attr("stroke", "steelblue")
        .attr("fill", "steelblue")
        .attr("cx", x(data[i].Year))
        .attr("cy", y(data[i].Refugees))
        .attr("r", 5)
        .on("mouseover", function() {
            render_details(i);
        })
        .on("mouseout", function() { d3.select(".details").remove() });
}

function render_label(i) {
    svg.append("text")
        .attr("font-family", "Arial")
        .attr("font-size", "9pt")
        .attr("fill", "steelblue")
        .attr("font-weight", "bold")
        .attr("x", x(data[i].Year) - 45)
        .attr("y", y(data[i].Refugees) - 3)
        .text("" + data[i].Refugees);
}

function render_details(i) {
    var left = x(data[i].Year) + 10,
        detailsdata,
        palette = ["#0066ff", "#1a75ff", "#3385ff", "#4d94ff", "#66a3ff", "#80b3ff"];
        
    // select the correct details data
    if (i == 4) detailsdata = c1990;
    else if (i == 5) detailsdata = c1991;
    else if (i == 12) detailsdata = c1998;
    else if (i == 13) detailsdata = c1999;
    else if (i == 29) detailsdata = c2015;
    
    // if the bar would not fit to the right, place it to the left of the data point
    if ((left + 100) > w) {
        left = left - 100 - 3;
    }
    
    // add group element
    var g = svg.append("g").attr("class", "details");
    
    // add rect for each country contribution to create the bar chart
    g.selectAll("rect")
        .data(detailsdata)
        .enter()
        .append("rect")
        .attr("x", function (d, i) { return left; })
        .attr("y", function (d, i) {
            cum = 0;
            for (idx = 0; idx < i; idx++) {
                cum += detailsdata[idx].Refugees;
            }
            return y(cum) - (y(0) - y(d.Refugees));
        })
        .attr("width", "80")
        .attr("height", function (d) {
            return y(0) - y(d.Refugees);
        })
        .attr("fill", function(d, i) {return palette[i];})
        .attr("stroke", "#999")
        .attr("stroke-width", "1");
        
    // add text for each country to annotate the bar chart
    g.selectAll("text")
        .data(detailsdata)
        .enter()
        .append("text")
        .attr("font-family", "Arial")
        .attr("font-size", "9pt")
        .attr("fill", "#ccc")
        .attr("x", function (d, i) { return left + 3; })
        .attr("y", function (d, i) {
            cum = 0;
            for (idx = 0; idx < i; idx++) {
                cum += detailsdata[idx].Refugees;
            }
            return y(cum) - 4;
        })
        .text(function (d) {return d.Country; });
}    
