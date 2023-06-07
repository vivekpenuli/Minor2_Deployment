from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
model = pickle.load(open('vivek_model_pickle','rb'))
print("model is loaded")


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    
    a= request.args['a1']
    b= request.args['a2']
    c= request.args['a3']
    d= request.args['a4']
    e= request.args['a5']
    f= request.args['a6']
    g= request.args['a7']
    h= request.args['a8']
    i= request.args['a9']
    print(a,b,c,d,e,f,g,h,i)
    score=90
 
    if h=="technical" : 
      score=model.predict([[float(a),float(b),int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,0,0,0,0,1]])
     
   
    elif h=="RandD" :
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),1,0,0,0,0,0,0,0,0]])
    elif h=="accounting" :
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,1,0,0,0,0,0,0,0]])
    elif h=="HR" :
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,1,0,0,0,0,0,0]])
    elif h=="management" :
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,1,0,0,0,0,0]])
    elif h=="marketing":
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,1,0,0,0,0]])
    elif h=="product_mng":
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,0,1,0,0,0]])
    elif h=="sales" :
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,0,0,1,0,0]])
    elif h=="support":
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,0,0,0,1,0]])
    elif h=="IT":
      score=model.predict([[a,b,int(c),d,int(e),int(f),int(g),int(i),0,0,0,0,0,0,0,0,0]])

    



   # prediction=model.predict(pd.DataFrame(columns=['satisfaction_level','last_evaluation','number_project',
    #                                               'average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','Department','salary'],
     #                         data=np.array([a,b,c,d,e,f,g,h,i]).reshape(1, 9)))
 
    return jsonify(prediction=str(score))

if __name__=="__main__":
    app.run(debug=True)

#/?a1=0.10&a2=0.60&a3=6&a4=288&a5=2&a6=0&a7=0&a8=technical&a9=1