import webapp2import cgiimport stringimport codecsform = """  <head>    <title>Use codec</title>  </head>  <body>    <h2>Enter text here:</h2>    <form method="post">      <textarea name="text">%(hello)s</textarea>      <br>      <br>      <input type="submit">    </form>"""def escape_html(s):    return cgi.escape(s, quote = True)def rot13(s):    return codecs.encode(s,'rot_13')class rot13MainPage(webapp2.RequestHandler):    def write(self, hello=""):        self.response.out.write(form %{"hello":escape_html(hello)})    def get(self):        self.write()    def post(self):        inputtext = self.request.get('text')        self.write(rot13(inputtext))app = webapp2.WSGIApplication([('/',rot13MainPage),],debug=True)