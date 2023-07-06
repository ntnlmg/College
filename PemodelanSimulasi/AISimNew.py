import math
import numpy as np
import PySimpleGUI as psg
import pandas as pd


def report(statArrive, underService, serverStat, clock, numberInQueue, timesOfArrival, numberDelayed, totalDelay, qt, bt, nextArrive, nextDepart):
    print("Clock : ", clock)
    print("Next arrive : ", nextArrive)
    print("Next departure : ", nextDepart)
    print("Under service : ", underService)
    print("Server status : ", serverStat)
    print("Number in queue : ", numberInQueue)
    print("Times of arrival :")
    for i in range(len(timesOfArrival)):
        print(timesOfArrival[i])
    print("Times of last event : ", clock)
    print("Number delayed : ", numberDelayed)
    print("Total delayed : ", totalDelay)
    print("Q(t) : ", qt)
    print("B(t) : ", bt)
    print()


def lcg(x, a, c, m, i):
    list = []
    list.append(round(x/m, 5))
    for iterasi in range(i-1):
        x = (a*x+c) % m
        r = round(x/m, 5)
        list.append(r)
    return list


def randExponential(x, a, c, m, i, b):
    listExp = []
    uniform = lcg(x, a, c, m, i)
    for i in range(len(uniform)):
        x = round(-b * math.log(1-uniform[i], math.e), 5)
        listExp.append(x)
    return listExp


def simulate(x, a, c, m, i, ba, bs):
    arrive = randExponential(x, a, c, m, i, ba)  # rand kedatangan
    service = randExponential(x, a, c, m, i, bs)  # rand service

    # isi array diacak acak sampai tidak sama
    np.random.shuffle(arrive)
    np.random.shuffle(service)
    iterasi = len(arrive)+len(service)
    underService = 0
    clock = 0
    clockPrev = 0
    numberInQueue = 0
    numberDelayed = 0
    totalDelayed = 0
    qt = 0
    isQt = False
    bt = 0
    isBt = False
    timesOfArrival = []
    nextArrive = arrive[0]
    nextDepart = math.inf
    serverStat = 0
    statArrive = True

    clock = nextArrive
    for i in range(iterasi):
        # print("iter ", i)
        if isBt:
            bt += clock - clockPrev
            isBt = False
        if isQt:
            qt += (clock - clockPrev)*numberInQueue
            isQt = False
        if (min(nextArrive, nextDepart) == nextDepart):  # cek kalau misal depart
            # print("Departure time : ", clock)
            statArrive = False  # next depart
            if (len(timesOfArrival) != 0):  # masih error #cek antrian kosong gk. ini kalau nggk kosong
                # pindahin antrian paling atas untuk dilayani
                underService = timesOfArrival[0]
                for j in range(1, len(timesOfArrival)):  # untuk mindahin queue
                    timesOfArrival[j-1] = timesOfArrival[j]
                timesOfArrival.remove(timesOfArrival[len(timesOfArrival)-1])
                # sama kyk yg remove dibawah biar arraynya mundur dan bisa diassign
                service.remove(service[0])
                if service != []:  # selama service belum selesai
                    # update nextDepart kalau masih ada
                    nextDepart = clock + service[0]
                    totalDelayed += clock - underService
                    numberDelayed += 1
                    numberInQueue -= 1
                    isQt = True
                    isBt = True
                    clockPrev = clock
                else:  # kalau misal service udah selesai semua / last iterasi
                    nextDepart = math.inf
            else:  # kalau antrian kosong
                underService = 0
                serverStat = 0
                # sama kyk yg remove dibawah biar arraynya mundur dan bisa diassign
                service.remove(service[0])
                nextDepart = math.inf
        else:  # arrive
            # print("Arrival time : ", clock)
            if (underService != 0):  # kalau ada yang dilayani maka ya ngantri
                timesOfArrival.append(clock)
                numberInQueue += 1
                isQt = True
                isBt = True
                clockPrev = clock
            else:  # jika antrian kosong
                underService = clock
                numberDelayed += 1
                serverStat = 1
                isBt = True
                clockPrev = clock
                nextDepart = clock + service[0]
            # eliminate kasus ini supaya lebih gampang aja assign arraynya, ibarat bold kalau di excel
            arrive.remove(arrive[0])
            if (arrive != []):
                # update nextArrive jika masih ada
                nextArrive = clock + arrive[0]
            else:
                nextArrive = math.inf  # kalau sudah habis

        if i != iterasi-1:  # selama bukan iterasi terakhir clock terus diupdate
            clock = min(nextArrive, nextDepart)
        print()

    dn = round(totalDelayed/numberDelayed, 2)
    qn = round(qt/clock)
    un = round(bt/clock, 2)

    return dn, qn, un


psg.set_options(font=('Arial Bold', 25))
layout = [
    [psg.Text('Input the beta for arrival and service, Number of data (N)')],
    [psg.Text('Beta Arrival\t:'),
     psg.Input(key='-BA-')],
    [psg.Text('Beta Service\t:'), psg.Input(key='-BS-')],
    [psg.Text('How many data\t:'), psg.Input(key='-N-')],
    [psg.Text('How many run\t:'), psg.Input(key='-Ns-')],
    [psg.Button('Run Simulation'), psg.Exit()]
]

window = psg.Window('Kantin AI - Simulation', layout,
                    size=(1000, 300), enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == "Run Simulation":
        # mengecek apakah disetiap input ada isinya atau tidak, kalau tidak ada isinya dia bakal err
        if values['-BA-'] == '' or values['-BS-'] == '' or values['-N-'] == '':
            pop = psg.popup('Err : Missing input !', title="Error")
            continue

        ba = float(values['-BA-'])
        bs = float(values['-BS-'])
        n = int(values['-N-'])

        if values['-Ns-'] == '':
            ns = int("1")
            pass
        else:
            ns = int(values['-Ns-'])

        result = []
        for i in range(ns):
            simulasi = simulate(15, 75, 74, 2**16+1, n, ba, bs)
            dn, qn, un = simulasi
            inner_result = [i+1, dn, qn, un]
            result.append(inner_result)
            []
        data_sim = pd.DataFrame(result)
        data_sim.to_csv(f"data_sim{ba, bs}.csv", index=False)
        psg.popup_scrolled(
            result, title="Hasil simulasi [iterasi, dn, qn, un]", size=(50, 10))

    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
window.close()
