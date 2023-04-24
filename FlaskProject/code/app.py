import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
   bg_color=os.getenv('BG_COLOR', 'black')
   text_color=os.getenv('TEXT_COLOR', 'yellow')
   return render_template('index.html', name='Ejemplo de Proyecto con Flask', bg_color=bg_color, text_color=text_color)	
   #return render_template('index.html', name='Ejemplo de Proyecto con Flask', bg_color='red', text_color='white') --> asi se haria sin variables de entorno

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

