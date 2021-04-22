from app import creatApp

if __name__ == "__main__":
    app = creatApp()
    app.debug = True
    #print(app.url_map)
    app.run()