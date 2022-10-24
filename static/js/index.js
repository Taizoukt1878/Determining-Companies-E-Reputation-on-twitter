let chart = document.getElementById('myChart').getContext('2d');
        //Chart.defaults.global.defaultFontFamily = '#777';
        let barchart = new Chart(myChart, {
            type : 'pie',// bar, horizontalbar,pie, line, radar
            data : {
                labels : ['negative', 'positive'],
                datasets: [{
                label : 'Tweets',
                data: [
                    {{ neg | safe }},
                    {{ pos | safe }}
                ],
                backgroundColor: [
                    'red',
                    'lightgreen',
                ],

                hoverBorderWidth : 2,
                hoverBorderColor : 'black'

                }]
            },
            options:{
                title:{
                    display:true,
                    text:'bigest cities'
                },
                legend:{
                    position:true
                }
            }

        });