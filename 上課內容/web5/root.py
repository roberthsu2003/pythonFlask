from app import createApp

if __name__ == "__main__":
    app = createApp()
    app.debug = True
    app.run()