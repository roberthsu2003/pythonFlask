from app import create_app
#執行一次models
#from app import models
if __name__ == "__main__":
    app = create_app()
    app.secret_key = 'super secret key'
    app.run(debug=True)