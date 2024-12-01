## Pagination的方式

```py
@app.route("/product")
def product():
    ITEMS = list(range(1,101))
    page = request.args.get('page',1, type=int)
    per_page = 10
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(ITEMS) + per_page - 1 ) // per_page
    
    items_on_page = ITEMS[start:end]
    return render_template('product.j2',
                           items_on_page=items_on_page,
                           total_pages=total_pages,
                           page = page
                           )
```

## jinja頁面

```html
<ul>
    {% for item in items_on_page %}
    <li>{{item}}</li>
    {% endfor %}

    {% if page > 1%}
    <a href="{{ url_for('product',page=page-1) }}">上一頁</a>
    {% endif %}

    <span>Page {{page}} of {{total_pages}} </span>

    {% if page < total_pages %}
    <a href="{{ url_for('product', page=page+1) }}">下一頁</a>
    {% endif %}
</ul>
```