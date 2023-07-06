from tkinter import *
from tkinter import ttk
import math
from array import array
import matplotlib.pyplot as plt

root = Tk()
root.title("Simulator Antrian")
# root.iconbitmap('D:/Ma Chung/Semester 4/Pemodelan Simulasi/UAS - Simulator/queue.ico')

main_frame = LabelFrame(root, padx=5, pady=5)
main_frame.pack(ipadx=5, ipady=5, padx=3, pady=3)
Label(root, text="Universitas Ma Chung | Dibuat oleh : Stanley Adi Dewangga & Catherine Kezia Wijaya").pack()

text_event = "Initialization Time"
step = 0

# input
frame_input = LabelFrame(main_frame, text="Input", padx=10, pady=10, labelanchor=N)
label = Label(frame_input, text="Mean Waktu Kedatangan : ")
input_waktuKedatangan = Entry(frame_input, width=10)
label2 = Label(frame_input, text="Mean Lama Pelayanan : ")
input_lamaPelayanan = Entry(frame_input, width=10)
label3 = Label(frame_input, text="Banyak Data : ")
input_banyakData = Entry(frame_input, width=10)
# layout input
frame_input.grid(row=0, column=0, ipady=10)
label.grid(row=0, column=0, pady=10, sticky=W)
input_waktuKedatangan.grid(row=0, column=1, pady=10, sticky=W)
label2.grid(row=1, column=0, pady=10, sticky=W)
input_lamaPelayanan.grid(row=1, column=1, pady=10, sticky=W)
label3.grid(row=2, column=0, pady=10, sticky=W)
input_banyakData.grid(row=2, column=1, pady=10, sticky=W)

# Frame running
frame_hasilRun = LabelFrame(main_frame, text="Hasil Running", padx=5, pady=5, labelanchor=N)
# system
frame_system = LabelFrame(frame_hasilRun, text="System", labelanchor=S)
frame_event = LabelFrame(frame_system, text=text_event)
event_value = Label(frame_event, text="0", bd=1, relief=SUNKEN)
next_arr = Label(frame_system, text="0", width=7, bd=1, relief=SUNKEN)
stack_arrival = LabelFrame(frame_system, borderwidth=0)
next_next_arr = Label(stack_arrival, text="0", width=7, bd=1, relief=SUNKEN)
lebih2 = Label(stack_arrival, text="", width=7)
# system state
frame_systemState = LabelFrame(frame_hasilRun, text="System State", labelanchor=N)
serverStatus_value = Label(frame_systemState, text="0", width=4, bd=1, relief=SUNKEN)
serverStatus = Label(frame_systemState, text="Server Status")
number_in_queue_value = Label(frame_systemState, text="0", width=7, bd=1, relief=SUNKEN)
number_in_queue = Label(frame_systemState, text="Number in Queue")
stack_timeArrival = LabelFrame(frame_systemState, borderwidth=0)
timeArrival_value = Label(stack_timeArrival, text="0", bd=1, width=8, relief=SUNKEN)
timeArrival = Label(frame_systemState, text="Time of Arrival")
timeEvent_value = Label(frame_systemState, text="0", width=7, bd=1, relief=SUNKEN)
lebih1 = Label(stack_timeArrival, text="", width=7)
timeEvent = Label(frame_systemState, text="Time of Event")
# frame kanan
blank_frame = LabelFrame(frame_hasilRun)
# frame clock & arr_dep
frame_clock = LabelFrame(blank_frame)
clock_value = Label(frame_clock, text="0", width=5, height=2, bd=2, relief=SUNKEN)
clock = Label(frame_clock, text="Clock")
nextArrival = Label(frame_clock, text="Next Arrival : ")
nextArrival_value = Label(frame_clock, text="0", width=5, bd=1, relief=SUNKEN)
nextDepart = Label(frame_clock, text="Next Depart : ")
nextDepart_value = Label(frame_clock, text="0", width=5, bd=1, relief=SUNKEN)
# frame counter (bawah)
frame_counter = LabelFrame(blank_frame)
numberDelayed_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
numberDelayed = Label(frame_counter, text="Number Delayed")
totalDelay_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
totalDelay = Label(frame_counter, text="Total Delay")
areaUnderQt_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
areaUnderQt = Label(frame_counter, text="Area Under Q(t)")
areaUnderBt_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
areaUnderBt = Label(frame_counter, text="Area Under B(t)")

# layout frame Running
frame_hasilRun.grid(row=0, column=1, padx=5, pady=5)
# system
frame_system.grid(row=0, column=0)
frame_event.grid(row=0, column=0, padx=5, pady=5)
event_value.pack()
next_arr.grid(row=1, column=0, padx=8, pady=8)
lebih2.pack()
stack_arrival.grid(row=2, column=0, sticky=W + E, padx=10, pady=5)
next_next_arr.pack(pady=2)

# system state
frame_systemState.grid(row=0, column=1, padx=5, pady=5)
serverStatus_value.grid(row=0, column=0)
serverStatus.grid(row=1, column=0)
number_in_queue_value.grid(row=0, column=1)
number_in_queue.grid(row=1, column=1)
stack_timeArrival.grid(row=0, column=2)
timeArrival_value.pack()
lebih1.pack()
timeArrival.grid(row=1, column=2)
timeEvent_value.grid(row=0, column=3)
timeEvent.grid(row=1, column=3)
# frame kanan
blank_frame.grid(row=0, column=2)
# frame clock
frame_clock.pack(side=TOP, padx=5, pady=5)
clock_value.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
clock.grid(row=2, column=0)
nextArrival_value.grid(row=0, column=2, padx=5, pady=5, sticky=E)
nextArrival.grid(row=0, column=1)
nextDepart_value.grid(row=1, column=2, padx=5, pady=5, sticky=E)
nextDepart.grid(row=1, column=1)
# frame counter
frame_counter.pack(side=BOTTOM, padx=5, pady=5)
numberDelayed_value.grid(row=0, column=0, pady=5)
numberDelayed.grid(row=1, column=0)
totalDelay_value.grid(row=0, column=1)
totalDelay.grid(row=1, column=1)
areaUnderQt_value.grid(row=0, column=2)
areaUnderQt.grid(row=1, column=2)
areaUnderBt_value.grid(row=0, column=3)
areaUnderBt.grid(row=1, column=3)

# frame Statistical Counter
frame_sc = LabelFrame(main_frame, text="Statistical Counter", padx=5, pady=5, labelanchor=N)
frame_dn = LabelFrame(frame_sc, padx=5, pady=5)
frame_qn = LabelFrame(frame_sc, padx=5, pady=5)
frame_u = LabelFrame(frame_sc, padx=5, pady=5)
dn = Label(frame_dn, text="Rata - rata lama antrian = ")
qn = Label(frame_qn, text="Rata - rata banyak orang dalam antrian = ")
u = Label(frame_u, text="Utilitas = ")
dn_value = Label(frame_dn, text="   ", bd=1, relief=SUNKEN, width=7)
qn_value = Label(frame_qn, text="   ", bd=1, relief=SUNKEN, width=7)
u_value = Label(frame_u, text="   ", bd=1, relief=SUNKEN, width=7)

# layout statistical counter
frame_sc.grid(row=2, column=1, sticky=N)
frame_dn.grid(row=0, column=0, padx=5)
frame_qn.grid(row=0, column=1, padx=5)
frame_u.grid(row=0, column=2, padx=5)
dn.grid(row=0, column=0, padx=5)
dn_value.grid(row=0, column=1, padx=10)
qn.grid(row=0, column=0, padx=5)
qn_value.grid(row=0, column=1)
u.grid(row=0, column=0, padx=5)
u_value.grid(row=0, column=1)


log_tree = ttk.Treeview(main_frame, height=5)
log_tree['columns'] = ("No", "Delay", "Queue", "Utility")

log_tree.column("#0", width=0, stretch=NO)
log_tree.column("No", anchor=CENTER, width=30, minwidth=25, stretch=TRUE)
log_tree.column("Delay", anchor=CENTER, width=60, minwidth=40, stretch=TRUE)
log_tree.column("Queue", anchor=CENTER, width=70, minwidth=45, stretch=TRUE)
log_tree.column("Utility", anchor=CENTER, width=60, minwidth=35, stretch=TRUE)

log_tree.heading("#0", anchor=W)
log_tree.heading("No", text="No", anchor=CENTER)
log_tree.heading("Delay", text="Delay", anchor=CENTER)
log_tree.heading("Queue", text="Queue", anchor=CENTER)
log_tree.heading("Utility", text="Utility", anchor=CENTER)

log_tree.grid(row=2, column=0, rowspan=2, sticky=N)

# generate number eksponen
def generateEksponen(banyakData):
    # lcg
    # input nilai x, a, c, m untuk menghitung lcg
    x0 = 48342
    x = x0
    a = 31071
    c = 0
    m = 0.99187
    data = []
    for i in range(0, banyakData + 1):
        LCG = ((a * x) + c) % m
        data.append(LCG)
        x = LCG
    # cek long cycle
    count = 0
    data_lolos = []
    sama = False
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if (data[i] == data[j]):
                sama = True
        if (sama == True):
            break
        else:
            data_lolos.append(data[i])
            count += 1
    return data_lolos

# transformasi invers
def transformasi_invers(mean, data):
    t = (-(mean)) * (math.log(1 - data))
    return t

class Hasil(object):
    def __init__(self):
        self.tambah_indeks_data = 0
        self.arrivalTime = []
        self.departTime = [99999]
        self.hasil_generate = []
        self.hasil_generate1 = []
        self.hasil_generate2 = []
        self.array_clock = [0]
        self.array_keterangan = ["Initialization Time"]
        self.array_nextarrival = [0]
        self.array_nextdepart = [0]
        self.array_numberdelay = [0]
        self.array_next_queue = [0]
        self.array_serverStatus = [0]
        self.array_numberInQueue = [0]
        self.array_areaUnderQt = [0]
        self.array_areaUnderBt = [0]
        self.array_utilitas = [0]
        self.array_total_delay = [0]
        self.array_timeOfArrival = [[0]]
        self.array_in_service = [0]
        self.array_dn = [0]
        self.array_qn = [0]

    def add_clock(self, arg):
        self.array_clock.append(arg)

    def add_keterangan(self, arg):
        self.array_keterangan.append(arg)

    def change_generate(self, arg):
        self.hasil_generate = arg

    def add_generator1(self, arg):
        self.hasil_generate1.append(arg)

    def add_generator2(self, arg):
        self.hasil_generate2.append(arg)

    def change_arrival_time(self, arg):
        self.arrivalTime = arg

    def add_depart_time(self, arg):
        self.departTime.append(arg)

    def add_next_arrival(self, arg):
        self.array_nextarrival.append(arg)

    def add_next_depart(self, arg):
        self.array_nextdepart.append(arg)

    def add_number_delay(self, arg):
        self.array_numberdelay.append(arg)

    def add_next_queue(self, arg):
        self.array_next_queue.append(arg)

    def add_areaUnderQt(self, arg):
        self.array_areaUnderQt.append(arg)

    def add_areaUnderBt(self, arg):
        self.array_areaUnderBt.append(arg)

    def add_dn(self, arg):
        self.array_dn.append(arg)

    def add_qn(self, arg):
        self.array_qn.append(arg)

    def add_utilitas(self, arg):
        self.array_utilitas.append(arg)

    def add_numberInQueue(self, arg):
        self.array_numberInQueue.append(arg)

    def add_total_delay(self, arg):
        self.array_total_delay.append(arg)

    def add_serverStatus(self, arg):
        self.array_serverStatus.append(arg)

    def add_indeks_data(self, arg):
        if self.tambah_indeks_data < (int(input_banyakData.get())*18):
            self.tambah_indeks_data += arg
        else:
            self.tambah_indeks_data = 0

    def add_timeOfArrival(self, arg):
        self.array_timeOfArrival.append(arg)

    def add_in_service(self, arg):
        self.array_in_service.append(arg)

    def hapusData(self):
        self.arrivalTime = []
        self.arrivalTime = []
        self.departTime = [99999]
        self.hasil_generate = []
        self.hasil_generate1 = []
        self.hasil_generate2 = []
        self.array_clock = [0]
        self.array_keterangan = ["Initialization Time"]
        self.array_nextarrival = [0]
        self.array_nextdepart = [0]
        self.array_numberdelay = [0]
        self.array_next_queue = [0]
        self.array_serverStatus = [0]
        self.array_numberInQueue = [0]
        self.array_areaUnderQt = [0]
        self.array_areaUnderBt = [0]
        self.array_utilitas = [0]
        self.array_total_delay = [0]
        self.array_timeOfArrival = [[0]]
        self.array_in_service = [0]
        self.array_dn = [0]
        self.array_qn = [0]

hasil = Hasil()

def generate_command():
    global input_waktuKedatangan, input_lamaPelayanan

    if input_banyakData.get() == '' or input_lamaPelayanan.get() == '' or input_banyakData.get() == '':
        Label(frame_run, text="Masukkan Input..", width=15).grid(row=0, column=1)
    else:
        Label(frame_run, text="Berhasil digenerate!", width=15).grid(row=0, column=1)

        hasil.change_generate(generateEksponen(int(input_banyakData.get())*20))

        #membuat uniform random -> eksponen
        for i in range(int(input_banyakData.get())):
            hasil.add_generator1(transformasi_invers(float(input_waktuKedatangan.get()),
                                                     hasil.hasil_generate[(i + hasil.tambah_indeks_data)]))
            hasil.add_generator2(transformasi_invers(float(input_lamaPelayanan.get()),
                                                     hasil.hasil_generate[(i + int(input_banyakData.get()) + hasil.tambah_indeks_data)]))

        tempArrival = []
        serviceTime = [99999]
        for i in range(int(input_banyakData.get())):
            tempArrival.append(hasil.hasil_generate1[i])
            serviceTime.append(hasil.hasil_generate2[i])

        arrivalTime = []
        v_tempArrival = 0
        for i in tempArrival:
            v_tempArrival += i
            arrivalTime.append(v_tempArrival)
        hasil.change_arrival_time(arrivalTime)
        arrivalTime.append(99999)
        status = 0
        numberdelay = 0
        next_queue = 0
        numberInQueue = 0
        arrival = 0
        depart = 0
        arrival_index = 0
        service_index = 0
        stack = array('f')
        in_service = 0

        for i in range(int(input_banyakData.get())):
            arrival = arrivalTime[arrival_index]
            if i == 0:
                depart = serviceTime[service_index]
            hasil.add_next_depart(depart)
            hasil.add_next_arrival(arrival)
            if arrival < depart:
                next_queue += 1
                if service_index == 0:
                    service_index += 1
                hasil.add_keterangan("Arrival")
                hasil.add_clock(arrival)

                if next_queue > 1:
                    numberInQueue += 1
                    stack.append(arrival)
                else:
                    in_service = arrival
                    depart = arrivalTime[arrival_index] + serviceTime[service_index]
                status = 1
                arrival_index += 1
            else:
                hasil.add_keterangan("Departure")
                hasil.add_clock(depart)
                hasil.add_depart_time(depart)
                if next_queue > 1:
                    in_service = arrivalTime[arrival_index - numberInQueue]
                    numberInQueue -= 1
                    stack.pop(0)
                else:
                    in_service = arrival
                    numberInQueue = 0
                    stack = array('f')
                next_queue -= 1

                if next_queue == 0:
                    in_service = 0
                    status = 0

                if status == 0:
                    depart = 99999
                else:
                    numberdelay += 1
                    depart += serviceTime[service_index]
                service_index += 1
            hasil.add_in_service(in_service)
            hasil.add_timeOfArrival(stack.tolist())
            hasil.add_serverStatus(status)
            hasil.add_next_queue(next_queue)
            hasil.add_numberInQueue(numberInQueue)
            hasil.add_number_delay(numberdelay)

        qT = 0
        bT = 0
        total_delay = 0
        for i in range(len(hasil.array_clock)-1):
            if hasil.array_keterangan[i] == "Departure":
                total_delay += hasil.array_clock[i] - hasil.array_clock[i - hasil.array_next_queue[i]]
            qT += hasil.array_numberInQueue[i] * (hasil.array_clock[i + 1] - hasil.array_clock[i])
            bT += hasil.array_serverStatus[i] * (hasil.array_clock[i + 1] - hasil.array_clock[i])
            hasil.add_total_delay(total_delay)
            hasil.add_areaUnderQt(qT)
            hasil.add_areaUnderBt(bT)

            if hasil.array_numberdelay[i] != 0:
                hasil.add_dn(total_delay/hasil.array_numberdelay[i])
            else:
                hasil.add_dn(0)
            hasil.add_qn(qT/hasil.array_clock[i+1])
            hasil.add_utilitas(bT/hasil.array_clock[i+1])


arrival_counter = 0
service_counter = 0
counter = 1

def insertLog(indeks):
    global counter
    log_tree.insert(parent='', index='end', id=str(counter),
                    values=(counter,
                            "%.4f" % hasil.array_dn[indeks],
                            "%.4f" % hasil.array_qn[indeks],
                            "%.4f" % hasil.array_utilitas[indeks]))
    counter += 1

def run(i):
    global event_value, next_arr, next_next_arr, frame_event
    global serverStatus_value, number_in_queue_value, timeArrival_value, timeEvent_value
    global clock_value, nextArrival_value, nextDepart_value, numberDelayed_value
    global totalDelay_value, areaUnderQt_value, areaUnderBt_value
    global dn_value, qn_value, u_value, button_next, button_previous
    global text_event, stack_timeArrival, stack_arrival, step
    global lebih1, lebih2

    if input_waktuKedatangan.get() == '' or input_lamaPelayanan.get() == '' or input_banyakData.get() == '':
        teks = "Masukkan Input.."
        peringatan = Label(frame_run, text=teks, width=15)
        peringatan.grid(row=0, column=1)
    else:

        teks = "Diganti ke data akhir!"
        peringatan = Label(frame_run, text=teks, width=15)
        peringatan.grid(row=0, column=1)

        step = int(input_banyakData.get()) - 1

        try:
            text_event = hasil.array_keterangan[step]
            frame_event.grid_forget()
            frame_event = LabelFrame(frame_system, text=text_event)
            frame_event.grid(row=0, column=0, padx=5, pady=5)
            event_value.pack_forget()
            event_value = Label(frame_event, text="%.2f" % hasil.array_clock[step], bd=1, relief=SUNKEN)
            event_value.pack()
            clock_value.grid_forget()
            clock_value = Label(frame_clock, text="%.2f" % hasil.array_clock[step], width=5, height=2, bd=2,
                                relief=SUNKEN)
            clock_value.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
            timeEvent_value.grid_forget()
            timeEvent_value = Label(frame_systemState, text="%.2f" % hasil.array_clock[step], width=7, bd=1,
                                    relief=SUNKEN)
            timeEvent_value.grid(row=0, column=3)
            nextArrival_value.grid_forget()
            nextArrival_value = Label(frame_clock, text="%.2f" % hasil.array_nextarrival[step + 1], width=5, bd=1,
                                      relief=SUNKEN)
            nextArrival_value.grid(row=0, column=2, padx=5, pady=5, sticky=E)
            nextDepart_value.grid_forget()
            nextDepart_value = Label(frame_clock, text="%.2f" % hasil.array_nextdepart[step + 1], width=5, bd=1,
                                     relief=SUNKEN)
            nextDepart_value.grid(row=1, column=2, padx=5, pady=5, sticky=E)
            serverStatus_value.grid_forget()
            serverStatus_value = Label(frame_systemState, text=hasil.array_serverStatus[step], width=7, bd=1,
                                       relief=SUNKEN)
            serverStatus_value.grid(row=0, column=0)
            number_in_queue_value.grid_forget()
            number_in_queue_value = Label(frame_systemState, text=hasil.array_numberInQueue[step], width=7, bd=1,
                                          relief=SUNKEN)
            number_in_queue_value.grid(row=0, column=1)
            numberDelayed_value.grid_forget()
            numberDelayed_value = Label(frame_counter, text=hasil.array_numberdelay[step], width=7, height=2, bd=2,
                                        relief=SUNKEN)
            numberDelayed_value.grid(row=0, column=0, pady=5)
            totalDelay_value.grid_forget()
            totalDelay_value = Label(frame_counter, text="%.2f" % hasil.array_total_delay[step], width=7, height=2,
                                     bd=2,
                                     relief=SUNKEN)
            totalDelay_value.grid(row=0, column=1)

            next_arr.grid_forget()
            next_arr = Label(frame_system, text="%.2f" % hasil.array_in_service[step], width=7, bd=1, relief=SUNKEN)
            next_arr.grid(row=1, column=0, padx=8, pady=8)

            stack_timeArrival.grid_forget()
            stack_timeArrival = LabelFrame(frame_systemState, borderwidth=0)
            stack_timeArrival.grid(row=0, column=2)
            stack_arrival.grid_forget()
            stack_arrival = LabelFrame(frame_system, borderwidth=0)
            stack_arrival.grid(row=2, column=0, sticky=W + E, padx=10, pady=5)
            for i in range(len(hasil.array_timeOfArrival[step])):
                if i < 10:
                    next_next_arr = Label(stack_arrival, text="%.2f" % hasil.array_timeOfArrival[step][i], width=7, bd=1,
                                          relief=SUNKEN)
                    next_next_arr.pack()
                    timeArrival_value = Label(stack_timeArrival, text="%.2f" % hasil.array_timeOfArrival[step][i], bd=1,
                                              width=8, relief=SUNKEN)
                    timeArrival_value.pack()
                else:
                    lebih1.pack_forget()
                    lebih1 = Label(stack_timeArrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                                   width=8)
                    lebih1.pack()
                    lebih2.pack_forget()
                    lebih2 = Label(stack_arrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                                   width=8)
                    lebih2.pack()

            areaUnderQt_value.grid_forget()
            areaUnderQt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderQt[step], width=7, height=2,
                                      bd=2,
                                      relief=SUNKEN)
            areaUnderQt_value.grid(row=0, column=2)
            areaUnderBt_value.grid_forget()
            areaUnderBt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderBt[step], width=7, height=2,
                                      bd=2, relief=SUNKEN)
            areaUnderBt_value.grid(row=0, column=3)

            dn_value.grid_forget()
            dn_value = Label(frame_dn, text="%.2f" % hasil.array_dn[step], bd=1, relief=SUNKEN, width=7)
            dn_value.grid(row=0, column=1, padx=10)
            qn_value.grid_forget()
            qn_value = Label(frame_qn, text="%.2f" % hasil.array_qn[step], bd=1, relief=SUNKEN, width=7)
            qn_value.grid(row=0, column=1, padx=10)
            u_value.grid_forget()
            u_value = Label(frame_u, text="%.2f" % hasil.array_utilitas[step], bd=1, relief=SUNKEN, width=7)
            u_value.grid(row=0, column=1, padx=10)

            insertLog(step)

            dataKe = Label(frame_run, text="data ke - " + str(step), width=15)
            dataKe.grid(row=2, column=1)

            button_next = Button(frame_run, text=">>", width=4, command=lambda: next(i + 1))
            button_previous = Button(frame_run, text="<<", width=4, command=lambda: previous(i - 1))
            if step == int(input_banyakData.get())-1:
                button_next = Button(frame_run, text=">>", width=4, state=DISABLED)
            button_next.grid(row=1, column=2, pady=5, padx=5)
            button_previous.grid(row=1, column=0, pady=5, padx=5)
        except:
            Label(frame_run, text="Error! Data kosong", width=15).grid(row=0, column=1)


def next(i):
    global button_next, button_previous, step
    global event_value, next_arr, next_next_arr, frame_event
    global serverStatus_value, number_in_queue_value, timeArrival_value, timeEvent_value
    global clock_value, nextArrival_value, nextDepart_value, numberDelayed_value
    global totalDelay_value, areaUnderQt_value, areaUnderBt_value
    global dn_value, qn_value, u_value
    global text_event, stack_timeArrival, stack_arrival
    global arrival_counter, service_counter, lebih1, lebih2

    if input_banyakData.get() == '' or input_lamaPelayanan.get() == '' or input_banyakData.get() == '':
        Label(frame_run, text="Masukkan Input..", width=15).grid(row=0, column=1)
    else:
        Label(frame_run, text=" ", width=15).grid(row=0, column=1)

        step += 1

        try:
            text_event = hasil.array_keterangan[step]
            frame_event.grid_forget()
            frame_event = LabelFrame(frame_system, text=text_event)
            frame_event.grid(row=0, column=0, padx=5, pady=5)
            event_value.pack_forget()
            event_value = Label(frame_event, text="%.2f" % hasil.array_clock[step], bd=1, relief=SUNKEN)
            event_value.pack()
            clock_value.grid_forget()
            clock_value = Label(frame_clock, text="%.2f" % hasil.array_clock[step], width=5, height=2, bd=2, relief=SUNKEN)
            clock_value.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
            timeEvent_value.grid_forget()
            timeEvent_value = Label(frame_systemState, text="%.2f" % hasil.array_clock[step], width=7, bd=1, relief=SUNKEN)
            timeEvent_value.grid(row=0, column=3)
            nextArrival_value.grid_forget()
            nextArrival_value = Label(frame_clock, text="%.2f" % hasil.array_nextarrival[step+1], width=5, bd=1, relief=SUNKEN)
            nextArrival_value.grid(row=0, column=2, padx=5, pady=5, sticky=E)
            nextDepart_value.grid_forget()
            nextDepart_value = Label(frame_clock, text="%.2f" % hasil.array_nextdepart[step+1], width=5, bd=1, relief=SUNKEN)
            nextDepart_value.grid(row=1, column=2, padx=5, pady=5, sticky=E)
            serverStatus_value.grid_forget()
            serverStatus_value = Label(frame_systemState, text=hasil.array_serverStatus[step], width=7, bd=1, relief=SUNKEN)
            serverStatus_value.grid(row=0, column=0)
            number_in_queue_value.grid_forget()
            number_in_queue_value = Label(frame_systemState, text=hasil.array_numberInQueue[step], width=7, bd=1, relief=SUNKEN)
            number_in_queue_value.grid(row=0, column=1)
            numberDelayed_value.grid_forget()
            numberDelayed_value = Label(frame_counter, text=hasil.array_numberdelay[step], width=7, height=2, bd=2, relief=SUNKEN)
            numberDelayed_value.grid(row=0, column=0, pady=5)
            totalDelay_value.grid_forget()
            totalDelay_value = Label(frame_counter, text="%.2f" % hasil.array_total_delay[step], width=7, height=2, bd=2, relief=SUNKEN)
            totalDelay_value.grid(row=0, column=1)
            areaUnderQt_value.grid_forget()
            areaUnderQt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderQt[step], width=7, height=2, bd=2, relief=SUNKEN)
            areaUnderQt_value.grid(row=0, column=2)
            areaUnderBt_value.grid_forget()
            areaUnderBt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderBt[step], width=7, height=2, bd=2, relief=SUNKEN)
            areaUnderBt_value.grid(row=0, column=3)
            dn_value.grid_forget()
            dn_value = Label(frame_dn, text="%.2f" % hasil.array_dn[step], bd=1, relief=SUNKEN, width=7)
            dn_value.grid(row=0, column=1, padx=10)
            qn_value.grid_forget()
            qn_value = Label(frame_qn, text="%.2f" % hasil.array_qn[step], bd=1, relief=SUNKEN, width=7)
            qn_value.grid(row=0, column=1, padx=10)
            u_value.grid_forget()
            u_value = Label(frame_u, text="%.2f" % hasil.array_utilitas[step], bd=1, relief=SUNKEN, width=7)
            u_value.grid(row=0, column=1, padx=10)

            next_arr.grid_forget()
            next_arr = Label(frame_system, text="%.2f" % hasil.array_in_service[step], width=7, bd=1, relief=SUNKEN)
            next_arr.grid(row=1, column=0, padx=8, pady=8)

            stack_timeArrival.grid_forget()
            stack_timeArrival = LabelFrame(frame_systemState, borderwidth=0)
            stack_timeArrival.grid(row=0, column=2)
            stack_arrival.grid_forget()
            stack_arrival = LabelFrame(frame_system, borderwidth=0)
            stack_arrival.grid(row=2, column=0, sticky=W + E, padx=10, pady=5)
            for i in range(len(hasil.array_timeOfArrival[step])):
                if i < 10:
                    next_next_arr = Label(stack_arrival, text="%.2f" % hasil.array_timeOfArrival[step][i], width=7,
                                          bd=1,
                                          relief=SUNKEN)
                    next_next_arr.pack()
                    timeArrival_value = Label(stack_timeArrival, text="%.2f" % hasil.array_timeOfArrival[step][i], bd=1,
                                              width=8, relief=SUNKEN)
                    timeArrival_value.pack()
                else:
                    lebih1.pack_forget()
                    lebih1 = Label(stack_timeArrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                                   width=8)
                    lebih1.pack()
                    lebih2.pack_forget()
                    lebih2 = Label(stack_arrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                                   width=8)
                    lebih2.pack()

            button_next = Button(frame_run, text=">>", width=4, command=lambda: next(i + 1))
            button_previous = Button(frame_run, text="<<", width=4, command=lambda: previous(i - 1))
            dataKe = Label(frame_run, text="data ke - " + str(step), width=15)
            dataKe.grid(row=2, column=1)
            if step == int(input_banyakData.get())-1:
                button_next = Button(frame_run, text=">>", width=4, state=DISABLED)
            if (step == 1):
                button_previous = Button(frame_run, text="<<", width=4, state=DISABLED)
            button_next.grid(row=1, column=2, pady=5, padx=5)
            button_previous.grid(row=1, column=0, pady=5, padx=5)
        except:
            Label(frame_run, text="Error! Data kosong", width=15).grid(row=0, column=1)

def previous(i):
    global button_next, button_previous, step
    global event_value, next_arr, next_next_arr, frame_event
    global serverStatus_value, number_in_queue_value, timeArrival_value, timeEvent_value
    global clock_value, nextArrival_value, nextDepart_value, numberDelayed_value
    global totalDelay_value, areaUnderQt_value, areaUnderBt_value
    global dn_value, qn_value, u_value
    global text_event, stack_timeArrival, stack_arrival
    global arrival_counter, service_counter, lebih1, lebih2

    step -= 1

    text_event = hasil.array_keterangan[step]
    frame_event.grid_forget()
    frame_event = LabelFrame(frame_system, text=text_event)
    frame_event.grid(row=0, column=0, padx=5, pady=5)
    event_value.pack_forget()
    event_value = Label(frame_event, text="%.2f" % hasil.array_clock[step], bd=1, relief=SUNKEN)
    event_value.pack()
    clock_value.grid_forget()
    clock_value = Label(frame_clock, text="%.2f" % hasil.array_clock[step], width=5, height=2, bd=2, relief=SUNKEN)
    clock_value.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
    timeEvent_value.grid_forget()
    timeEvent_value = Label(frame_systemState, text="%.2f" % hasil.array_clock[step], width=7, bd=1, relief=SUNKEN)
    timeEvent_value.grid(row=0, column=3)
    serverStatus_value.grid_forget()
    serverStatus_value = Label(frame_systemState, text=hasil.array_serverStatus[step], width=7, bd=1, relief=SUNKEN)
    serverStatus_value.grid(row=0, column=0)
    number_in_queue_value.grid_forget()
    number_in_queue_value = Label(frame_systemState, text=hasil.array_numberInQueue[step], width=7, bd=1, relief=SUNKEN)
    number_in_queue_value.grid(row=0, column=1)
    nextArrival_value.grid_forget()
    nextArrival_value = Label(frame_clock, text="%.2f" % hasil.array_nextarrival[step + 1], width=5, bd=1,relief=SUNKEN)
    nextArrival_value.grid(row=0, column=2, padx=5, pady=5, sticky=E)
    nextDepart_value.grid_forget()
    nextDepart_value = Label(frame_clock, text="%.2f" % hasil.array_nextdepart[step + 1], width=5, bd=1, relief=SUNKEN)
    nextDepart_value.grid(row=1, column=2, padx=5, pady=5, sticky=E)
    numberDelayed_value.grid_forget()
    numberDelayed_value = Label(frame_counter, text=hasil.array_numberdelay[step], width=7, height=2, bd=2,relief=SUNKEN)
    numberDelayed_value.grid(row=0, column=0, pady=5)
    totalDelay_value.grid_forget()
    totalDelay_value = Label(frame_counter, text="%.2f" % hasil.array_total_delay[step], width=7, height=2, bd=2,
                             relief=SUNKEN)
    totalDelay_value.grid(row=0, column=1)
    areaUnderQt_value.grid_forget()
    areaUnderQt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderQt[step], width=7, height=2, bd=2, relief=SUNKEN)
    areaUnderQt_value.grid(row=0, column=2)
    areaUnderBt_value.grid_forget()
    areaUnderBt_value = Label(frame_counter, text="%.2f" % hasil.array_areaUnderBt[step], width=7, height=2, bd=2, relief=SUNKEN)
    areaUnderBt_value.grid(row=0, column=3)

    next_arr.grid_forget()
    next_arr = Label(frame_system, text="%.2f" % hasil.array_in_service[step], width=7, bd=1, relief=SUNKEN)
    next_arr.grid(row=1, column=0, padx=8, pady=8)

    stack_timeArrival.grid_forget()
    stack_timeArrival = LabelFrame(frame_systemState, borderwidth=0)
    stack_timeArrival.grid(row=0, column=2)
    stack_arrival.grid_forget()
    stack_arrival = LabelFrame(frame_system, borderwidth=0)
    stack_arrival.grid(row=2, column=0, sticky=W + E, padx=10, pady=5)
    for i in range(len(hasil.array_timeOfArrival[step])):
        if i < 10:
            next_next_arr = Label(stack_arrival, text="%.2f" % hasil.array_timeOfArrival[step][i], width=7, bd=1,
                                  relief=SUNKEN)
            next_next_arr.pack()
            timeArrival_value = Label(stack_timeArrival, text="%.2f" % hasil.array_timeOfArrival[step][i], bd=1,
                                      width=8, relief=SUNKEN)
            timeArrival_value.pack()
        else:
            lebih1.pack_forget()
            lebih1 = Label(stack_timeArrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                           width=8)
            lebih1.pack()
            lebih2.pack_forget()
            lebih2 = Label(stack_arrival, text="+" + str(hasil.array_numberInQueue[step] - 10) + " more",
                           width=8)
            lebih2.pack()

    dn_value.grid_forget()
    dn_value = Label(frame_dn, text="%.2f" % hasil.array_dn[step], bd=1, relief=SUNKEN, width=7)
    dn_value.grid(row=0, column=1, padx=10)
    qn_value.grid_forget()
    qn_value = Label(frame_qn, text="%.2f" % hasil.array_qn[step], bd=1, relief=SUNKEN, width=7)
    qn_value.grid(row=0, column=1, padx=10)
    u_value.grid_forget()
    u_value = Label(frame_u, text="%.2f" % hasil.array_utilitas[step], bd=1, relief=SUNKEN, width=7)
    u_value.grid(row=0, column=1, padx=10)

    button_next = Button(frame_run, text=">>", width=4, command=lambda: next(i + 1))
    button_previous = Button(frame_run, text="<<", width=4, command=lambda: previous(i - 1))
    dataKe = Label(frame_run, text="data ke - " + str(step), width=15)
    dataKe.grid(row=2, column=1)

    if (step == 1):
        button_previous = Button(frame_run, text="<<", width=4, state=DISABLED)
    button_previous.grid(row=1, column=0, pady=5, padx=5)
    button_next.grid(row=1, column=2, pady=5, padx=5)

def clear():
    global stack_timeArrival, stack_arrival, next_arr
    global step, event_value, button_next, button_previous
    if input_banyakData.get() == '' or input_lamaPelayanan.get() == '' or input_banyakData.get() == '':
        Label(frame_run, text="Masukkan Input..", width=15).grid(row=0, column=1)
    else:
        Label(frame_run, text="Data dibersihkan!", width=15).grid(row=0, column=1)
        step = 0
        hasil.hapusData()

        hasil.add_indeks_data(int(input_banyakData.get())*2)
        button_previous = Button(frame_run, text="<<", width=4, state=DISABLED)
        button_previous.grid(row=1, column=0, pady=5, padx=5)
        dataKe = Label(frame_run, text="data ke - " + str(step))
        dataKe.grid(row=2, column=1)

        #RESET
        event_value.pack_forget()
        event_value = Label(frame_event, text="0", bd=1, relief=SUNKEN)
        next_arr.grid_forget()
        next_arr = Label(frame_system, text="0", width=7, bd=1, relief=SUNKEN)
        stack_arrival.grid_forget()
        stack_arrival = LabelFrame(frame_system, borderwidth=0)
        next_next_arr = Label(stack_arrival, text="0", width=7, bd=1, relief=SUNKEN)
        # system state
        serverStatus_value = Label(frame_systemState, text="0", width=7, bd=1, relief=SUNKEN)
        number_in_queue_value = Label(frame_systemState, text="0", width=7, bd=1, relief=SUNKEN)
        stack_timeArrival.grid_forget()
        stack_timeArrival = LabelFrame(frame_systemState, borderwidth=0)
        timeArrival_value = Label(stack_timeArrival, text="0", bd=1, width=8, relief=SUNKEN)
        timeEvent_value = Label(frame_systemState, text="0", width=7, bd=1, relief=SUNKEN)
        # frame clock & arr_dep
        clock_value = Label(frame_clock, text="0", width=5, height=2, bd=2, relief=SUNKEN)
        nextArrival_value = Label(frame_clock, text="0", width=5, bd=1, relief=SUNKEN)
        nextDepart_value = Label(frame_clock, text="0", width=5, bd=1, relief=SUNKEN)
        # frame counter (bawah)
        numberDelayed_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
        totalDelay_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
        areaUnderQt_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)
        areaUnderBt_value = Label(frame_counter, text="0", width=7, height=2, bd=2, relief=SUNKEN)

        # system
        event_value.pack()
        next_arr.grid(row=1, column=0, padx=8, pady=8)
        stack_arrival.grid(row=2, column=0, sticky=W + E, padx=10, pady=5)
        next_next_arr.pack(pady=2)
        # system state
        serverStatus_value.grid(row=0, column=0)
        number_in_queue_value.grid(row=0, column=1)
        stack_timeArrival.grid(row=0, column=2)
        timeArrival_value.pack()
        timeEvent_value.grid(row=0, column=3)
        # frame clock
        clock_value.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        nextArrival_value.grid(row=0, column=2, padx=5, pady=5, sticky=E)
        nextDepart_value.grid(row=1, column=2, padx=5, pady=5, sticky=E)
        # frame counter
        numberDelayed_value.grid(row=0, column=0, pady=5)
        totalDelay_value.grid(row=0, column=1)
        areaUnderQt_value.grid(row=0, column=2)
        areaUnderBt_value.grid(row=0, column=3)

        # frame Statistical Counter
        dn_value = Label(frame_dn, text="   ", bd=1, relief=SUNKEN, width=7)
        qn_value = Label(frame_qn, text="   ", bd=1, relief=SUNKEN, width=7)
        u_value = Label(frame_u, text="   ", bd=1, relief=SUNKEN, width=7)

        # layout statistical counter
        dn_value.grid(row=0, column=1)
        qn_value.grid(row=0, column=1)
        u_value.grid(row=0, column=1)

def dnGraph():
    global step

    dn = []
    clock = []

    for i in range(step):
        dn.append(hasil.array_dn[i])
        clock.append(hasil.array_clock[i])
    plt.xlabel('Clock')
    plt.ylabel('Rata - rata lama antri')
    plt.plot(clock, dn)
    plt.show()

def qnGraph():
    global step

    qn = []
    clock = []
    for i in range(step):
        qn.append(hasil.array_qn[i])
        clock.append(hasil.array_clock[i])
    plt.xlabel('Clock')
    plt.ylabel('Rata - rata banyak orang dalam antrian')
    plt.plot(clock, qn)
    plt.show()

def uGraph():
    global step

    u = []
    clock = []
    for i in range(step):
        u.append(hasil.array_utilitas[i])
        clock.append(hasil.array_clock[i])
    plt.xlabel('Clock')
    plt.ylabel('Utilitas')
    plt.plot(clock, u)
    plt.show()

dn_graph = Button(frame_dn, text=" Tampilkan Grafik ")
# , command=dnGraph
dn_graph.grid(row=1, column=0, pady=10, columnspan=2)
qn_graph = Button(frame_qn, text=" Tampilkan Grafik ")
# , command=qnGraph
qn_graph.grid(row=1, column=0, pady=10, columnspan=2)
u_graph = Button(frame_u, text=" Tampilkan Grafik ")
# , command=uGraph
u_graph.grid(row=1, column=0, pady=10, columnspan=2)

# run, generate, clear button
frame_run = LabelFrame(main_frame, borderwidth=0)
button_run = Button(frame_run, text="Run", command=lambda: run(2), padx=20, width=10)
button_next = Button(frame_run, text=">>", command=lambda: next(2), width=4)
button_previous = Button(frame_run, text="<<", width=4, state=DISABLED)
dataKe = Label(frame_run, text="data ke - " + str(step))

frame_generate = LabelFrame(main_frame, borderwidth=0)
frame_generate.grid(row=1, column=0, sticky=N)
generate = Button(frame_generate, text="Generate", command=generate_command)
generate.pack(side=RIGHT, padx=5)
clear = Button(frame_generate, text="Clear", command=clear)
clear.pack(side=LEFT, padx=5)

# layout run
frame_run.grid(row=1, column=1, columnspan=3, ipady=5, sticky=N)
button_run.grid(row=1, column=1, pady=5, padx=5)
button_next.grid(row=1, column=2, pady=5, padx=5)
button_previous.grid(row=1, column=0, pady=5, padx=5)
dataKe.grid(row=2, column=1)

root.mainloop()
