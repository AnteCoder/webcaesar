#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):

        textarea = "<textarea name='message' style='height:100px; width:400px'></textarea><br>"
        rotinp = "<input name='rotate' type='number'/>"
        submit = "<input type='submit'/>"
        form = "<form method='post'>" + textarea + "<br>" + rotinp + "<br>" + submit + "</form>"

        self.response.write(form)

    def post(self):

        message = self.request.get("message")
        rotate = self.request.get("rotate")
        encmsg = caesar.encrypt(message, int(rotate))
        self.response.write("Secret Message: " + encmsg)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
