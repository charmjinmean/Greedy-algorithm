from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("전송된 데이터 방식")
   
    won_50000=50000
    won_10000=10000
    won_5000=5000
    won_1000=1000
    won_500=500
    won_100=100
    won_50=50
    won_5=5

    won_list = [50000, 10000, 5000, 1000, 
                500, 100, 50 ,10]
    
    total = None  
    price = None 
    amount = None 
    error_msg = None 
    mok = None
    nmg = None

    if request.method == 'POST':
        
        total = request.form.get('total') 
        price = request.form.get('price') 

        total = int(total)
        price = int(price)

        if price > total :
           
            error_msg = "음수는 허용되지 않습니다."
        else :

            for won in won_list :
                print(won)

            amount = total - price 
 
            for won in won_list:
                mok = amount // won
                nmg = amount % won
                print(f"{won}원 : {mok}개")

            print("거스름돈", amount)

    return render_template("index.html", won_list=won_list, mok = mok, nmg = nmg, 
                           total=total, price = price, amount=amount, error_msg=error_msg)   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True