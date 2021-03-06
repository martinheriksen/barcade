"""
This file is part of Barcade.

Barcade is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Barcade is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Barcade.  If not, see <http://www.gnu.org/licenses/>.
"""
import json, os, mimetypes

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class HttpHandler(BaseHTTPRequestHandler):
    
    def _setHeadersSuccess(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _sendNotFound(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><body><h1>Not found!</h1></body></html>")

    def _sendWrongMediaType(self, expected):
        self.send_response(415)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><body><h1>Wrong Media Type/h1></body></html>")

    def _sendMissingInput(self, missing):
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><body><h1>Missing Input!</h1>Still need: " + missing + "</body></html>")

    def _getPrograms(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        programs = list()

        for subdir, dirs, files in os.walk('../data/programs/'):
            for file in files:
                if file == "readme":
                    continue

                if file == "program.json":
                    programFile = open(os.path.join(subdir, file))
                    programData = json.loads(programFile.read())

                    programID = subdir.split("/")[3]
                    programData['id'] = programID
                    programData['screenshot'] = "http://127.0.0.1:8081/programs/" + programID + "/screenshot.png"

                    programs.append(programData)

        self.wfile.write(json.dumps(programs))

    def _getProgram(self, programID):
        if os.path.isdir("../data/programs/" + programID) == False:
            self._sendNotFound()
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        programFile = open(os.path.join("../data/programs/" + programID + "/program.json"))
        programData = json.loads(programFile.read())

        programData['screenshot'] = "programs/" + programID + "/screenshot.png"

        self.wfile.write(json.dumps(programData))

    def _getScreenshot(self, programID):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()

        f = open('../data/programs/' + programID + "/screenshot.png", 'rb')
        self.wfile.write(f.read())
        f.close()

    def _postProgram(self):
        if self.headers['Content-Type'][:16] != "application/json":
            self._sendWrongMediaType("application/json")
            return

        
        postData = json.loads(self.rfile.read(int(self.headers['Content-Length'])))

        if "title" not in postData:
            self._sendMissingInput("title")
            return

        if "description" not in postData:
            self._sendMissingInput("description")
            return


        if "emulator" not in postData:
            self._sendMissingInput("emulator")
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        programID = postData['title'].lower().replace(" ", "")
        print programID

        os.makedirs('../data/programs/' + programID)

        with open("../data/programs/" + programID + "/program.json", 'w+') as outfile:
            json.dump(postData, outfile)

        postData['id'] = programID
        self.wfile.write(json.dumps(postData))


    def do_GET(self):
        if self.path == "/":
            self._setHeadersSuccess()
            self.wfile.write(open(os.path.join("../portal/index.html")).read())
            return
        
        tokenPath = self.path.split("/")
            
        if tokenPath[1] == "programs" and len(tokenPath) == 2:
            self._getPrograms()
            return
        if tokenPath[1] == "programs" and len(tokenPath) == 3:
            self._getProgram(tokenPath[2])
            return
        if tokenPath[1] == "programs" and tokenPath[3] == "screenshot.png"  and len(tokenPath) == 4:
            self._getScreenshot(tokenPath[2])
            return

        if tokenPath[1] == "portal":
            if os.path.isfile("../" + self.path) == False:
                self._sendNotFound()
            else:
                self.send_response(200)
                mimeType = mimetypes.guess_type("../" + self.path)
                print mimeType[0]
                self.send_header('Content-type', mimeType[0])
                self.end_headers()
                self.wfile.write(open(os.path.join("../" + self.path)).read())

            return

        self._sendNotFound()
        return


    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_HEAD(self):
        self._setHeadersSuccess()
        
    def do_POST(self):
        print self.path
        print self.headers

        tokenPath = self.path.split("/")
        
        if tokenPath[1] == "programs" and len(tokenPath) == 2:
            self._postProgram()
            return

        self._sendNotFound()
        return



def run(server_class=HTTPServer, handler_class=HttpHandler, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
