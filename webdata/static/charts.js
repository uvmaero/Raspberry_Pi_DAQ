$(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "damper 1",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'title 2'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };

    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "another damper",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Creating Real-Time Charts with Flask'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };

    const context = document.getElementById('canvas').getContext('2d');
	var canvas = document.getElementById('canvas');
	canvas.width = 700;
	canvas.height = 600;
	canvas.style.left = "100px";
	canvas.style.top = "100px";
	canvas.style.position = "absolute";

        const lineChart = new Chart(context, config);

        const source = new EventSource("/rideHeight");

        source.onmessage = function (event) {
            const data = JSON.parse(event.data);
            if (config.data.labels.length === 20) {
                config.data.labels.shift();
                config.data.datasets[0].data.shift();
            }
            config.data.labels.push(data.time);
            config.data.datasets[0].data.push(data.value);
            lineChart.update();
        }

        const context = document.getElementById('damper2').getContext('2d');
        var canvas = document.getElementById('damper2');
        canvas.width = 900;
        canvas.height = 700;
        canvas.style.left = "100px";
        canvas.style.top = "300px";
        canvas.style.position = "relative";
    
            const lineChart = new Chart(context, config);
    
            const source = new EventSource("/VandC");
    
            source.onmessage = function (event) {
                const data = JSON.parse(event.data);
                if (config.data.labels.length === 20) {
                    config.data.labels.shift();
                    config.data.datasets[0].data.shift();
                }
                config.data.labels.push(data.time);
                config.data.datasets[0].data.push(data.value);
                lineChart.update();
            }
    });