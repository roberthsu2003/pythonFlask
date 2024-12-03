# 動態導覽列
### 1. **使用{% include 'xxxx.j2'%}

**base.j2**

```jinja
<div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <span class="fs-4">職能發展學院</span>
      </a>

      {% include "_navigation.j2"%}
    </header>
  </div>
```


**_navigation.j2**

```jinja
<ul class="nav nav-pills">
{% set function_names={
    "Home":"index",
    "Product":"product",
    "Pricing":"pricing",
    "FAQs":"faq",
    "About":'about'
    } %}
{% for menu_item in ["Home","Product","Pricing","FAQs","About"]%}
    {% if menu_item == "Home" %}
    {% set vars = "/" %}
    {% else %}
    {% set vars = "/"+ menu_item.lower() %}
    {% endif %}
<li class="nav-item"><a href="{{url_for(function_names.get(menu_item))}}" class="{{"nav-link active" if request.path == vars else "nav-link"}}" aria-current="page">{{menu_item}}</a></li>
{% endfor %}
</ul>
```

### 2. **使用macro和import

** _macros.j2 **

```jinja
{% macro display_menu(menu_names) %}
    <ul class="nav nav-pills">
    {% for name,index in menu_names.items() %}
      
      {% if name == "Home" %}
        {% set vars = "/" %}
      {% else %}
        {% set vars = "/"+index %}
      {% endif %}
        <li class="nav-item"><a href="{{url_for(index)}}" class="{{"nav-link active" if request.path == vars else "nav-link"}}" aria-current="page">{{name}}</a></li>
     
    {% endfor %}
     </ul>
{% endmacro %}
```

** bas2.j2 **

```jinja
<div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <span class="fs-4">職能發展學院</span>
      </a>

      {% import "_macros.j2" as macros %}
      {% set menu_names = {
              "Home":"index",
              "Product":"product",
              "Pricing":"pricing",
              "FAQs":"faqs",
              "About":"about"}
      %}
      {{ macros.display_menu(menu_names) }}
    </header>
  </div>
```



