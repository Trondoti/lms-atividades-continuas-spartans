function validateForm() {
    var inputs = document.querySelectorAll('input[type="radio"]');
    var cont_aprovado = 0;
    var cont_cancelado = 0;
    var has_alerted = false;
    console.log(inputs);

    for(var i = 0; i < inputs.length; i++) {
        if(inputs[i].checked == true && inputs[i].className == "aprovado") {
            cont_aprovado++;
            console.log("APROVADO");
        }
        else if(inputs[i].checked == true && inputs[i].className == "cancelado") {
            cont_cancelado++;
            console.log("CANCELADO");
        }
        else if(inputs[i].checked == false && inputs[i].className == "aprovado" && has_alerted == false || inputs[i].checked == false && inputs[i].className == "cancelado" && has_alerted == false) {
            console.log("Você deve preencher pelo menos uma opção em cada linha da lista.");
            has_alerted = true;
        }
    }


    if(cont_aprovado <= 20) {
        alert("Mínimo de 20 alunos aprovados!")
        return false;
    }
    else if(cont_aprovado > 60) {
        alert("Máximo de 60 alunos aprovados!");
        return false;
    }
    else {
        console.log("Já eras");
    }
}
