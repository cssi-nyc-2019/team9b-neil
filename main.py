# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
    	# self.response.write('Greetings')  # the response
        homeTemplate = the_jinja_env.get_template('templates/index.html')
        self.response.write(homeTemplate.render())
    def post(self):
  	    self.response.write("Button Works")
  def get(self):  # for a get request
    self.response.write('Greetings')  # the response

<<<<<<< HEAD
class GameHandler(webapp2.RequestHandler):
    def get(self):
		gameTemplate = the_jinja_env.get_template('templates/game.html')
		self.response.write(gameTemplate.render())
=======
<<<<<<< HEAD
# the app configuration section	
=======
>>>>>>> 362535b6d9542de60d09881f3f6b7563433e1068

# the app configuration section
>>>>>>> a5cd64e3cfaf2d752972ad592c864c6102324c66
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
<<<<<<< HEAD
  ("/game", GameHandler)
  ], debug=True)
=======
  ], debug=True)
>>>>>>> 362535b6d9542de60d09881f3f6b7563433e1068
