from libs.myRequestHandler import MyRequestHandler

class MainHandler(MyRequestHandler):
    async def get(self):
        self.render('../templates/index.html', index_word='Hello Tornado')