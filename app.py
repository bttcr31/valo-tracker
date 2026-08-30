from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>VALO TRACKER</title>

        <style>
            body {
                margin: 0;
                background: #0b0d10;
                color: white;
                font-family: Arial, sans-serif;
            }

            .container {
                max-width: 900px;
                margin: 80px auto;
                padding: 30px;
                text-align: center;
            }

            h1 {
                font-size: 42px;
                letter-spacing: 3px;
            }

            p {
                color: #aaa;
                font-size: 18px;
            }

            .status {
                display: inline-block;
                margin-top: 25px;
                padding: 15px 25px;
                background: #15181d;
                border: 1px solid #2b3038;
                border-radius: 10px;
                color: #55d98a;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>VALO TRACKER</h1>

            <p>
                VALORANT oyuncularının kendi maç geçmişini
                ve performansını takip edebildiği tracker.
            </p>

            <div class="status">
                ● Uygulama çalışıyor
            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )