from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_unit_count(amount, won_list): #중첩 함수, #파라미터터

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
    error_msg = None 
    mok = None
    nmg = None 
    money = None
 
    if request.method == 'POST':
        
        total = request.form.get('total') 
        price = request.form.get('price') 

        total = int(total)
        price = int(price)

        if price > total :
            error_msg = "음수는 허용되지 않습니다."
        else :
            amount = total - price
            for won in won_list :
                print(won)

            get_unit_count(amount, won_list)

    return render_template("index.html", won_list=won_list, money=money,
                           total=total, price = price, amount=amount, error_msg=error_msg)   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True