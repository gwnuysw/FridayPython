from flask import Flask, escape, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    name = request.args.get("name","World")
    payload = json.loads(request.data)
    amount = json.loads(payload["action"]["params"]["sys_number"])
    print(amount["amount"])
    amount = amount["amount"]
    
    
    
    if(amount == 60|| amount =='육십'): 
    
        sayhi = {
        "version": "2.0",
        "template":{
        "outputs":[
        {
        "simpleText":{
        "text":"축하합니다 맞췄어용!"
        }
        } 
        ]
        }
        }
        return sayhi

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
