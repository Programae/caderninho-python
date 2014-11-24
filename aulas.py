'''  aulas.py

     Ao iniciar a aula execute este arquivo no seu computador e compartilhe
     a URL com os alunos.

     Tiago Maluta <tiago.maluta@gmail.com>
'''
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket
import glob
import os
import codecs


root = "CODIGOS"
lessons = ['Aula1', 'Aula2', 'Aula3', 'Aula4', 'Aula5', 'Aula6', 'Aula7', 'Aula8', 'Aula9','Aula10-14','Aula15','Aula16']
pyfiles = []
pyfiles_len = []

html = ""
preface = '''
            <!DOCTYPE html>
            <html>
               <head>
               <meta charset="utf-8">
               <meta http-equiv="X-UA-Compatible" content="IE=edge">
               <meta name="viewport" content="width=device-width, initial-scale=1">
               <meta name="description" content="Programaê">
               <meta name="author" content="Tiago Maluta">
               <!-- <link rel="icon" href="../../favicon.ico"> -->

              <!-- Bootstrap core CSS -->
              <link href="css/bootstrap.min.css" rel="stylesheet">

              <!-- Custom styles for this template -->
              <link href="css/sticky-footer.css" rel="stylesheet">

               <link rel="stylesheet" href="css/codemirror.css">
               <link rel="stylesheet" href="css/caderninho.css">

               <script src="js/codemirror.js"></script>
               <script src="js/python.js"></script>
               <script src="js/css.js"></script>
               <style type="text/css">
                  /* Custom Styles */
                  ul.nav-tabs{
                      width: 140px;
                      margin-top: 20px;
                      border-radius: 4px;
                      border: 1px solid #ddd;
                      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.067);
                  }
                  ul.nav-tabs li{
                      margin: 0;
                      border-top: 1px solid #ddd;
                  }
                  ul.nav-tabs li:first-child{
                      border-top: none;
                  }
                  ul.nav-tabs li a{
                      margin: 0;
                      padding: 8px 16px;
                      border-radius: 0;
                  }
                  ul.nav-tabs li.active a, ul.nav-tabs li.active a:hover{
                      color: #fff;
                      background: #0088cc;
                      border: 1px solid #0088cc;
                  }
                  ul.nav-tabs li:first-child a{
                      border-radius: 4px 4px 0 0;
                  }
                  ul.nav-tabs li:last-child a{
                      border-radius: 0 0 4px 4px;
                  }
                  ul.nav-tabs.affix{
                      top: 30px; /* Set the top position of pinned element */
                  }

                  .CodeMirror {
                    border: 1px solid #eee;
                  }
                  .CodeMirror-scroll {
                    height: auto;
                    overflow-y: hidden;
                    overflow-x: auto;
                    width: 100%;
                  }
                </style>

               <title>Meu caderninho...</title>

               </head>

            <body>


              <div class="container">
              <div class="page-header">
              <h1 class="font1">Meu caderninho...</h1>
              </div>
              <div>
              <div class="row">
                    <div class="col-xs-3" id="myScrollspy">
                        <ul class="font3 nav nav-tabs nav-stacked" data-spy="affix" data-offset-top="125">
                            <li><a href="dicas.html">Dicas</a></li>
                            <li class="active"><a href="exercicios.html">Exercícios</a></li>
                            <li><a href="anota.html">Anotações</a></li>
                            <li><a href="index.html">Início</a></li>
                            <li><img alt="http://programae.org.br" src='img/programae_laranja_128x128.png' border=0px></img></li>
                        </ul>

                    </div>
                    <div class="col-xs-9">
                        <h2 id="section-1"></h2>
'''

suffix = '''
            </div>
            <div class="footer">
            <div class="container">
              <p class="text-muted">http://www.programae.org.br</p>
            </div>
            </div>

            <script src="js/jquery.min.js"></script>
            <script src="js/bootstrap.min.js"></script>

            </body>
            </html>

        '''


html = preface

for i in lessons:
    os.chdir(root+"/"+i)
    #p = glob.glob(root+"/"+i+"/*py")
    p = glob.glob("*py")
    pyfiles.append(p)
    pyfiles_len.append(len(p))
    os.chdir("../../")

pyfiles_len.reverse()
html += '<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">'

for files in zip(lessons,pyfiles):
    s_m = '<ul class="list-group">'
    files[1].sort()
    for f in files[1]:
        if "resposta" in f:
            pass
        else:
            s_m += '<li class="list-group-item"><a href="{2}/{1}/{0}">{0}</a></li>'.format(f,files[0],root)
    s_i = '''
            <!-- -->
            <div class="panel panel-default">
            <div class="panel-heading" role="tab" id="heading_{0}">
            <h4 class="panel-title">
              <a data-toggle="collapse" data-parent="#accordion" href="#collapse_{0}" aria-expanded="false" aria-controls="collapse_{0}">
                {0}
              </a>
            </h4>
            </div>
            <div id="collapse_{0}" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading_{0}">
            <div class="panel-body">'''.format(files[0])
    s_m += '</ul>'

    s_f = '''
             </div>
             </div>
             </div>
             <!-- -->'''

    html += s_i
    html += s_m
    html += s_f

html += '    </div>'
html += suffix

with codecs.open('exercicios.html','w',encoding='utf8') as f:
    f.write(html)

'''
try:
    ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
except:
    print("*** VERIFIQUE SUA CONEXÃO COM A INTERNET ***")
    ip = socket.gethostbyname(socket.gethostname())

print("Compartilhe o seguinte endereço:")
print("+---------------------------+")
print(" http://" + ip + ":5000")
print("+---------------------------+")

httpd = HTTPServer((ip, 5000), SimpleHTTPRequestHandler)

# abre o navegador
webbrowser.open_new("http://" + ip + ":5000")

try:
    httpd.serve_forever()
except:
    print("OOPS... aconteceu algum erro na inicialização!")
    print("Verifique com a equipe do Programaê!")
    print("http://programae.org.br")
'''
