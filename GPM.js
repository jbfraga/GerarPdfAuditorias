

let cabecalhoRemover = ["Origem do Sistema:", "Origem do Serviço:", "Departamento:", "Usuário:", "Usuário de cadastro:", "Prioridade:", "Justificativa de Leitura:", "Últ. atualização:", "Medidor anterior:", "Qtd. Horas APR:","Laudo:", "Proc. SESMT:"];

let linhasAlvo = document.querySelector("table.tbl_head").querySelectorAll("tr");

linhasAlvo.forEach((el)=>{
    cabecalhoRemover.forEach((remover)=>{
        if (el.innerText.includes(remover)){
            el.remove();
        }
    })       
})
/*
let abrirImagens = document.querySelector("#btn_mostra_fotos").click();

await new Promise(r => setTimeout(r, 5000));

let aumentarImagens = document.querySelector("#div_fotos").querySelectorAll("img");
aumentarImagens.forEach((el)=>{
    el.style.width = "300px"
});

let cabecalhoRemover2 = document.querySelector("body > div:nth-child(11)").remove();

let tabelaRemover = document.querySelector("body > table:nth-child(38)").remove();
document.querySelector("body > div:nth-child(40) > div.div_head").remove();
document.querySelector("body > div:nth-child(40) > div:nth-child(15)").remove();
window.print();*/