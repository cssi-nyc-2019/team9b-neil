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

# other functions should go above the handlers or in a separate file
x = 0
q1 = "What is the largest continent? \nA: North America B: Asia C: Africa"
q2 = "What is the tallest mammal? \nA: Giraffe B: Elephant C: Moose"
q3 = "What is the capital of Italy? \nA: Yerevan B: Luanda C: Rome"
q4 = "How many sides does a hexagon have? \nA: 5 B: 6 C: 7"
q5 = "What is the full name of Michael Jackson? \nA: Michael Jackson B: Michael Joseph Jackson C: Michael Jerald Jackson"
q6 = "Who is the creator of Facebook? \nA: Mark Zuckerberg B: Elon Musk C: Bill Gates"
q7 = "When was Google founded? \nA: 1998 B: 1995 C: 1997"
q8 = "Which ocean is the deepest? \nA: Atlantic Ocean B: Pacific Ocean C: Indian Ocean"
q9 = "What does LEM stand for in math? \nA: Lunar Excursion Module B: Least Common Multiple C: Low End Mac"
q10 = "Where was Obama born? \nA: New York B: Ohio C: Hawaii"
q11 = "Which planet is closest to the sun? \nA: Venus B: Mercury C: Saturn"
q12 = "Whose picture is on a dime? \nA: George Washington B: Thomas Jefferson C: Franklin D. Roosevelt"
q13 = "Who is the richest person in the world? \nA: Warren Buffet B: Larry Page C: Jeff Bezos"
q14 = "How do you say 'goodbye' in Japanese? \nA: Sayonara B: Arrivederci C: Annyeong"
q15 = "How many strings does a cello have? \nA: 4 B: 5 C: 6"
q16 = "What is the currency in Japan? \nA: Yuan B: Yen C: Kyat"
q17 = "What is Talia's favorite game? \nA: Cookie Clicker B: Cookie Clicker (with autoclicker) C: Cookie Clicker (with extreme autoclicker)"
q18 = "What is Julia's favorite school subject? \nA: Math B: Computer Science C: Science"
q19 = "What is Neil's last name? \nA: Yang B: Baidan C: Jansen"
q20 = "How tall is Reiaz? \nA: 6 feet B: 5 feet 11 inches C: 5 feet 9 inches"

# the handler section
class MainHandler(webapp2.RequestHandler):
    def get(self):
        homeTemplate = the_jinja_env.get_template('templates/index.html')
        self.response.write(homeTemplate.render())
    def post(self):
  	    gameTemplate = the_jinja_env.get_template('templates/game.html')
  	    self.response.write(gameTemplate.render())

app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler)
  ], debug=True)
