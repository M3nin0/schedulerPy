cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

var sistema = 0;
var interativa = 0;
var batch = 0;

function reset(){
    // Reset das variaveis globais
    sistema = 0;
    interativa = 0;
    batch = 0;

    var canvas = document.getElementById("stack_process");
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, 171, 221);
}

function decision(canvas, process){
  if (canvas.getContext){

    var ctx = canvas.getContext('2d');
    ctx.fillStyle = cores['pronto'];

    if (process == 0){
      ctx.fillRect(96, 25, 38, 38);
      process += 1;
    } else if (process == 1){
      ctx.fillRect(96, 80, 38, 38);
      process += 1;
    } else if (process == 2){
      ctx.fillRect(96, 135, 38, 38);
      process += 1;
    } else if (process == 3){
      ctx.fillRect(96, 185, 38, 38);
      process += 1;
    }
  }
}
function addSistema(){
  var canvas = document.getElementById("stack_process");
  decision(canvas, sistema);
  sistema += 1;
}

function addBatch(){
  var canvas = document.getElementById("stack_process");
  decision(canvas, interativa);
  interativa += 1;
}

function addInterativa(){
  var canvas = document.getElementById("stack_process");
  decision(canvas, batch);
  batch += 1;
}

function escalonaSistema(){

}

function escalonaInterativa(){

}

function escalonaBatc(){

}
