from flask import Flask

app = Flask(__name__)

# dekoreter
# bölümü
@app.route('/')
def hello():
    return "Hello World from Flask!!!"
#/ second dekore edildi
@app.route('/second')
def second():
    return 'Welcome!!!!'
@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'



if __name__ == '__main__':
    #port secimi yapılabilir ,port=2000 gibi
    app.run(debug=True)