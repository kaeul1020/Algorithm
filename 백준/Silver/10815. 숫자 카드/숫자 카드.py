import sys

sys.stdin.readline()
n_cards = list(map(int, sys.stdin.readline().split(' ')))
sys.stdin.readline()
m_cards = list(map(int, sys.stdin.readline().split(' ')))
n_ckp = {}

for nc in n_cards:
    n_ckp[nc] = 1

for mc in m_cards:
    try :
        print(n_ckp[mc], end=" ")
    except:
        print(0, end=" ")