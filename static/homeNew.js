var a;

// function show_hide(){
//     if(a==1){
//         document.getElementById('container-inbox').style.display="inline";
//         return a=0;
//     }
//     else{
//         document.getElementById('container-inbox').style.display="none";
//         return a=1;
//     }
// }
function show_hide(){
    document.getElementById('container-inbox').classList.toggle('active');
}