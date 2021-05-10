from . import main
from flask import render_template,redirect,session
from ..model import db,createDB,City



@main.route("/")
def index():
    createDB()
    return redirect('/1')


@main.route("/<int:pageNum>")
def page(pageNum):

    cityPageQuery = City.query.paginate(per_page=9,page=pageNum)


    page = cityPageQuery.page
    pages = cityPageQuery.pages
    has_next = cityPageQuery.has_next
    next_num = None
    if has_next:
        next_num = cityPageQuery.next_num

    has_prev = cityPageQuery.has_prev
    prev_num = None
    if has_prev:
        prev_num = cityPageQuery.prev_num


    #session
    username = session.get('username')
    know = session.get('know')

    return render_template('index.html',citys=cityPageQuery.items,has_next=has_next,has_prev=has_prev,next_num = next_num, prev_num=prev_num,page=page,pages=pages,know=know,username=username),200

@main.route('/cities/<int:cityNum>')
def cities(cityNum):
    city = City.query.get(cityNum)
    print(city)
    return render_template('cities/city.html',city=city),200