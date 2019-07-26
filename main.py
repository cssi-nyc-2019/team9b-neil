# the import section
import webapp2
import jinja2
import os
import random

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

number = 0
correct = 0

# other functions should go above the handlers or in a separate file

def scoreDeterminer(player_ans, answer1, answer2, answer3):
	global correct
	global number
	print(player_ans)

	if number == 0:
		if player_ans == answer1:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 1:
		if player_ans == answer2:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 2:
		if player_ans == answer3:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 3:
		if player_ans == answer2:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 4:
		if player_ans == answer1:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 5:
		if player_ans == answer2:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 6:
		if player_ans == answer3:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 7:
		if player_ans == answer2:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 8:
		if player_ans == answer1:
			correct += 1
			print("hello")
		else:
			print("incorrect")
	if number == 9:
		if player_ans == answer3:
			correct += 1
			print("hello")
		else:
			print("incorrect")

# the handler section
class MainHandler(webapp2.RequestHandler):
	def get(self):
		homeTemplate = the_jinja_env.get_template('templates/index.html')
		self.response.write(homeTemplate.render())


	def post(self):
		global number
		global correct
		gameTemplate = the_jinja_env.get_template('templates/game.html')
		endTemplate = the_jinja_env.get_template("templates/game_end.html")
		triviaDict1 = { "question": "What is the largest continent?", "img": "", "ans1": "Asia", "ans2": "North America", "ans3": "Africa" }
		triviaDict2 = { "question": "What is the tallest mammal?", "img": "", "ans1": "Elephant", "ans2": "Giraffe", "ans3": "Gorilla" }
		triviaDict3 = { "question": "What is the capital of Italy?", "img": "", "ans1": "Florence", "ans2": "Venice", "ans3": "Rome"}
		triviaDict4 = { "question": "How many sides does a hexagon have?", "img": "", "ans1": "10", "ans2": "6", "ans3": "7" }
		triviaDict5 = { "question": "When was Google founded?", "img": "", "ans1": "1997", "ans2": "1989", "ans3": "1995" }
		triviaDict6 = { "question": "Where was Obama born?", "img": "", "ans1": "Wisconsin", "ans2": "Hawaii", "ans3": "Florida" }
		triviaDict7 = { "question": "Which planet is closest to the sun?", "img": "", "ans1": "Venus", "ans2": "Mars", "ans3": "Mercury" }
		triviaDict8 = { "question": "Whose picture is on a dime?", "img": "", "ans1": "Thomas Jefferson", "ans2": "Franklin D. Roosevelt", "ans3": "James Madison" }
		triviaDict9 = { "question": "How do you say goodbye in Japanese?", "img": "", "ans1": "Sayonara", "ans2": "Joigin", "ans3": "Annyeong" }
		triviaDict10 = { "question": "How many strings does a cello have?", "img": "", "ans1": "5", "ans2": "6", "ans3": "4" }
		triviaList = [triviaDict1, triviaDict2, triviaDict3, triviaDict4, triviaDict5, triviaDict6, triviaDict7, triviaDict8, triviaDict9, triviaDict10]
		
		player_ans = self.request.get("ans")
		answer1 = self.request.get("ans1")
		answer2 = self.request.get("ans2")
		answer3 = self.request.get("ans3")

		if number < 10:
			scoreDeterminer(player_ans, answer1, answer2, answer3)
			self.response.write(gameTemplate.render(triviaList[number]))
		else:
			number = 0
			end_score = { "score": correct }
			self.response.write(endTemplate.render(end_score))
		# if number == 10:
		# 	number = 0
		number += 1
		

class GameHandler(webapp2.RequestHandler):
	def get(self):
		triviaTemplate = the_jinja_env.get_template('templates/game.html')
		# self.response.write(triviaTemplate.render(randomQ))

def getCurrentUser(self):
	#will return None if user does not exist
	return self.session.get('user')

def login(self, id):
	self.session['user'] = id

def logout(self):
	self.session['user'] = None

def isLoggedIn(self):
	if self.session['user'] is not None:
		return True
	else:
		return False

# the handler section
class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

class SignupHandler(BaseHandler):
	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('templates/sign.html')
		self.response.write(welcome_template.render())

class AccountHandler(BaseHandler):
	def get(self):  # for a get request
		acct_template = the_jinja_env.get_template('templates/account.html')
		user = getCurrentUser(self)
		if user is not None:
			user_info = User.query().filter(User.username == getCurrentUser(self)).fetch()
			variable_dict = {"username": user_info[0].username, "email": user_info[0].email}
			self.response.write(acct_template.render(variable_dict))
		else:
			#send user back to home/login if they're not signed in
			self.redirect('/')

class LogoutHandler(BaseHandler):
	def get(self):  # for a get request
		logout_template = the_jinja_env.get_template('templates/logout.html')
		user = getCurrentUser(self)
		if user is not None:
			logout(self)
			self.response.write(logout_template.render())
		else:
			self.redirect('/')

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/game', GameHandler),
  ('/signup', SignupHandler),
  ('/account', AccountHandler),
  ('/logout', LogoutHandler),
  ], debug=True)
