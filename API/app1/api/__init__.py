from flask import Blueprint,request

api = Blueprint('api',__name__,url_prefix='/api/v1')

@api.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(request.get_data().decode('utf-8'))
        print(request.get_json())
        print(f'username:{request.authorization["username"]}')
        print(f'password:{request.authorization["password"]}')
    elif request.method == "POST":
        print(request.get_json())

    return "Hello! API"
