const widthGrid = 400;
const heightGrid = 400;

const widthLegend = 600;
const heightLegend = 20;
const numberOfLegends = 10;
const maxPrice = 300;

d3.json("https://raw.githubusercontent.com/amadorsoy/keepCodingBootCampBDML/master/modernvisualization/datosjson/practica.json")
    .then( (dataGeoJson) => {
        drawMap(dataGeoJson);
    } 
);


function drawMap(dataGeoJSon) {
    //First Hide Timer Spinner
    hideSpinner();

    //Use a SchemaCategory10 for Scale Color (map, legend)
    const scaleColor = d3.scaleOrdinal(d3.schemeCategory10);   

    /*All the steps to draw the map - START*/
    //Use a div for a tooltip message with AVG Price.
    const divToolTip = d3.select('#tooltip');
    //Get All Features from GeoJSon Object
    const featuresGeoJSon = dataGeoJSon.features;
    //Use projectPoint function for transform
    const transform = d3.geoTransform({ point: projectPoint });
    //Use transform for the projection
    const path = d3.geoPath().projection(transform);
    //Get Center Position from GeoJSon Object
    const mapCenterInitial = d3.geoCentroid(dataGeoJSon);
    //Get from Function LeafLet Map
    const mapLeafLet = createLeaflet(mapCenterInitial);
    //Agregate SVG to LeafLet Map
    const svgMapLeafLet = getSVGLeafLet(mapLeafLet);    
    //Add a Group to SVG Object
    const mapGroupLeafLet = svgMapLeafLet
        .append('g');
    //create Path Objects from GeoJSon Features, fill with scaleColor, agregate tooltip and clic event...
    const features = mapGroupLeafLet.selectAll('path')
        .data(featuresGeoJSon)
        .enter()
        .append('path')
        .attr('fill', (feature) => {
            let minColorRange = 0;
            let maxColorRange = maxPrice / numberOfLegends;
            let index = 0;
            let price = feature.properties.avgprice || 0;
            while ( ( price >= minColorRange && price <= maxColorRange) === false ) {
                index += 1;
                minColorRange = maxColorRange + 1;
                maxColorRange += 30;
            }            
            return scaleColor(index);
        })
        .on('click', function (feature){
            createGraphic(feature);
        })
        .on('mouseover', function(feature){
            showMoveToolTip(feature, divToolTip);
        })
        .on('mousemove', function(feature){
            showMoveToolTip(feature, divToolTip);
        })
        .on('mouseout', function(feature){
            divToolTip.style("opacity", 0);
        });

    //Use Zoomend to reset position to paths and position for the first time
    mapLeafLet.on('zoomend', reset);
    reset();

    //Previously used functions (in drawmap)
    function projectPoint(x, y) {
        var point = mapLeafLet.latLngToLayerPoint(new L.LatLng(y, x));
        this.stream.point(point.x, point.y);
    }
    
    function showMoveToolTip(feature, div) {
        const preciomedio = feature.properties.avgprice !== undefined ? feature.properties.avgprice : 0;
        div
            .transition()
            .duration(200)
            .style("opacity", .9)
            .style("left", (event.pageX+10) + "px")
            .style("top", (event.pageY-10) + "px")
            .text(`${feature.properties.name} - Average Price: ${preciomedio}`);
    }

    function reset() {
        divToolTip.style("opacity", 0);

        const bounds = path.bounds(dataGeoJSon);
        const topLeft = bounds[0];
        const bottomRight = bounds[1];
    
        svgMapLeafLet
            .attr("width", bottomRight[0] - topLeft[0])
            .attr("height", bottomRight[1] - topLeft[1])
            .style("left", topLeft[0] + "px")
            .style("top", topLeft[1] + "px");
    
        mapGroupLeafLet
            .attr("transform", `translate(${-topLeft[0]}, ${-topLeft[1]})`);
    
        features.attr("d", path);
      }

    /*All the steps to draw the map - START*/
    const svgLegend = getSVG('#legendmap')
        .attr("height", heightLegend + 5)
        .attr("width", widthLegend);
    const legend = svgLegend.append('g').attr('class', 'legend');
    const scaleLegend = d3.scaleLinear()
      .domain([0, numberOfLegends])
      .range([0, widthLegend]);
    let minColorRange = 0;
    let maxColorRange = 30;
    for (let index=0; index < numberOfLegends; index += 1) {        
        const posx = scaleLegend(index);
        const legendGroupIndex = legend
            .append('g')
            .attr('transform', `translate(${posx}, 0)`);
        const rectColorLegendGroupIndex = legendGroupIndex
            .append('rect');
        const textColorLegendGroupIndex = legendGroupIndex
            .append("text");
        const widthRect = (widthLegend / numberOfLegends) - 2;
        rectColorLegendGroupIndex
            .attr('width', widthRect)
            .attr('height', heightLegend)
            .attr('fill', scaleColor(index));
        textColorLegendGroupIndex
            .style("color", "black")
            .style("font-size", "small")
            .attr("x", 1)
            .attr("y", 15)
            .text(`${minColorRange}-${maxColorRange}€`);
        minColorRange = maxColorRange + 1;
        maxColorRange += 30;
    }

}

function createGraphic(feature){
    console.log(feature);
    if (d3.select('#grid').select("svg") != undefined){
        d3.select('#grid').select("svg").remove();
    }
    const svgGraphic = getSVG("#grid");
    svgGraphic
        .attr("width", widthGrid + 100)
        .attr("height", heightGrid + 100);

    if (feature.properties.avgbedrooms.length == 0){
        const text = svgGraphic
            .append("text")
            .attr("x", 20)
            .attr("y", heightGrid / 2)
            .text("No data to show, sorry for the inconvenience.");
    } else {

        const scaleY = getScalarY(feature.properties.avgbedrooms);
        const scaleX = getScalarX(feature.properties.avgbedrooms);
        
        const dataLine = d3.line()
            .x( d => scaleX(d.bedrooms))
            .y( d => scaleY(d.total));
        
        const groupGraphic = svgGraphic
            .append("g")
            .attr("left", 10)
            .attr("width", widthGrid + 50)
            .attr("height", heightGrid + 50);

        const pathLine = groupGraphic.append("path");
        pathLine.attr("class", "line");

        pathLine
            .attr("fill", "none")
            .attr("stroke", "blue")
            .attr("stroke-width", 1)
            .attr("transform", `translate(30, 5)`)
            .attr("d", dataLine(feature.properties.avgbedrooms));

        const axisY = d3.axisLeft(scaleY).ticks(5);

        groupGraphic
            .append("g")
            .attr("transform", `translate(30, 10)`)
            .style("fill", "black")
            .call(axisY);

        const axisX = d3.axisBottom(scaleX).ticks(5);

        groupGraphic
            .append("g")
            .attr("transform", `translate(30, ${heightGrid + 5 })`)
            .style("fill", "black")
            .call(axisX);
    }
}

function getScalarY(avgBedrooms){
    const scaleY = d3.scaleLinear()
        .domain(d3.extent(avgBedrooms, (data) => data.total ))
        .range([heightGrid, 0]);
    return scaleY;
}

function getScalarX(avgBedrooms){
    const scaleX = d3.scaleLinear()
        .domain(d3.extent(avgBedrooms, (data) => data.bedrooms ))
        .range([0, widthGrid]);
    return scaleX;
}



function getSVG(divId) {
    return d3.select(divId)
        .append("svg");
}

function getSVGLeafLet(mapLeafLet){
    return d3.select(mapLeafLet.getPanes().overlayPane)
        .append("svg");
}

function hideSpinner(){
    $(document).ready( function()
    {
        var element = document.getElementById('spinnerObject');
        element.classList.add('spinnerObject');
    });
}

function createLeaflet(center) {
    const map = L.map('map', {center: [center[1], center[0]], zoom: 10 });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    return map;
}