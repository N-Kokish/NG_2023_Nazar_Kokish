from flask import Flask,render_template,request

servak = Flask("Lection_4_1")

@servak.route("/ask")
def ask():
    return render_template("ask.html")

@servak.route("/sum")
def sum():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    znak = str(request.args.get("znak"))
    match znak :
        case str("+"):
            return(str(firstValue+secondValue))
        case str("-"):
            return(str(firstValue-secondValue))
        case str("*"):
            return(str(firstValue*secondValue))
        case str("/"):
            return(str(firstValue/secondValue))
        case str("^"):
            return(str(firstValue**secondValue))    
        case str("!^"):
            return(str(firstValue**(1/secondValue)))  

servak.run(host="0.0.0.0", port=8080)

