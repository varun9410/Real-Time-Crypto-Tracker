var bitcoin_array = [];
var ethereum_array = [];
var dogecoin_array = [];
var xValues = [];
var today = new Date();
socket.on("my_response", function (result) {
  console.log(result);
  document.getElementById("bitcoin").innerHTML = result[0];
  bitcoin_array.push(result[0]);
  document.getElementById("ethcoin").innerHTML = result[1];
  ethereum_array.push(result[0]);
  document.getElementById("dogecoin").innerHTML = result[2];
  dogecoin_array.push(result[0]);
  xValues.push(today.getSeconds());
});
new Chart("myChart", {
  type: "line",
  data: {
    lables: xValues,
    datasets: [
      {
        fill: true,
        lineTension: 0.3,
        pointRadius: 0,
        backgroundColor: "skyblue",
        borderColor: "rgba(0,0,255,0.1)",
        data: bitcoin_array,
      },
    ],
  },
  options: {
    legend: { display: false },
    scales: {
      yAxes: [{ ticks: { min: 0, max: 10000 }, gridLines: { display: false } }],
      xAxes: [{ gridLines: { display: false } }],
    },
  },
});
var xValues = ["Bitcoin", "Ethurum", "Dogecoin"];
var yValues = [1321, 3123, 234];
var barColors = ["red", "green", "orange"];

new Chart("myBar", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: barColors,
        data: yValues,
      },
    ],
  },
  options: {},
});
