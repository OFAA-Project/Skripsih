from flask import Flask, render_template 
import docker
# declaring app name 
app = Flask(__name__) 
  
# making list of pokemons 
#Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
#           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"] 
# defining home page 
@app.route('/') 
def homepage(): 
    client = docker.from_env() 
    container = client.containers.list()
    images = client.images.list()
# returning index.html and list 
# and length of list to html page 
    return render_template("index.html", len = len(container), container = container, len1 = len(images), images = images) 


  
    # if __name__ == '__main__': 
  
    # running app 
app.run(use_reloader = True, debug = True) 