//plotly rendering
function drawingGraph(data, opt){
  Plotly.newPlot('myDiv',{
    data: data,
    layout: opt,
  });
}

//load facebook data by AJAX
function loadDailyTable(){

  var url = '';
  var from_date = document.getElementById("datepicker1").value;
  var to_date = document.getElementById("datepicker2").value;

  //setting date for query
  if(to_date.length == 0 || from_date.length == 0){
    from_date = "2017-02-02";
    to_date = "2018-02-02";
  }
  
  url = "/finance/open/" + from_date + "/" + to_date;

  $.ajax({
    type: "GET",
    url: url,
    success: function(rows){
      parseDailyData(rows);
      return false;
    },
    error: function(xhr, status, err){
      console.log(xhr.responseText);
      var err = '';
      $.each(JSON.parse(xhr.responseText), function(i, item){
        err += '<li>' + item.msg + '</li>'
      });
      console.log(err);
      return false;
    }
  });
}

//data parsing and set configuration
function parseDailyData(rows){
  datas = rows.result
  console.log(datas);
  datelst = [];
  openlst = [];

  for(var i=0; i<datas.length; i++){
    datelst.push(datas[i].Date);
    openlst.push(datas[i].Open);
  }

  var graphdata = [
    {
      x: datelst,
      y: openlst,
      mode: 'lines+markers',
      type: 'scatter'
    }
  ];

  var opt = {
    title : "FACEBOOK RECENT OPEN PRICE",
    titlefont: {
        family: 'Courier New, monospace',
        size: 25,
        color: 'lightgrey'
    },
    xaxis: {
      title: 'DAILY',
      titlefont: {
        color: 'lightgrey'
      },
      zeroline: true,
      showline: true,
      mirror: 'ticks',
    }
  };

  drawingGraph(graphdata, opt);
}


