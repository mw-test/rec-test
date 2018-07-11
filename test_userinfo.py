#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# test_userinfo.py
#
# Development/Testing script for the userinfo class
#
# Assumes newly created database with empty userinfo table

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

# create one record test - gets userid for use later on

userinfo = Userinfo(dblogin)
userid = userinfo.create("fname.sname@website.com", "fname", "sname")
userinfo.close()

print("userinfo.create() returned userid: {}\n".format(repr(userid)))

# retrieve one record by userid test - gets email address for use later on

userinfo = Userinfo(dblogin)
rec = userinfo.retrieve_by_userid(userid)
userinfo.close()

print("userinfo.retrieve_by_userid({}) returned: {}\n".format(userid, repr(rec)))

email = rec['email']

# retrieve one record by email test

userinfo = Userinfo(dblogin)
rec = userinfo.retrieve_by_email(email)
userinfo.close()

print("userinfo.retrieve_by_email({}) returned: {}\n".format(userid, repr(rec)))

# update one record by user id test

userinfo = Userinfo(dblogin)
userinfo.update_by_userid(userid, "fname2.sname2@website2.com", "fname2", "sname2")
userinfo.close()

userinfo = Userinfo(dblogin)
rec = userinfo.retrieve_by_userid(userid)
userinfo.close()

print("userinfo.update_by_userid({}, ...) called - retrieved data is: {}\n".format(userid, repr(rec)))

# delete one record by userid test

userinfo = Userinfo(dblogin)
userinfo.delete_by_userid(userid)
userinfo.close()

print("userinfo.delete_by_userid({}) called\n".format(userid))