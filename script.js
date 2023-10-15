function tabela(){
    const nome = document.getElementById("nome").value;
    const disc = document.getElementById("disciplina").value
    const tabelaDisc = document.getElementById("tabela-disciplina");
    if (nome == "" || disc ==  ""){
      document.getElementById("erro").innerHTML="Preencha todos os campos";
    }
    
    else{
      document.getElementById("erro").innerHTML="";

      const tr = document.createElement("tr");
      const tdNome = document.createElement("td");
      const tdDisc = document.createElement("td");
      tdNome.innerText = nome;
      tdDisc.innerText = disc;
      tr.appendChild(tdNome);
      tr.appendChild(tdDisc);
      tabelaDisc.appendChild(tr);
    }
    console.log("testeeeeeee")

}