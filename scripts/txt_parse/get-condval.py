##!/c/"Program Files (x86)"/"Microsoft Visual Studio"/Shared/Python36_64/python


#import xlsxwriter,xlrd
import sys,os.path
import struct


#New sensor's log
#log_file = "log-hero-0702.log"
#calibration value=3050
#head=24450
#tail=27045

#calibration value=2080
#head=27974
#tail=30749

#calibration value=5450
#head=31764
#tail=34850


#Old sensor's log
#log_file = "log-hero-0702-02.log"
#calibration value=2080
#head=80
#tail=3140

#calibration value=3050
#head=4616
#tail=7150

#calibration value=5450
#head=8648
#tail=11205

#New sensor's log
log_file = "log-hero-0703.log"
#calibration value=3050
#head=17244
#tail=20005

#calibration value=2080
head=21276
tail=24049

#calibration value=5450
#head=9393
#tail=12782



def reverse_raw(val):
    v = val
    l = []
    for i in range(int(len(v)/2)):
        #print(v[2*i]+v[2*i+1])
        l.append(v[2*i]+v[2*i+1])
    l.reverse()
    
    rvs = "".join(l)
    #print(l)
    print(rvs)


def hex2float(val):
    f_val = struct.unpack('<f', bytes.fromhex(val))[0]
    print(f_val)
    return f_val



def get_condval(log_path, head, tail):
    vals=[]
    f_vals=[]
    with open(log_path, "r") as f:
        for line in f.readlines()[head : tail]:
            if line.find("we are here 4 ;	Rcved reg Value")==0:
                #print(line)
                line = line.strip('\r\n')
                tmp_val = line.strip()[-8:]
                vals.append(tmp_val)
            
    for v in vals:
        #print(v)
        #reverse_raw(v)
        f = hex2float(v)
        f_vals.append(f)

    print(len(vals))
        


# fname = u'Conductivity-波动测试.xlsx'
# if not os.path.isfile(fname):
    # print 'Can not find the target document.'
    # sys.exit()

# exl = xlrd.open_workbook(fname)
# exl.sheet_names()
# table = exl.sheet_by_index(0)

# new_wksheet = exl.add_worksheet()
# new_wksheet.set_column(0,ncols,22)


if __name__ == '__main__':
    print('Runing as the main program')
    get_condval(log_file, head, tail)
else:
    print('package initialization')
