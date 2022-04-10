from search_engines import Google
from ast import literal_eval
import time
# import arg
def mysearch(csvaddr='0x5b27531228d8c65a0d2adcd8903fd3348f768a11'):
    with open('addr.txt','r') as f:
        addrlist = literal_eval(f.read())
    # addrlist = ['0x516980e3321482b51b0e10af2770d6fbd47f6f9f']
    # addr = '0x44a7ff01f7d38c73530c279e19d31527bdcf8c78'
    # addr = '0x67dc51fca0626bcb18eaf82a0e8aa355019b8723'
    # addr = '0xaa1ea8f6cdeeb491d9cf9fcdfc8fec6b4040d1c4'
    # csvaddr = '0xc31fb4c352cb68c847715d46d97c1fa2aa2d0f00'
    # csvaddr = '0xa1b04a60a35854d0749ae39b0346bceb55247ecc'
    # csvaddr = '0x5b27531228d8c65a0d2adcd8903fd3348f768a11'
    count = 0
    myindex = addrlist.index(csvaddr)
    addrlist = addrlist[myindex:]
    engine = Google()
    for addr in addrlist:
        try:
            engine.set_search_operator('host')#设置为url将过滤
            results = engine.search(addr)
            filename = 'mycsv/' + addr
            engine.output('csv',filename)
            links = results.links()
            time.sleep(1)
        except Exception:
            time.sleep(5)
            count += 1
            if count >= 50 :
                quit()
            mysearch(addr)
            # print(addr)
            # results = engine.search(addr)
            # engine.output('html',filename)
    # print(links)
if __name__ == '__main__':
    mysearch()
