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

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
	def get(self):
		homeTemplate = the_jinja_env.get_template('templates/index.html')
		self.response.write(homeTemplate.render())


	def post(self):
		global number
		gameTemplate = the_jinja_env.get_template('templates/game.html')
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
		# question = triviaDict1
		# x = 0
		# for x in len(triviaList)-1:

		# self.response.write(gameTemplate.render(randomQ))
		player_ans = self.request.get('ans')
		# if number == 0:
		# 	if player_ans == "ans1":
		# 		print(number)
		# 	else:
		# 		print("incorrect")
		self.response.write(gameTemplate.render(triviaList[number]))
		number += 1
		if number == 10:
			number = 0


class GameHandler(webapp2.RequestHandler):
	def get(self):
		triviaTemplate = the_jinja_env.get_template('templates/game.html')
		# self.response.write(triviaTemplate.render(randomQ))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/game', GameHandler),
  ], debug=True)
