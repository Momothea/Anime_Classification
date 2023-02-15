from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #debug true since we are in development. Put 'off' in production