from flask import Flask,render_template
app = Flask(__name__,template_folder='template')
@app.route('/',methods=['GET'])
def success():
    d={}
    d['name']='manoj'
    d['age']=28
    return render_template('index.html',name=d)
if __name__ == '__main__':
    app.run(debug=True)

