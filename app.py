from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pour Louanne ❤️</title>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      padding: 40px 20px;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #ff8eb4, #9d4edd);
      color: white;
      font-family: Arial, sans-serif;
    }

    .message {
      max-width: 950px;
      text-align: center;
      font-size: clamp(1.2rem, 2.5vw, 2rem);
      line-height: 1.8;
      background: rgba(255, 255, 255, 0.16);
      padding: 45px;
      border-radius: 28px;
      box-shadow: 0 15px 45px rgba(0, 0, 0, 0.2);
      backdrop-filter: blur(8px);
    }

    h1 {
      margin-top: 0;
      font-size: clamp(2rem, 5vw, 4rem);
    }

    .signature {
      display: block;
      margin-top: 30px;
      font-size: 1.4em;
      font-weight: bold;
    }
  </style>
</head>

<body>
  <main class="message">
    <h1>Pour Louanne ❤️</h1>

    <p>
      Louanne, vraiment mille merci d'être là à mes côtés chaque jour.
      Je ne suis ni beau ni attirant, mais j'ai trouvé une fille que j'aime
      et qui m'aime. Une fille avec qui j'ai envie de construire un avenir,
      une famille.
    </p>

    <p>
      J'ai vraiment envie de faire les choses bien avec toi, chaton.
      Alors ne me lâche pas, s'il te plaît. Tu es la personne qui me redonne
      goût à la vie. Tu n'es pas qu'une simple copine : tu es une véritable
      lumière.
    </p>

    <p>
      Tu illumines mes journées chaque fois que je te parle ou chaque fois
      que je reçois une photo de toi. Alors s'il te plaît, ne pars pas.
      Tu es vraiment une personne incroyable.
    </p>

    <span class="signature">Je t'aime, Louanne. ❤️</span>
  </main>
</body>
</html>
"""

@app.route("/")
def accueil():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)