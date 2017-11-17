var sistema = 0;
var interativa = 0;
var batch = 0;

function decision(context){
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');

    if (process == 0){
      ctx.fillRect(25, 25, 50, 50);
      process += 1;
    } else if (process == 1){
      ctx.fillRect(25, 80, 50, 50);
      process += 1;
    } else if (process == 2){
      ctx.fillRect(25, 135, 50, 50);
      process += 1;
    }
  }
}

function addSistema(){
  var canvas = document.getElementById("stack_process");
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');

    if (sistema == 0){
      ctx.fillRect(85, 25, 50, 50);
      sistema += 1;
    } else if (sistema == 1){
      ctx.fillRect(85, 80, 50, 50);
      sistema += 1;
    } else if (sistema == 2){
      ctx.fillRect(85, 135, 50, 50);
      sistema += 1;
    }
  }
  sistema += 1;
}

function addBatch(){
  var canvas = document.getElementById("stack_process");
  decision(canvas);
  interativa += 1;
}

function addInterativa(){
  var canvas = document.getElementById("stack_process");
  decision(canvas);
  batch += 1;
}
