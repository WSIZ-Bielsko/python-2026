from uuid import uuid4

if __name__ == '__main__':
    w = ['' for _ in range(100000)]
    w[10] = '112233'
    w[99999] = '112211'

    # czy wartosc '112211' jest w "w" ?
    if '112211' in w:
        print('yes')

    # print(w)
    # transakcje.....
    # dane dodatkowe transakcji...

    # 5mld ... 5 * 10^9

    # baza: pesel -> [] (lista eventów) ... pesel = 11 cyfr... => 100mld... .. ale tylko 35mln obywateli....

    ww = dict()  # {}
    ww[10] = '112233'
    print(ww)
    print('112211' in ww)

    w = (1, 2, 1)

    ww['abrakadabra'] = 'hokus pokus'
    u = uuid4()
    print(u)
    ww[u] = 18