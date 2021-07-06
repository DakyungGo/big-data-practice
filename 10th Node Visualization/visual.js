//plotly rendering
function drawingGraph(data, opt){
  Plotly.newPlot('myDiv',{
    data: data,
    layout: opt,
  });
}

//load facebook data by AJAX
function loadDailyTable(a){
  console.log(a);
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
      if(a == '1') parseHCLData(rows);
      else if(a == '2') parseVolumeData(rows);
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
function parseHCLData(rows){
  datas = rows.result
  datelst = [];
  highlst = [];
  closelst = [];
  lowlst = [];

  for(var i=0; i<datas.length; i++){
    datelst.push(datas[i].Date);
    highlst.push(datas[i].High);
    closelst.push(datas[i].Close);
    lowlst.push(datas[i].Low);
  }
  
  var high = {
    x: datelst,
    y: highlst,
    mode: 'lines',
    name: 'high'
  };

  var low = {
    x: datelst,
    y: lowlst,
    mode: 'lines',
    name: 'low'
  };

  var close = {
    x: datelst,
    y: closelst,
    mode: 'lines',
    name: 'close'
  }
  
  var graphdata = [high, low, close];

  var opt = {
    title : "HIGH, LOW, CLOSE",
    titlefont: {
        family: 'Courier New, monospace',
        size: 25,
        color: 'lightgrey'
    },
  };

  drawingGraph(graphdata, opt);
}


function parseVolumeData(rows){
  datas = rows.result
  datelst = [];
  volumelst=  [];

  for(var i=0; i<datas.length; i++){
    datelst.push(datas[i].Date);
    volumelst.push(datas[i].Volume);
  }

  var graphdata = [
    {
      x: datelst,
      y: volumelst,
      type: 'bar'
    }
  ];

  var opt = {
    title : "VOLUME",
    titlefont: {
        family: 'Courier New, monospace',
        size: 25,
        color: 'lightgrey'
    },
  };

  drawingGraph(graphdata, opt);
}
