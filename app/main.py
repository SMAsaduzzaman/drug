'''importing Flask and other modules'''
from flask import Flask, request, render_template
from joblib import load



app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('home.html')

# @app.route('/result')
# def result():
#   return render_template('result.html')


# load the model
model = load("models/model_v1.joblib")

@app.route('/',methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/result',methods=["GET", "POST"])
def result():
    return render_template("result.html")

@app.route('/prediction', methods=["GET", "POST"])
def prediction():
    '''
    This will get data from html form and will do prediction.

    Returns
    -------
    html
        html code for render
    '''
    form_items = ['Age' ,'Na_to_K']
    	
    data = []
    pred = None

    if request.method == "POST":
        # getting input with name = fname in HTML form
        for item in form_items:  
            try:
                print(item)
                temp = request.form.get(item)
                temp = temp.strip()
                temp = float(temp)
                data.append(temp)
            except Exception as ex:
                print(ex)
    #getting input of BP and rearranging it for matching the data shape
       
        BP= request.form.get('BP')   
        if BP=='HIGH':
            BP_HIGH=1
            BP_LOW=0
            BP_NORMAL=0
        elif BP=='LOW':
            BP_HIGH=0
            BP_LOW=1
            BP_NORMAL=0
        else:
            BP_HIGH=0
            BP_LOW=1
            BP_NORMAL=0
    
        Cholesterol= request.form.get('Cholesterol')   
        if Cholesterol=='HIGH':
            Cholesterol_HIGH=1
            Cholesterol_NORMAL=0
        else:
            Cholesterol_HIGH=0
            Cholesterol_NORMAL=1
        
        print(BP_HIGH,BP_LOW,BP_NORMAL,Cholesterol_HIGH,Cholesterol_NORMAL)
        items=[BP_HIGH,BP_LOW,BP_NORMAL,Cholesterol_HIGH,Cholesterol_NORMAL]

        for i in items:
            print(i)
            temp=i
            temp = float(temp)
            data.append(temp)

        print(data)

        pred = model.predict([data])
        if pred[0] == 'DrugY':
            pred = "Drug Y "
        elif pred[0] == 'drugA':
            pred = "Drug A"
        elif pred[0] == 'drugB':
            pred= "Drug B"
        elif pred[0]=='drugC':
            pred="drug C"
        elif pred[0]=='drugX':
            pred="drug X"

    return render_template("result.html", result=pred)


if __name__ == '__main__':
    app.run(debug=True)
