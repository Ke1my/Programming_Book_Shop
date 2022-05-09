from bottle import post, request

@post('/home', method='post')
def registration():