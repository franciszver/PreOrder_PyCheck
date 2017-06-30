import sys

import os

import re

import requests

import time

import smtplib

import urllib.request



from lxml import html

from random import randint



from smtplib import SMTP_SSL as SMTP

from email.mime.text import MIMEText



#If present call function to text, "present in this site, site link"

def textMe(arg1, url):

	print (arg1)

	

	me = "startingemail@aim.com"

	you = "7078675309@txt.att.net"

	wife = "7078675309@txt.att.net"

	text_subtype = 'plain'

	message = ""

	#if arg1 is Amazon

	if arg1 is "Amazon":

		message = "BUY NOW- " + url

	

	if arg1 is "Walmart":

		message = "BUY NOW- " + url

	msg = MIMEText(message, text_subtype)

	msg['Subject'] = "AVAILABLE"

	msg['From'] = me

	msg['To'] = you

	

	try:

		try:

			conn = smtplib.SMTP_SSL("smtp.aol.com",465)

			conn.login('username', 'password')

			conn.sendmail(me, you, msg.as_string())

			print ("Successfully sent email to hubby")

			conn.sendmail(me, wife, msg.as_string())

			print ("Successfully sent email to wife")

		finally:

			conn.quit()

	except Exception:

		print ("Error: unable to send email")




count = 0
while (count < 15):
	print ("----STARTING RUN---")
	#Set timed delay for random bot check
	delay = randint(5,50)
	print ("Timed Delay For Amazon: " + str(delay))
	time.sleep(delay)

	#Check Amazon to see if it's still empty
	url = "http://www.amazon.com/Super-NES-Classic/dp/B0721GGGS9/"
	#url = "https://www.amazon.com/AmazonBasics-Mini-DisplayPort-Thunderbolt-Adapter/dp/B00NH13K8S"
	print (url)
	html = requests.get(url)
	text = html.text

	if "when or if this item will be back in stock" in text:
		print ("Definitely Not Available in Amazon - " + str(count))
	else:
		print ("Checking through other method")
		time.sleep(5)
		data = urllib.request.urlopen(url)
		time.sleep(5)
		datatext = str(data.read())
		if "Currently unavailable." in datatext:
			print ("Still UNAVAILABLE")
		else:
			print ("MAY BE AVAILABLE AMAZON GET IT NOW")
			if "Turn on 1-Click ordering" in text:
				print ("YES AVAILABLE")
				textMe("Amazon", url)
			else:
				print ("Nope not yet!")

		

	#Set timed delay for random bot check
	delay = randint(15,60)
	print ("Timed Delay For Walmart: " + str(delay))
	time.sleep(delay)	
	#Check Walmart to see if it's still empty
	url = "http://www.walmart.com/ip/PO-HDW-PLACEHOLDER-652-WM50-Universal/55791858"
	#url = "https://www.walmart.com/ip/Deal-or-No-Deal-Special-Edition-DS-Nintendo-DS/14562180"
	print (url)
	html = requests.get(url)
	text = html.text

	if "Out of stock" in text:
		print ("No Walmart")
	else:
		print ("Checking through other method")
		time.sleep(5)
		data = urllib.request.urlopen(url)
		time.sleep(5)
		datatext = str(data.read())
		if "Add to Cart" in text:
			print ("AVAILABLE WALMART GET IT NOW")
			textMe("Walmart", url)
		else:
			print ("Not Available in Walmart")
		
	
	print ('The count is: ' + str(count))
	count = count + 1

	
#Email Status After While loop
me = "email@aim.com"
you = "email@gmail.com"
message = "Status Checkin for SNES executed: " + str(count)

msg = MIMEText(message, 'plain')

msg['Subject'] = "SNES STATUS"

msg['From'] = me

msg['To'] = you

try:

	try:

		conn = smtplib.SMTP_SSL("smtp.aol.com",465)
		conn.login('username', 'password')
		conn.sendmail(me, you, msg.as_string())

		print ("Successfully sent email to hubby")

	finally:

		conn.quit()

except Exception:

	print ("Error: unable to send email")

