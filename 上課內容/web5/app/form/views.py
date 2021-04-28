from . import form

@form.route("/")
def form():
    return "<h1>Hello!Form</h1>"