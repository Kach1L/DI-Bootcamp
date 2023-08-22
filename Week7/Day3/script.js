// Scope Review
// var x = 6;
// let x = 9;
// const A = 'a'

// let x = 8;
// let x = 3;
// {
//  let x = 9;
// }

// console.log("x=>", x);
// for (var i = 0; i < 5; i++) {}
// console.log("i=>", i);

// function x(){
//     let x = 8;
//     function y(){
//         let a = 7;
//         console.log('x=>',x);
//     }
//     console.log('a=>',a);
// }
// x()
// function x(){
//     console.log('hello');
// }

// Error bcos xx is declared after the console log
// console.log(xx); 
// let xx = 6;


// function getXY(x=5,y=5){
//     return x+y
// }

// let sum = getXY(7,7)
// console.log(sum)

// function x(param){
//     function y(param1){
//         return param + param1;
//     }
//     return y;
// }

// let sum = x(3);
// console.log('sum=>',sum);


/* Currying */

// function x(){
//     let hi = 'Hello';
//     function y() {
//         console.log(hi);
//     }
//     return y;
// }

// let sayhi = x()();
// console.log(sayhi);


// function x(param) {
//   function y(param1) {
//     return param * param1;
//   }
//   return y;
// }
/*
const x = (x) => {
  return (y) => {
    return x * y
  };
};
*/

// const x = (x) => (y) => x * y;

// const VAT = 1.17
// let sum = x(VAT);
// console.log("sum=>", sum(100));
// console.log("sum=>", sum(200));
// console.log("sum=>", sum(300));



// Compose
// const x = (a,b) => (c) => a(b(c))

// const sum2 = (num) => num * 2;
// const sum = (num) => num + 1;

// let ret = x(sum, sum2)(6);
// console.log("ret=>", ret);



// Pass By Value, Pass By Reference
// let a = 10;
// let b = a;
// b = 8
// console.log('a=>', a, 'b=>', b);

// let arr1 = [1,2,3];
// let arr2 = [...arr1];
// arr2[1] = 5;
// console.log('arr1=>', arr1, 'arr2=>', arr2);

// let obj1 = {a:10};
// let obj2 = {...obj1};
// obj2.a = 15;
// console.log('obj1=>', obj1, 'obj2=>', obj2);

