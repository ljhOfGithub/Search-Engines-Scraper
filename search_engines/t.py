from search_engines import Google
from ast import literal_eval
import time
import argparse
import os
import traceback
# import arg
# def mysearch(csvaddr='0x5b27531228d8c65a0d2adcd8903fd3348f768a11'):
# def mysearch(csvaddr='0xb01fce059d66971fdc1e584a5cbf0116068c9048'):
# def mysearch(csvaddr='0x81e4b65b9330c5693d38430111d7eb174615bdd6'):
# def mysearch(csvaddr='0x98831a269cb88b6bfcc86e45b32c158981b34b22'):
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-q', help='query to search', default='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91')
    args = ap.parse_args()
    csvaddr = args.q
    mysearch(csvaddr)

def mysearch(csvaddr='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'):
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
            time.sleep(2)
        except Exception:
            print('reboot')
            time.sleep(5)
            myindex = addrlist.index(addr) - 1#
            rebootaddr = addrlist[myindex]
            count += 1
            if count >= 50:
                quit()
            # mysearch(rebootaddr)
            os.execv('/root/.miniconda3/envs/twvenv/bin/python',['python','t.py','-q',rebootaddr])

            # print(addr)
            # results = engine.search(addr)
            # engine.output('html',filename)
    # print(links)
def winsearch(csvaddr='0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'):
    with open('addr.txt','r') as f:
        addrlist = literal_eval(f.read())
        # csvaddr = '0x3bf351a62df57dce8512b136daa4cd6ebe2dda91'
        count = 0
        myindex = addrlist.index(csvaddr)
        addrlist = addrlist[myindex:]
        engine = Google()
    for addr in addrlist:
        try:
            engine.set_search_operator('host')  # 设置为将对应的host过滤掉
            results = engine.search(addr)
            filename = 'mycsv/' + addr
            engine.output('csv', filename)
            links = results.links()
            time.sleep(2)
        except Exception:
            print('reboot')
            time.sleep(5)
            myindex = addrlist.index(addr) - 1  #
            rebootaddr = addrlist[myindex]
            count += 1
            if count >= 50:
                quit()
            traceback.print_exc()
            mysearch(rebootaddr)

            # os.execv('/root/.miniconda3/envs/twvenv/bin/python', ['python', 't.py', '-q', rebootaddr])
#0x3bf351a62df57dce8512b136daa4cd6ebe2dda91
#0xd67e205a5b7a5d82b86afbc59f67f74a878d1e68
if __name__ == '__main__':
    # mysearch()
    # main()
    winsearch()

#python t.py -q 0x3bf351a62df57dce8512b136daa4cd6ebe2dda91