import math
import numpy as np
import PySimpleGUI as psg


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


def simulate(x, a, c, m, i, ba, bs):
    arrive = randExponential(x, a, c, m, i, ba)  # rand kedatangan
    service = randExponential(x, a, c, m, i, bs)  # rand service
    while (arrive == service):  # isi array diacak acak sampai tidak sama
        np.random.shuffle(arrive)
        np.random.shuffle(service)
    # arrive = [0.34056,0.29353,1.78004,0.76183,2.343] #a2
    # service = [0.17117,0.34364,0.1947,0.31147,0.45238]
    # arrive = [0.58781, 0.58218, 0.22566 , 0.12384, 0.11962] #a4
    # service = [0.19333, 0.19147, 0.07422, 0.04073, 0.03934]
    # arrive = [0.28607,0.57492,2.43039,0.05544,1.47267] #e1
    # service = [0.17333,0.34834,1.47257,0.03359,0.89229]
    # arrive = [0.39724,0.03267,0.28362,0.35794,0.12551] #a5
    # service = [1.00057,0.23425,0.05605,0.90371,0.02575]
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

    print("Init Time")
    # report(statArrive, underService, serverStat, clock, numberInQueue,
    #        timesOfArrival, numberDelayed, totalDelayed, qt, bt, nextArrive, nextDepart)
    clock = nextArrive
    for i in range(iterasi):
        print("iter ", i)
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
        # print(arrive)
        # print(service)
        # report(statArrive, underService, serverStat, clock, numberInQueue,
        #        timesOfArrival, numberDelayed, totalDelayed, qt, bt, nextArrive, nextDepart)
        if i != iterasi-1:  # selama bukan iterasi terakhir clock terus diupdate
            clock = min(nextArrive, nextDepart)
        print()

    dn = totalDelayed/numberDelayed
    qn = qt/clock
    un = bt/clock

    return dn, qn, un
    # print("d(n) : ", dn)
    # print("q(n) : ", qn)
    # print("u(n) : ", un)


# simulate(15, 75, 74, 2**16+1, 70, 0.1)
# Gui
layout = [
    [psg.Text('qs')],
    [psg.Text('Beta Arrival\t:'), psg.Input(key='-BA-'), ],
    [psg.Text('Beda Service\t:'), psg.Input(key='-BS-')],
    [psg.Text('N\t\t:'), psg.Input(key='-N-', size=(10, 2))],
    #  psg.Text('How many run\t:'), psg.Input(key='-Ns-', size=(10, 2))],
    [psg.Text('d(n):'), psg.Text(key='-DN-')],
    [psg.Text('q(n):'), psg.Text(key='-QN-')],
    [psg.Text('u(n):'), psg.Text(key='-UN-')],
    [psg.Button('Run Simulation'), psg.Exit()]
]

window = psg.Window('Kantin AI - Simulation', layout,
                    enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == "Run Simulation":
        ba = float(values['-BA-'])
        bs = float(values['-BS-'])
        n = int(values['-N-'])
        # ns = int(values['-Ns-'])

        # for _ in range(ns):

        simulasi = simulate(15, 75, 74, 2**16+1, n, ba, bs)
        dn, qn, un = simulasi
        window['-DN-'].update(dn)
        window['-QN-'].update(qn)
        window['-UN-'].update(un)
    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?', title='Elgamal') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
window.close()
