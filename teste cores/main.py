from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root():
    #inicia as listas
    cores = []
    cores_unicas = []
    verifica_impar = []
    #abre o arquivo
    f= open("cores.txt","w+")
    URL = 'https://random-data-api.com/api/color/random_color'
    #pega as cores do ramdom_color
    for x in range(50):
        response = requests.get(url = URL)
        cores.append(response.json())
    #separa as cores que não foram repetidas
    for x in cores:
        if x["color_name"] not in cores_unicas:
            cores_unicas.append(x["color_name"])
        else:
            verifica_impar.append(x["color_name"])
            cores_unicas.remove(x["color_name"])
    #salva as cores unicas no arquivo
    for x in cores_unicas:
        if x not in verifica_impar:
            f.write(x + ", ")
    f.close
    #tentativa de chamar um arquivo html ao invés de cria-lo no return
#    return templates.TemplateResponse("index.html", "request")
    
    #retorno do html, não consegui configurar o grafico ou chamar o javascript deste modo
    return """
    <html>
        <head>
            <title>Grafico</title>
            <script scr="fazGrafico.js"></script>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        </head>
        <body>
            <h1></h1>
            <canvas id="lineChart"></canvas>
        </body>
    </html>
    """
