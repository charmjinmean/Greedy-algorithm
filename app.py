from flask import Flask, render_template, request, redirect, url_for
from com.count.exchange_controller import ExchangeController
from com.count.exchange_model import ExchangeModel

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

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    print("달러 환전 요청")
   
    if request.method == 'POST':
        amount = int(request.form.get('amount'))
        currency = request.form.get('currency')
        print("currency", currency)
        print("amount", amount)

        controller = ExchangeController(amount=amount, currency=currency)
        resp: ExchangeModel = controller.getResult()

        render_html = '<h1>결과보기</h1><br/>'
        render_html += f"{resp.result}"

        return render_template(resp.page , render_html = render_html)
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True