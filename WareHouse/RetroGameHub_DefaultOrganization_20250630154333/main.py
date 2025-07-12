'''  
Retro Arcade Games Catalog web application  
'''  
from flask import Flask, render_template  
import games_data  
import styles  
app = Flask(__name__)  
@app.route('/')  
def index():  
    return render_template('index.html',   
                          games=games_data.GAMES,  
                          styles=styles.STYLES)  
if __name__ == '__main__':  
    app.run(debug=True)  