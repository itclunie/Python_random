#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:02:48 2018

@author: itclunie
"""

import smtplib

server = smtplib.SMTP('smtp.gmx.com', 25)

server.starttls()
server.set_debuglevel(1)
server.ehlo
server.login("j_smithy@gmx.com", "andy1999")

sender = "j_smithy@gmx.com"
subject = "test"
messageBody = "this is the message body \n so is this"

msg = "From: " + sender + "\nSubject: " + subject + "\n\n" + messageBody #header info

server.sendmail("j_smithy@gmx.com", "itclunie@gmail.com", msg)

server.quit()


