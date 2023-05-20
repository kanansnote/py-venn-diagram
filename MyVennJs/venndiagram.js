<script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>

// ok, so let's create data

var data = [
    {x: "A", value: 100},
    {x: "B", value: 100},
    {x: "c", value: 100},
    {x: ["A", "B", "C"], value: 25}
];

// create a chart and set the data
chart = anychart.venn(data);

// configure labels of intersections
chart.intersections().labels().format("{%x}");

// set the container id
chart.container("container");

// initiating drawing the chart
chart.draw();
