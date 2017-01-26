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
import cgi

def replicate(tacontent):

            msglabel = "<label style='font-size:20px'><strong>Type a message to encode: </strong></label>"
            textarea = "<textarea name='message' style='height:100px; width:400px'>" + tacontent + "</textarea><br>"

            rotlabel = "<label>Rotate by: </label>"
            rotinp = "<input name='rotate' type='number'/>"

            submit = "<input type='submit'/>"
            form = "<form method='post'>" + msglabel + "<br>" + textarea + "<br>" + rotlabel + rotinp + "<br>" + submit + "</form>"

            header = "<h2>Web Caesar</h2>"

            return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(replicate(""))

    def post(self):

        message = self.request.get("message")
        rotate = self.request.get("rotate")
        encmsg = caesar.encrypt(message, int(rotate))
        escaped_message = cgi.escape(encmsg)

        self.response.write(replicate(escaped_message))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
