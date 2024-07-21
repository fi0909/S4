import time
teks = dict(name = "luthfi", ig="@vxyzuc", youtube = "link")
global con
global dict_info
dict_info = []
for x in teks.keys():
    dict_info.append(x)
count = 0
con = True
index = 0
while True:
    if con is True:
        txt = teks[dict_info[count]]
        print(txt[:index], end=" ",flush=True)
        time.sleep(0.5)
        print(index)
        if index >= len(txt):
            print(con)
            con  = False
        index += 1
    else:
        print(index)
        print(txt[0:index], end=" ",flush=True)
        time.sleep(0.5)
        if index == 0:
            con = True
            index = 1
            count += 1
            if count > 2:
                count = 0
        index -= 1
print(len(teks))

'''
single text
if con is True:
            print(txt[:index], end=" ",flush=True)
            time.sleep(0.5)
            print(index)
            if index >= len(txt):
                print(con)
                con  = False
            index += 1
        else:
            print(index)
            print(txt[0:index], end=" ",flush=True)
            time.sleep(0.5)
            if index == 0:
                con = True
                index = 1
                dict_info = 2
            index -= 1
'''

'''
dictionary
if dict_info == 1:
        txt = teks["name"]
        if con is True:
            print(txt[:index], end=" ",flush=True)
            time.sleep(0.5)
            print(index)
            if index >= len(txt):
                print(con)
                con  = False
            index += 1
        else:
            print(index)
            print(txt[0:index], end=" ",flush=True)
            time.sleep(0.5)
            if index == 0:
                con = True
                index = 1
                dict_info = 2
            index -= 1
    elif dict_info == 2:
        txt = teks["ig"]
        if con is True:
            print(txt[:index], end=" ",flush=True)
            time.sleep(0.5)
            print(index)
            if index >= len(txt):
                print(con)
                con  = False
            index += 1
        else:
            print(index)
            print(txt[0:index], end=" ",flush=True)
            time.sleep(0.5)
            if index == 0:
                con = True
                index = 1
                dict_info = 3
            index -= 1
    elif dict_info == 3:
        txt = teks["youtube"]
        if con is True:
            print(txt[:index], end=" ",flush=True)
            time.sleep(0.5)
            print(index)
            if index >= len(teks):
                print(con)
                con  = False
            index += 1
        else:
            print(index)
            print(txt[0:index], end=" ",flush=True)
            time.sleep(0.5)
            if index == 0:
                con = True
                index = 1
                dict_info = 1
            index -= 1
'''