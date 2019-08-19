from flask import Flask, render_template, request
import json
import pandas as pd

app = Flask(__name__)
data=pd.read_csv('monthly_electricity_source_data.csv')


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/button1", methods=['POST'])
def button1():
    print(request.form['status'])
    return_data = data.query('YEAR<=2005 & STATE=="CA"')
    return_data['TYPE OF PRODUCER'] = return_data['TYPE OF PRODUCER'].str.strip()
    return_data = return_data[return_data['TYPE OF PRODUCER']=='Total Electric Power Industry']
    return_data = return_data[return_data['ENERGY SOURCE']=='Coal']
    return json.dumps({'data': return_data.to_json(orient='split',index=False)})

@app.route("/button2", methods=['POST'])
def button2():
    print(request.form['status'])
    return json.dumps({'response':'received button2 click'})


if __name__ == "__main__":
    app.run()