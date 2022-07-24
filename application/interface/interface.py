
# GUI Window
from gevent.pywsgi import WSGIServer
from interface.window import GUIWindow

# Flask
from flask import Flask, render_template


class Interface(object):

    instance = None

    @staticmethod
    def get_instance():
        if Interface.instance is None:
            Interface.instance = Interface()
        return Interface.instance



    def __init__(self):
        super().__init__()

        self.app = Flask(__name__)

        self.host = "0.0.0.0"
        self.port = 2040

        self.set_routes()

        print("Interface init.")


    def set_routes(self):
        
        @self.app.route("/")
        def home():
            return render_template('index.html')



    def run(self):
        ''' RUN PROGRAM
        :return: None
        '''
    
        try:
            self.window = GUIWindow()
            self.window.start()
    
            http_server = WSGIServer(('', self.port), self.app)
            http_server.serve_forever()
        except Exception as e:
            print(e)
        


