ipp=['5LMBGM6SBYIRINRS','HMKNW17B15021466']
def start(ip):
    for i in range(len(ip)):
    subprocess.Popen(‘/Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js –address “127.0.0.1” -p “’+str(4723+2*i)+’” –command-timeout “100” –automation-name “Appium” -U “’+ip[i]+’:’+str(5555+i)+’” >/tmp/1.txt’,shell=True)
    time.sleep(3.5)
    wzj = webdriver.Remote(‘http://localhost:’+str(4723+2*i)+’/wd/hub’, desired_caps)
    dingwei = DingWei(wzj, name)
    t = threading.Thread(target=dingwei.begin)
    tt.append(t)