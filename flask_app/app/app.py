from flask import Flask
 
app = Flask(__name__)

 
@app.route('/')
def home():
    app.logger.info("Hello there")
    return 'hello, world'
 