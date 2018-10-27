import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
#wallpaper
print ('''
\033[91m
@@@  @@@  @@@  @@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@  @@@   @@@@@@   @@@  @@@  
@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@@ @@@  
@@!  @@!@!@@@  @@!       @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@    @@!    @@!  @@!  @@@  @@!@!@@@  
!@!  !@!!@!@!  !@!       !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@    !@!    !@!  !@!  @!@  !@!!@!@!  
!!@  @!@ !!@!  @!!!:!    @!@  !@!  @!@!!@!   @!! !!@ @!@  @!@!@!@!    @!!    !!@  @!@  !@!  @!@ !!@!  
!!!  !@!  !!!  !!!!!:    !@!  !!!  !!@!@!    !@!   ! !@!  !!!@!!!!    !!!    !!!  !@!  !!!  !@!  !!!  
!!:  !!:  !!!  !!:       !!:  !!!  !!: :!!   !!:     !!:  !!:  !!!    !!:    !!:  !!:  !!!  !!:  !!!  
:!:  :!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!    :!:    :!:  :!:  !:!  :!:  !:!  
::   ::   ::   ::       ::::: ::  ::   :::  :::     ::   ::   :::     ::     ::  ::::: ::   ::   ::  
:    ::    :    :         : :  :    :   : :   :      :     :   : :     :     :     : :  :   ::    :                                                               
               \033[92m[127.0.0.1]\033[93m|_|\033[92m[127.217.21.78]
                   \033[92m[\033[93mCodec By Codename\033[92m]
''')
print
print "           \033[91m[\033[94m1\033[91m]\033[93m> \033[92mDNS LookUP               "
print "           \033[91m[\033[94m2\033[91m]\033[93m> \033[92mWhois LookUP             "
print "           \033[91m[\033[94m3\033[91m]\033[93m> \033[92mGeoIP LookUP             "
print "           \033[91m[\033[94m4\033[91m]\033[93m> \033[92mnmap portscanner         "
print "           \033[91m[\033[94m5\033[91m]\033[93m> \033[92mReverseIP                "
print "           \033[91m[\033[94m6\033[91m]\033[93m> \033[92mDomainToIpConverter      "
print "           \033[91m[\033[94m7\033[91m]\033[93m> \033[92mDNS Host Search          "
print 
print "           \033[91m[\033[94m0\033[91m]\033[93m> \033[92mExit "
print
codec = raw_input("root@kalilinux ~# ")

if codec == "1" or codec == "01":
  os.system("clear")
  cn = raw_input('\033[96mPlace Domain Target :\033[96m')
  dns = "http://api.hackertarget.com/dnslookup/?q=" + cn
  look = urlopen(dns).read()
  print (look)
  sys.exit()

elif codec == "2" or codec == "02":
    os.system("clear")
    cn = raw_input('\033[92mPlace IP Address Target :\033[92m')
    whois = "http://api.hackertarget.com/whois/?q=" + cn
    lookup = urlopen(whois).read()
    print (lookup)
    sys.exit()

elif codec == "3" or codec == "03":
    os.system("clear")
    cn = raw_input('\033[96mPlace Domain Target :\033[96m')
    geo = "http://api.hackertarget.com/geoip/?q=" + cn
    ipl = urlopen(geo).read()
    print (ipl)
    sys.exit()

elif codec == "4" or codec == "04":
    os.system("clear")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host)) 
    sys.exit()

elif codec == "5" or codec == "05":
    os.system("clear")
    cn = raw_input('\033[91mPlace IP Address Target :\033[91m')
    host = "http://api.hackertarget.com/reverseiplookup/?q=" + cn
    hasil = urlopen(host).read()
    print (hasil)
    sys.exit()
    
elif codec == "6" or codec == "06":
    os.system("clear")
    cn = raw_input('\033[91mPlace Domain Target :\033[91m')
    get = "http://reverseip.domaintools.com/search/?q=" + cn
    page = urlopen(get).read()
    print(page)
    sys.exit()
    
elif codec == "7" or codec == "07":
    os.system("clear")
    cn = raw_input('\033[91mPlace Domain Target :\033[91m')
    host = "https://api.hackertarget.com/hostsearch/?q=" + cn
    search = urlopen(host).read()
    print(search)
    sys.exit()
    
elif codec == "0" or codec == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()