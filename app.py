from flask import Flask, request,  jsonify,render_template

app = Flask(__name__)

@app.route('/',   methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            result = num1 + num2
            answer = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result)
        if operation == 'subtract':
            result = num1 - num2
            answer = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result)
        if operation == 'Multiply':
            result = num1 * num2
            answer = 'The multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result)
        if operation == 'divide' and num2>0:
                result = num1 / num2
                answer = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(result)
        return render_template('results.html', result=answer)

@app.route('/postman', methods=['POST'])
def mathoperations():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            result = num1+num2
            answer = 'The sum of '+str(num1)+' and '+str(num2)+' is '+str(result)
        if operation == 'subtract':
            result = num1-num2
            answer = 'The difference of '+str(num1)+' and '+str(num2)+' is '+str(result)
        if operation == 'Multiply':
            result = num1*num2
            answer = 'The multiplication of '+str(num1)+' and '+str(num2)+' is '+str(result)
        if operation == 'divide':
            result = num1/num2
            answer = 'The quotient when '+str(num1)+' is divided by '+str(num2)+' is '+str(result)
        return jsonify(answer)

if __name__ == 'main':
    print('running')
    app.run()
