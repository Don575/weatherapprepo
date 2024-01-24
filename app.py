from flask import Flask , render_template , request
import requests
app = Flask(__name__)


@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/weatherapp',methods=['POST'])
def inside():
    city = str(request.form['city'])
    units = str(request.form['units'])
    apikey = str(request.form['key'])
    url = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'q' : city
         ,'appid' : apikey
         ,'units' : units}
    data = requests.get(url,params=para)     
    x = str(data.json())
    return x

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)


