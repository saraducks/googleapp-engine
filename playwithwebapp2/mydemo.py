import webapp2
import cgi

form_html="""
<form method="post">
<input type="text" name="myinput">%(hell)s</input>
<input type="hidden" name="myinput" value="click me!"></input>
<br>
<input type="submit" value="click me!">
</form>
"""
class Mainpage(webapp2.RequestHandler):
	def write(self,inputfromtheuser=""):
		self.response.out.write(form_html % {"hell":inputfromtheuser})
	def get(self):
		self.write()
	def post(self):
		myinput = self.request.get('myinput')
		self.write(myinput)

	
app = webapp2.WSGIApplication([('/',Mainpage),],debug= True) 