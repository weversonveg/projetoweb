from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


URL_PLANILHA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSr2QvO0Ha58vqNppRE3-KUCOF2yeE4MN-J2EnxZbywKsspZdqgu5z2TnA5xP95t8g2nbd9Wh0yoS0X/pub?output=csv"


@app.route("/")
def inicio():

    dados = pd.read_csv(URL_PLANILHA)

    tabela = dados.to_html(
        index=False,
        classes="tabela"
    )

    return render_template(
        "index.html",
        tabela=tabela
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
