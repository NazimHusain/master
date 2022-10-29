

//Time Block====================
setInterval(display,500); 
function display(){
   var time = new Date();
   var hour =time.getHours();
   var min = time.getMinutes();
   var sec = time.getSeconds();
    var en ='AM';
   if (hour>=12){ en='PM'}
   
   if (hour>12){
       hour=hour-12;
   }
   if (hour ==0){
       hour=12; 
   }
   if (hour<10){ houur='0'+hour};
   if (min<10){ min ='0'+min};
   if (sec<10){sec='0'+sec}
 
   document.getElementById('clock').innerHTML=hour+ ':' +min+ ':'+sec + ' '+en;
}