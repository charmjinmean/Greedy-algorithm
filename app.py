from flask import Flask, render_template, request, redirect, url_for
from com.count.exchange_controller import ExchangeController
from com.count.exchange_model import ExchangeModel
from com.knapsack.knapsack_controller import KnapsackController
from com.knapsack.knapsack_model import KnapsackModel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/exchange_dollar')
def exchange_dollar():
    return render_template("exchange_dollar.html")

@app.route('/exchange_won')
def exchange_won():
    return render_template("exchange_won.html")

@app.route('/exchange_yen')
def exchange_yen():
    return render_template("exchange_yen.html")

@app.route('/exchange_yuan')
def exchange_yuan():
    return render_template("exchange_yuan.html")

@app.route('/knapsack_al')
def knapsack_al():
    return render_template("knapsack.html")

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    print("달러 환전 요청")

    if request.method == 'POST':
        amount = int(request.form.get('amount'))
        currency = request.form.get('currency')
        print("currency", currency)
        print("amount", amount)

        controller = ExchangeController(amount=amount, currency=currency)
        resp: ExchangeModel = controller.get_result()

        render_html = '<h1>결과보기</h1><br/>'
        render_html += f"{resp.result}"

        return render_template(resp.page , render_html = render_html)
    
@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack():

    if request.method == 'POST':

        capacity = int(request.form.get('capacity', 0))
        profit1 = int(request.form.get('profit1', 0))
        profit2 = int(request.form.get('profit2', 0))
        profit3 = int(request.form.get('profit3', 0))
        profit4 = int(request.form.get('profit4', 0))
        weight1 = int(request.form.get('weight1', 0))
        weight2 = int(request.form.get('weight2', 0))
        weight3 = int(request.form.get('weight3', 0))
        weight4 = int(request.form.get('weight4', 0))

        controller = KnapsackController( capacity=capacity,
            profit1=profit1, profit2=profit2,
            profit3=profit3, profit4=profit4,
            weight1=weight1, weight2=weight2,
            weight3=weight3, weight4=weight4)
        resp: KnapsackModel = controller.get_result()

        render_html = '<h1>결과보기</h1><br/>'
        render_html += f"{resp.result}"

        return render_template('knapsack.html', render_html = render_html)
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)    

app.config['TEMPLATES_AUTO_RELOAD'] = True
