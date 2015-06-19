from bottle import Bottle,run,template
import dbconn
import bottle

app = Bottle()

@app.route('/')
@app.route('/hello/')
@app.route('/hello')
def greet():
    return ('Hello please input name')

@app.route('/hello/<name>')#route decorator binds it to a function just like annotations
def greet(name="Guest"):
    dbconn.establish_conn_to_db()#calling function from one script to another
    return template('Hello {{name}}, how are you?', name=name)

blogs = {'About OS','About Algorithms','About Datastructures'}

@app.route('/hello/<name>/blog')
def template1(name="Guest"):
    greet(name)
    return template('my_blog',username = name,owner= 'Rahul Ramesh',blogs = blogs)

@app.post('/subscribed')
def subscribed():
    email = bottle.request.forms.get('emailid')
    usn = bottle.request.forms.get('usn')
    print('email subscribed '+email)# need to store in mongodb later
    return template('subscribed',username = usn,owner= 'rahul')

run( app,host='localhost', port=8080)#run command starts a builtin server in bottle framework