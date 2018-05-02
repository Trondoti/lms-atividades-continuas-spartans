document.getElementById('login').required = true;
document.getElementById('nome').required = true;
document.getElementById('email').required = true;
document.getElementById('nascimento').required = true;
document.getElementById('cpf').required = true;
document.getElementById('senha').required = true;
document.getElementById('confirma_senha').required = true;

function validarSenha() {
    var senha = document.getElementById("senha").value;
    var aux = document.getElementById("senha");

    if(senha.search(/[a-zA-Z]/) <= 0 && senha.search(/\d/) <= 0) {
        aux.setCustomValidity("A senha deve ter letras e números!");
    }
    else {
        aux.setCustomValidity("");
  }
}


function senhasIguais(confirma_senha) {
    if(confirma_senha.value != document.getElementById("senha").value) {
        confirma_senha.setCustomValidity("As senhas devem ser iguais!");
    }
    else {
        confirma_senha.setCustomValidity("");
    }
}


function validarCPF() {
    if (vercpf(document.frmcpf.cpf.value)) {
        console.log("Sucesso");
    } else {
        errors = "1";
        if (errors) alert('CPF Inválido.');
        document.retorno = (errors == '');
    }
}


function validarIdade() {
    var data_nascimento = document.getElementById("nascimento").value;
    var ano_nascimento = data_nascimento.split("-")[0];
    var mes_nascimento = data_nascimento.split("-")[1];
    var dia_nascimento = data_nascimento.split("-")[2];
    var data_atual = new Date();
    var ano_atual = data_atual.getFullYear();
    var mes_atual = data_atual.getMonth()+1;
    var dia_atual = data_atual.getDate();
    var ano_subtracao = ano_atual - ano_nascimento;
    var mes_subtracao = 0;
    var dia_subtracao = 0;
    var idade = ano_subtracao;

    if(mes_nascimento != mes_atual) {
        if(mes_atual < mes_nascimento) {
            idade--;
        }
    }
    else if(dia_atual < dia_nascimento) {
        idade--;
    }

    (idade <= 17) ? alert("Menores de 17 anos não podem ser cadastrados!") : console.log("Só alegria!");

    console.log(idade)
    //alert(ano_subtracao);
    // alert(dia_atual + "/" + mes_atual + "/" + ano_atual);
    // alert(dia_nascimento + "/" + mes_nascimento + "/" + ano_nascimento);
}


function vercpf(cpf) {
    if (cpf.length != 11 || cpf == "00000000000" || cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" || cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" || cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999")
        return false;
    add = 0;
    for (i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    add = 0;
    for (i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
    return true;
}
