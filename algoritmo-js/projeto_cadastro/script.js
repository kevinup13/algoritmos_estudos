let btn = document.querySelector(".btn");

btn.addEventListener("click", ()=>{
    let peso = document.querySelector("#peso").value;
    let altura = document.querySelector("#altura").value;
    let infor = document.querySelector(".infor p");

    
    if (!peso || !altura){
        alert("Insira um numero válido!");
    }
    else {
        let imc = peso / (altura ** 2);
        infor.innerHTML = `<p>O seu IMC é: ${imc}</p>`;
    }
   
}) 

