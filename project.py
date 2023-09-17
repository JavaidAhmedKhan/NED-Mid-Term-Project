from flask import Flask, render_template, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        user_input = request.form['user_input']
        target_language = request.form['target_language']

        try:
            translator = Translator(to_lang=target_language)
            translation = translator.translate(user_input)
        except Exception as e:
            translation = f"Translation error: {str(e)}"

        return jsonify({'translation': translation})

    return render_template('index.html', translation=None)

if __name__ == '__main__':
    app.run(debug=True)
