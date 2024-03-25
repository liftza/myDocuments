
class ChartManager {
    constructor() {

    }

     initializeChart(data) {
            var chart1 = LightweightCharts.createChart(document.getElementById("firstContainer"), { width: 500, height: 300 });
            var lineSeries1 = chart1.addLineSeries();
            lineSeries1.setData(data);
            
            chart1.timeScale().fitContent();
      }



      rubber(data){
        var chartOptions = { width:500 ,
                             height: 300 ,
                             layout: { textColor: 'blue', background: { type: 'solid', color: 'white' } },
                             
                          };
        var chart = LightweightCharts.createChart(document.getElementById("secondContainer"),chartOptions);
        var lineSeries = chart.addLineSeries({ color: 'black' });
        lineSeries.setData(data);
        const minPriceLine = {
          price: 30,
          color: '#ef5350',
          lineWidth: 2,
          lineStyle: 2, // LineStyle.Dashed
          axisLabelVisible: true,
          title: 'bath',
      };
      lineSeries.createPriceLine(minPriceLine);
        
        chart.timeScale().fitContent();

      }

      addData(data){
        var chart = LightweightCharts.createChart(document.getElementById("firstContainer"), { width: 500, height: 300 });
        var lineSeries1 = chart.addLineSeries();
        lineSeries1.setData(data);
        chart.timeScale().fitContent();
      }

}

const manager = new ChartManager();
