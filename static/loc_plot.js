
make_plot()

function make_plot(){
	console.log(loc_data);
	var canvas = document.getElementById('lines_of_code_plot');
	var ctx = canvas.getContext('2d');
	
	var data = {
		datasets: [
			{ //here we need to make sure the data is in date order or we the connecting line is silly
				data: [{x: '2021-07-15T00:00:00', hash: 789232, y: 2938}, {x: '2021-07-21T12:00:00', anotherhash: 238298, y: 2911}, {x: '2021-08-11T00:00:00', y: 3014} ],
				showLine: true,
				pointBackgroundColor: 'rgba(0,0,0,1.0)'
			}
		]
	};
	
	var myChart = new Chart(ctx, { type: 'scatter', data ,
      	options: { responsive:true,
              legend: {
		      	display:false
	      },
		title:{
			text:'Lines of Code',
			display:true},
		scales:{
			   yAxes: [{
                         scaleLabel:{
                                labelString: "Lines of Code",
                                display: true
                         	},
                 	}],
                	 xAxes: [{
                         	scaleLabel:{
                          	labelString: 'date',
                          	display: true
                         	},
                          	type: 'time',
                          	position: 'bottom',
                 	}],
             	}
	}
	});
}

