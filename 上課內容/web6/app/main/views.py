from . import main
from flask import render_template
from ..model import db,createDB,City



@main.route("/")
def index():
    createDB()
    cityPageQuery = City.query.paginate(per_page=9, page=1)
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

    return render_template('index.html', citys=cityPageQuery.items, has_next=has_next, has_prev=has_prev,
                           next_num=next_num, prev_num=prev_num, page=page, pages=pages), 200


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

    return render_template('index.html',citys=cityPageQuery.items,has_next=has_next,has_prev=has_prev,next_num = next_num, prev_num=prev_num,page=page,pages=pages),200