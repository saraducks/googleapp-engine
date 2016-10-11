import webapp2
import cgi
import re

welcome_form="""
<form method="post">
<h1>welcome %(Name)s </h1>
</form>
""" 

form_html="""
<form method="post">
Name<input type="text" name="name">%(hell)s</input>
<br>
Password<input type="password" name="password">%(helltwo)s</input>
<br>
retype-password<input type="passowrd" name="retype-password">%(hellthree)s</input>
<br>
email<input type="text" name="email">%(hellfour)s</input> 
<br>
<input type="submit" value="click me!">
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def checkname(getname):
	if USER_RE.match(getname):
		return getname
	else:
		return "Username is not valid.Try again"
def checkpassword(getpassword,getconfirmationpassword):
	if PASS_RE.match(getpassword):
		if getpassword == getconfirmationpassword:
			return getpassword
		else:
			return "The password didn't match.Please try again"
def checkmail(mail):
	if MAIL_RE.match(mail):
		return mail
	else:
		return "Invalid mailid"

class Mainpage(webapp2.RequestHandler):
	def write_form(self,inputfromtheuser="",secondinput="",thirdinput=""):
		self.response.out.write(form_html % {"hell":inputfromtheuser,"helltwo":secondinput,"hellthree":"","hellfour":thirdinput})
	def get(self):
		self.write_form()
	def post(self):
		getname = self.request.get('name')
		getpassword = self.request.get('password')
		getconfirmationpassword = self.request.get('retype-password')
		getmailid = self.request.get('email')
		resname = checkname(getname)
		respass = checkpassword(getpassword,getconfirmationpassword)
		resmail = checkmail(getmailid)
		self.write_form(checkname(getname),checkpassword(getpassword,getconfirmationpassword),checkmail(getmailid))
		if resname == getname and respass == getpassword and resmail == getmailid:
			self.response.out.write(welcome_form % {"Name":resname})

		
app = webapp2.WSGIApplication([('/',Mainpage),],debug= True) 