var grafica1= document.getElementById("grafica2").getContext("2d");
var myChart= new Chart(grafica1,{
    type:"pie",
    data:{
        labels:["Barranquilla","Soledad"],
        datasets:[{
                label:"Citas por sede en esta semana ",
                data:[50,39],
                backgroundColor:[
                    'rgb(220, 180, 255)',
                    'rgb(173, 216, 230)'
                ]
        }]
    },
    options:{
        scales:{
            yAxes:[{
                    ticks:{
                        beginAtZero:true
                    }
            }]
        }
    }
});