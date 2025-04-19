import google.generativeai as ai
from flask import Flask, request, jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
myKey="AIzaSyBMKUMcSpRhUEaEudGFYm-6E8GzbwGDWgQ"
ai.configure(api_key=myKey)
model=ai.GenerativeModel("gemini-1.5-pro")
@app.route('/chat',methods=['GET'])
def chat():
    # data=request.get_json()
    msg=request.args.get("message")
    if not msg:
       return jsonify({"error":"No message provided"}),400
    # msg=data['msg']
    chat=model.start_chat()
    result=chat.send_message(msg)
    answer=result.text
    return jsonify({"response":answer})
if __name__=="__main__":
    app.run(debug=True)


# while True:
#     msg=input("User: ")
#     if(msg=="exit"):
#      break
#     result=chat.send_message(msg)
#     print("chatBot: "+result.text)
