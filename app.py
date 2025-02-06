from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def get_unit_count(amount, unit_list):

    money = amount
    unit_dict = {}
    for unit in unit_list:
        unit_dict[unit] = money // unit
        money %= unit
        print(f"{unit}원 : {unit_dict[unit]}개")
    print("거스름돈", amount)
    return unit_dict

@app.route('/exchange_won', methods=['GET', 'POST'])
def exchange_won():
    print("원화 환전 요청")
   
    won_list = [50000, 10000, 5000, 1000, 
                500, 100, 50 ,10]
    
    total = None  
    price = None 
    amount = None 
    render_html = ""
 
    if request.method == 'POST':
        
        total = int(request.form.get('total'))
        price = int(request.form.get('price')) 
        amount = total - price

        won_dict = get_unit_count(amount, won_list)

        for won,count in won_dict.items():
            print(f"{won}원: {count}개")

            render_html = '<h1>결과보기</h1><br/>'
            for won,count in won_dict.items():
                 render_html += f"{won}원: {count}개<br/>"
        
    return render_template("exchange_won.html", render_html = render_html)

@app.route('/exchange_dollar', methods=['GET', 'POST'])
def exchange_dollar():
    print("달러 환전 요청")
   
    dollar_list = [100, 50, 20, 10, 5, 2 ,1]
    
    total = None  
    price = None 
    amount = None 
    render_html = ""
 
    if request.method == 'POST':
        
        total = int(request.form.get('total')) 
        price = int(request.form.get('price')) 
        amount = total - price

        dollar_dict = get_unit_count(amount, dollar_list)

        for dollar,count in dollar_dict.items():
            print(f"{dollar}달러: {count}개")

            render_html = '<h1>결과보기</h1><br/>'
            for dollar,count in dollar_dict.items():
                 render_html += f"{dollar}달러: {count}개<br/>"
        
    return render_template("exchange_dollar.html", render_html = render_html)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True