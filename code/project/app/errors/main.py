from . import errors

@errors.app_errorhandler(404)
def page_not_found(e):
    return "<h1>沒有發現網頁</h>", 404


