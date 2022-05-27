#######################################################
# Name           : Brute Facebook (BF)                #
# File           : login_key.py                       #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import subprocess, time, os, urllib, json

from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel

from data import logo as asy
from platform import platform

M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # MATI

class Log_key:

    def __init__(self, url):
        self.url = url
        self.momok()

    def kontol(self):
        asy.Logo().log();print("");prints(Panel("""       SELAMAT DATANG DI TOOLS BRUTE FB 👋
UNTUK MENDAPATKAN API KEY ANDA BISA KUNJUNGI SITUS WEB INI: [green]https://keylicense.yayanxd.my.id[/]
JIKA TIDAK MENGERTI MENGGUNAKAN TOOLS SILAHKAN TONTON TUTORIAL DENGAN KETIK [green]tutorial[/]""",title="[green]PESAN[/]"))
        key = input("  [*] masukan api key kamu : ")
        if key in[""]:
            print("");prints(Panel("😡[bold red] jangan kosong"));time.sleep(3);Log_key(self.url)
        elif key in ["tutorial", "Tutorial", "TUTORIAL"]:
            print("");prints(Panel("😋[bold cyan] anda akan di alihkan ke youtube"));os.system("xdg-open https://youtu.be/bK8-A400sJQ");Log_key(self.url)
        try:
            reso = urllib.request.urlopen(self.url+key+"&dev="+platform())
            get_arg = json.loads(reso.read())
            if get_arg["status"] == "error":
                print("");prints(Panel(f"ðŸ˜”[bold red]  "+get_arg["msg"].replace("Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya", "Akses login di tolak di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.")));exit()
            else:
                kadaluarsa = get_arg["expired"]
                user = get_arg["nama"]
                open("/data/data/com.termux/._.txt", "w").write(key)
                print("");prints(Panel(f"""Hallo [green]{user}[/] apikey anda masih berlaku sampai tanggal: [bold red]{kadaluarsa}[/]
silahkan gunakan dengan bijak yah tools nya 😊😊😊"""));time.sleep(2)
                exit(f"\n [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
        except URLError:
            print("");prints(Panel("😭[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik."));exit()
        except KeyError:
            print("");prints(Panel("😔[bold red] oppsh key anda telah mencapai batas masa aktif nya, silahkan upgrade ke premium."));time.sleep(3);self.kontol()
    
    def momok(self):
        try:
            open("data/lisen.txt", "r").read()
            self.memek()
        except FileNotFoundError:
            self.kontol()
    
    def memek(self):
        asy.Logo();print("");print("");prints(Panel("""😝[bold red] akses login di tolak dikarenakan anda sebelumnya sudah register[/]
🤔 ketik[bold green] Upgrade[/] jika ingin upgrade ke premuim, ketik [bold red]Tidak[/] untuk exit atau keluar program.""",title="[bold red]LOGIN DI TOLAK[/]"))
        upd = input(f"  [{M}?{N}] ketik : ")
        if upd in[""]:
            print("");prints(Panel("😡[bold red] jangan kosong"));time.sleep(3);self.memek()
        elif upd in["upgrade","Upgrade","UPGRADE"]:
            exit(subprocess.Popen(["am","start","https://wa.me/625603036683?text=assalamuaikum bang beli lisenya"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
        elif upd in["tidak","Tidak","TIDAK"]:
            print("");prints(Panel("🤠[bold red] terima kasih telah menggunakan script Brute semoga hari² anda menyenangkan"));exit()
        else:
            prints(Panel("😡[bold red] tinggal ketik upgrade atau tidak apasusah nya memek"));time.sleep(3);self.memek()