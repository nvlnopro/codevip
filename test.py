do = "\033[1;91m"; xanhbien = "\033[1;36m"; vang = "\033[0;33m"; hong = "\033[1;35m"; xanhduong = "\033[1;34m"; xanhla = "\033[1;32m"; xanh="\033[1;32m"; cam="\033[1;33m"; blue="\033[1;34m"; lam="\033[1;34m"; tim="\033[1;34m"; syan="\033[1;36m"; xnhac= "\033[1;96m"; den="\033[1;90m"; luc="\033[1;92m"; xduong="\033[1;94m"; trang="\033[1;97m"
edit = vang+"]"+trang+"["+luc+"•√•"+trang+"]"+vang+"["+trang+" => "+luc
import requests, os, sys, re, random, base64, threading, hmac, struct, hashlib, time
from pystyle import Colors, Colorate
from pystyle import *
from random import randint
from time import sleep
from os import system
from datetime import datetime
from threading import Thread
banner = Colorate.Horizontal(Colors.red_to_white, f"""                █▀▄ █▀█ ▄▀█ █▀▀ █▀█ █▄█
                █▄▀ █▀▄ █▀█ █▄█ █▄█ █▀█
             @Copyright belongs to 𝙑𝙖̆𝙣 𝙇𝙤̛̣𝙞
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
[•√•] => Admin: 𝙉𝙜𝙪𝙮𝙚̂̃𝙣 𝙑𝙖̆𝙣 𝙇𝙤̛̣𝙞
[•√•] => Zalo ad: zalo.me/0338342654
[•√•] => Chúc bạn sử dụng tool vui vẻ (◕︵◕) 
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
""")
def echo(text):
	for i in range(len(text)):
		sys.stdout.write(text[i])
		sys.stdout.flush()
		sleep(0.0001)
	print()
def khang(khang):
   echo(Colorate.Horizontal(Colors.green_to_white, "= "*khang))
def CURL(method, url, head, data, cookie, text):
	if method == "GET":
		run = requests.get(url, headers=head, cookies=cookie)
	elif method == "POST":
		run = requests.post(url, headers=head, data=data, cookies=cookie)
	if text == "text":
		return run.text
	else: 
		return run.json()
def CheckUid(id, die, live):
	Check = CURL("GET", "https://graph.facebook.com/"+id+"/picture?redirect=false", None, None, None, "json")["data"]
	if "height" in Check:
		print(edit+vang+"["+luc+"LIVE"+vang+"]"+trang+" => "+vang+id); open(live, "a+").write('{}\n'.format(id))
	else:
		print(edit+vang+"["+do+"DIE"+vang+"]"+trang+" => "+vang+id); open(die, "a+").write('{}\n'.format(id))
def main():
	system("clear")
	echo(banner)
	while True:
		try:listuid= open(input(edit+"Input File Uid Facebook: "+trang)).readlines(); die = input(edit+"Input Name Save Uid Die: "+trang); live = input(edit+"Input Name Save Uid Live: "+trang); break
		except Exception as e:print('[ERROR]: {}'.format(e))
	for i in listuid:
		if "|" in i:
			id = i.strip("\n").strip("\r").split("|")[0]
		elif ":" in i:
			id = i.strip("\n").strip("\r").split(":")[0]
		else:id = i.strip("\n").strip("\r")
		threading.Thread(target=CheckUid, args=(id, die, live)).start()
















if __name__ == "__main__":
	main()
