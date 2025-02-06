from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_unit_count(amount, won_list):

    money = amount
    won_dict = {}
    for won in won_list:
        won_dict[won] = money // won
        money %= won
        print(f"{won}원 : {won_dict[won]}개")
    print("거스름돈", amount)
    return won_dict

@app.route('/', methods=['GET', 'POST'])
def index():
    print("전송된 데이터 방식")
   
    won_list = [50000, 10000, 5000, 1000, 
                500, 100, 50 ,10]
    
    total = None  
    price = None 
    amount = None 
    render_html = ""
 
    if request.method == 'POST':
        
        total = request.form.get('total') 
        price = request.form.get('price') 

        total = int(total)
        price = int(price)
        amount = total - price

        won_dict = get_unit_count(amount, won_list)

        for won,count in won_dict.items():
            print(f"{won}원: {count}개")

            render_html = '<h>결과보기</h1><br/>'
            for won,count in won_dict.items():
                 render_html += f"{won}원: {count}개<br/>"
        
    return render_template("index.html", render_html = render_html)   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True