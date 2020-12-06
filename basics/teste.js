let valor = 5

// for(let i=1;i<=valor;i++){
//   let divisores = 0;
//   for(let j=1;j<=i;j++){
//     let resto = i%j;
//     if(resto===0){
//       divisores+=1;
//     }
//   }
//   if(divisores===2){
//     console.log(i)
//   }
// }

let a = 0

for(let linhas=0;linhas<3;linhas++){
  for(let colunas=0;colunas<3;colunas++){
    console.log(' ',a++)
    // console.log('\n')
  }
}