#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# databaseapi.py
#
# Creates an http server to implement a web api for the userinfo class
#

# test data for postman
#
# create - POST
# http://localhost:8000/userinfo
# { "email": "email1@test.com", "forename": "fn1", "surname": "sn1" }
#
# retrieve - GET
# http://localhost:8000/userinfo/X
#
# update - PUT
# http://localhost:8000/userinfo/X
# { "email": "email2@test.com", "forename": "fn2", "surname": "sn2" }
#
# delete - DELETE
# http://localhost:8000/userinfo/X
# { "email": "email2@test.com", "forename": "fn2", "surname": "sn2" }


import http.server
import urllib.parse
import json

from userinfo import Userinfo

# dictonary to hold MySQL database login details

dblogin = {
  'user':     'holextusr',
  'password': 'somepassword',
  'host':     'localhost',
  'port':     3306,
  'database': 'holextdb',
  'raise_on_warnings': True,
  'autocommit': True
}

class Userinfo_api(http.server.BaseHTTPRequestHandler):
    """Handles rest style http requests for userinfo data"""

    def do_POST(self):
        """create requests"""
        data = self.read_request_body()

        userinfo = Userinfo(dblogin)
        userid = userinfo.create(data['email'], data['forename'], data['surname'])
        userinfo.close()

        self.send_response(200)
        self.end_headers()
        self.write_response_body({'userid': userid})
        
    def do_GET(self):
        """retrieve requests"""
        userid = self.get_userid_from_path()

        userinfo = Userinfo(dblogin)
        rec = userinfo.retrieve_by_userid(userid)
        userinfo.close()

        self.send_response(200)
        self.end_headers()
        self.write_response_body(rec)
        
    def do_PUT(self):
        """update requests"""
        userid = self.get_userid_from_path()
        data = self.read_request_body()
        
        userinfo = Userinfo(dblogin)
        userinfo.update_by_userid(userid, data['email'], data['forename'], data['surname'])
        userinfo.close()
                
        self.send_response(200)
        self.end_headers()
        
    def do_DELETE(self):
        """delete requests"""
        userid = self.get_userid_from_path()

        userinfo = Userinfo(dblogin)
        userinfo.delete_by_userid(userid)
        userinfo.close()

        self.send_response(200)
        self.end_headers()        
        
    def get_userid_from_path(self):
        """get the user id from the url path"""
        return self.path.rpartition('/')[2]

    def read_request_body(self):
        """returns request body in json format as a dictionary"""
        requestbody = self.rfile.read1(1000)
        return json.loads(requestbody.decode())
        
    def write_response_body(self, d):
        """writes request body as json format from a dictionary"""        
        responsebody = json.dumps(d).encode()
        self.wfile.write(responsebody)

# start api server on local machine using port 8000

http.server.HTTPServer(('', 8000), Userinfo_api).serve_forever()