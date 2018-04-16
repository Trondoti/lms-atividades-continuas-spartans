from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


# def index(request):
    # return HttpResponse('Login')
#    return HttpResponse(calculaMediaFinal(10, 5))


def login(request):
    return render(request, "login.html")


def templateBase(request):
    return render(request, "base.html")


def novoAluno(request):
    return render(request, "Formulario_Novo_Aluno.html")


def cursos(request):
    context = {
        'cursosL1' : [
            {
                "nome": "Analise e desenvolvimento",
                "url": "ads",
                "img": "img/ads.png"
            },
            {
                "nome": "Ciência da computação",
                "url": "cc",
                "img": "img/cc.png"
            },
            {
                "nome": "Sistema de informação",
                "url": "si",
                "img": "img/si.png"
            }
        ],
        'cursosL2': [
            {
                "nome": "Banco de dados",
                "url": "bd",
                "img": "img/bd.png"
            },
            {
                "nome": "Jogos Digitais",
                "url": "jd",
                "img": "img/jd.png"
            },
            {
                "nome": "Redes de computadores",
                "url": "rc",
                "img": "img/rc.png"
            }
        ]
    }
    return render(request, "cursos.html", context)

def detalheCurso(request, id=None):
    contextDetalheCursoADS = {
        "valorDetalheCurso1": "Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados.",
        "valorDetalheCurso2": "O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação.",
        "valor1": "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS",
        "valor2": "SOBRE O CURSO",
        "valor3": "Informações do Curso",
        "valor4": "Duração do Curso",
        "valor5": "04",
        "valor6": "Semestres",
        "valor7": "Tecnologo",
        "valor8": "Duração do Curso:",
        "valor9": "2020h",
        "valor10": "Modalidade:",
        "valor11": "Presencial",
        "valor12": "Unidade:",
        "valor13": "Barra Funda",
        "valor14": "Período Matutino",
        "valor15": "| 08h00 às 11h40 |",
        "valor16": "Período Noturno",
        "valor17": "| 19h00 às 22h40 |",
        "valor18": "Mensalidade Matutina",
        "valor19": "R$ 582,00",
        "valor20": "Mensalidade Noturna",
        "valor21": "R$ 657,00",
        "valor22": "Matriz Curricular",
        "valor23": "1º Semestre",
        "valor24": "Comunicação e Expressão",
        "valor25": "Fundamentos de Banco de Dados",
        "valor26": "Introdução à Internet das Coisas - IoT",
        "valor27": "Linguagem de Programação I",
        "valor28": "Lógica de Programação",
        "valor29": "Matemática Aplicada",
        "valor30": "2º Semestre",
        "valor31": "Linguagem de Programação II",
        "valor32": "Linguagem SQL",
        "valor33": "Tecnologia Web",
        "valor34": "Engenharia de Software",
        "valor35": "Gestão de Projetos",
        "valor36": "Ambiente de Desenvolvimento e Operação",
        "valor37": "3º Semestre",
        "valor38": "Desenvolvimento de Aplicações Distribuídas",
        "valor39": "Estrutura de Dados",
        "valor40": "Análise e Modelagem de Sistemas",
        "valor41": "Modelagem de Processos de Negócio",
        "valor42": "Interface Homem-Computador",
        "valor43": "OPE1 - Oficina Projeto Empresa 1",
        "valor44": "4º Semestre",
        "valor45": "Arquitetura e Projeto de Sistemas",
        "valor46": "Desenvolvimento para Dispositivos Móveis",
        "valor47": "Desenvolvimento para Internet das Coisas",
        "valor48": "Qualidade de Software",
        "valor49": "Projeto Empresa 2",
        "valor50": "Legislação e Ética",
        "valor51": "80 horas",
        "valor52": "40 horas",
        "valor53": "120 horas"
    }
    return render(request, "detalhe_curso.html", contextDetalheCursoADS)

def detalheCursoBD(request):
    contextDetalheCursoBD = {
        "valorDetalheCurso1": "O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas de desenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área.",
        "valorDetalheCurso2": "A graduação mostra a importância da segurança de compartilhamento de dados nas empresas modernas e ensina as melhores técnicas e ferramentas de criação e implementação da mesma.",
        "valor1": "BANCO DE DADOS",
        "valor2": "SOBRE O CURSO",
        "valor3": "Informações do Curso",
        "valor4": "Duração do Curso",
        "valor5": "04",
        "valor6": "Semestres",
        "valor7": "Tecnologo",
        "valor8": "Duração do Curso:",
        "valor9": "2020h",
        "valor10": "Modalidade:",
        "valor11": "Presencial",
        "valor12": "Unidade:",
        "valor13": "Barra Funda",
        "valor14": "Período Matutino",
        "valor15": "| 08h00 às 11h40 |",
        "valor16": "Período Noturno",
        "valor17": "| 19h00 às 22h40 |",
        "valor18": "Mensalidade Matutina",
        "valor19": "R$ 582,00",
        "valor20": "Mensalidade Noturna",
        "valor21": "R$ 657,00",
        "valor22": "Matriz Curricular",
        "valor23": "1º Semestre",
        "valor24": "Comunicação e Expressão",
        "valor25": "Fundamentos de Banco de Dados",
        "valor26": "Introdução à Internet das Coisas - IoT",
        "valor27": "Linguagem de Programação I",
        "valor28": "Lógica de Programação",
        "valor29": "Matemática Aplicada",
        "valor30": "2º Semestre",
        "valor31": "Linguagem SQL",
        "valor32": "Análise Exploratória de Dados",
        "valor33": "Ambiente de Desenvolvimento e Operação",
        "valor34": "Desenvolvimento de Sistemas",
        "valor35": "Engenharia de Software",
        "valor36": "Sociedade e Sustentabilidade",
        "valor37": "3º Semestre",
        "valor38": "Developing Database",
        "valor39": "Estrutura de Dados",
        "valor40": "Business Intelligence",
        "valor41": "Data Analytics",
        "valor42": "Sociedade e Sustentabilidade",
        "valor43": "OPE1 - Oficina Projeto Empresa 1",
        "valor44": "4º Semestre",
        "valor45": "Administração de Banco de Dados",
        "valor46": "Qualidade de Governança de Dados",
        "valor47": "Segurança de Banco de Dados",
        "valor48": "Big Data",
        "valor49": "Computação Cognitiva",
        "valor50": "OPE2 - Oficina Projeto Empresa 2",
        "valor51": "80 horas",
        "valor52": "40 horas",
        "valor53": "120 horas"
    }
    return render(request, "detalhe_curso.html", contextDetalheCursoBD)


def detalheCursoJD(request):
    contextDetalheCursoJD = {
        "valorDetalheCurso1": "A graduação de Jogos Digitais aborda as ferramentas práticas e teóricas para o aluno projetar, implementar e testar jogos. Com a criação de personagens, ambientes, objetos, interfaces e regras, é possível aprender sobre tudo o que é necessário para criar um jogo. Além disso, o profissional também pode aplicar técnicas de programação, áudio e elementos em 2D e 3D.",
        "valorDetalheCurso2": "O aluno ainda estará preparado para desenvolver games em diversos ambientes e áreas - não apenas para o entretenimento. Os setores da indústria e educação têm cada vez mais aderido a mecanismos, como jogos para seus setores, os chamados 'serious games', que abrem um grande leque de opções para a profissão.",
        "valor1": "JOGOS DIGITAIS",
        "valor2": "SOBRE O CURSO",
        "valor3": "Informações do Curso",
        "valor4": "Duração do Curso",
        "valor5": "04",
        "valor6": "Semestres",
        "valor7": "Tecnologo",
        "valor8": "Duração do Curso:",
        "valor9": "2100h",
        "valor10": "Modalidade:",
        "valor11": "Presencial",
        "valor12": "Unidade:",
        "valor13": "Barra Funda",
        "valor14": "Período Matutino",
        "valor15": "| 08h00 às 11h40 |",
        "valor16": "Período Noturno",
        "valor17": "| 19h00 às 22h40 |",
        "valor18": "Mensalidade Matutina",
        "valor19": "R$ 584,00",
        "valor20": "Mensalidade Noturna",
        "valor21": "R$ 657,00",
        "valor22": "Matriz Curricular",
        "valor23": "1º Semestre",
        "valor24": "Desenho e Concept Art para Jogos",
        "valor25": "Design de Jogos I",
        "valor26": "Empreendedorismo",
        "valor27": "Introdução à Programação para Jogos Digitais",
        "valor28": "Introdução aos Jogos Digitais",
        "valor29": "Arte 2D para Jogos Digitais",
        "valor30": "2º Semestre",
        "valor31": "Ambiente de Desenvolvimento de Jogos Digitais",
        "valor32": "Arte 3D para Jogos Digitais",
        "valor33": "Design de Jogos II",
        "valor34": "Programação para Jogos Digitais I",
        "valor35": "Processo de Produção de Jogos Digitais",
        "valor36": "Game Level Design",
        "valor37": "3º Semestre",
        "valor38": "Design de Personagens para Jogos Digitais",
        "valor39": "Jogos Digitais para Web",
        "valor40": "Programação para Jogos Digitais II",
        "valor41": "Roteirização e Storyboard para Jogos Digitais",
        "valor42": "Interfaces para Jogos Digitais",
        "valor43": "OPE1 - Oficina Projeto Empresa 1",
        "valor44": "4º Semestre",
        "valor45": "Animação, Áudio e Vídeo para Jogos Digitais",
        "valor46": "Estudos Complementares em Jogos Digitais",
        "valor47": "Jogos Digitais para Dispositivos Móveis",
        "valor48": "Marketing para Jogos Digitais",
        "valor49": "Qualidade e Testes para Jogos Digitais",
        "valor50": "OPE2 - Oficina Projeto Empresa 2",
        "valor51": "80 horas",
        "valor52": "40 horas",
        "valor53": "120 horas"
    }
    return render(request, "detalhe_curso.html", contextDetalheCursoJD)


def detalheDisciplinaTecweb(request):
    contexto = {
        'nome':'Tecnologia Web',
        'objetivo': 'coco fedido',
        'competencias': 'pablo gay',
        'bibliografia': 'guilherme ama o baby',
        'avaliacao': '>= 100'
        }

    return render(request, "detalhes_disciplina.html",contexto)


def detalheDisciplinaBd(request):
    contexto = {
        'nome':'Banco de Dados',
        'objetivo': 'coco fedido',
        'competencias': 'pablo gay',
        'bibliografia': 'guilherme ama o baby',
        'avaliacao': '>= 100'
        }
    return render(request, "detalhes_disciplina.html",contexto)



def detalheDisciplinaDevops(request):
    contexto = {
        'nome':'Ambiente e Desenvolvimento e Operações',
        'objetivo': 'coco fedido',
        'competencias': 'pablo gay',
        'bibliografia': 'guilherme ama o baby',
        'avaliacao': '>= 100'

    }
    return render(request, "detalhes_disciplina.html",contexto)



def formularioCurso(request):
    return render(request, "formulario_curso.html")


def formularioDisciplina(request):
    return render(request, "formulario_disciplina.html")


def formularioMatricula(request):
    return render(request, "formulario_matricula.html")


def painelAdmin(request):
    return render(request, "painel_admin.html")
