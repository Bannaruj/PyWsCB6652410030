import os
def data() :
    name_surname = input('ชื่อ-นามสกุล : ')
    mid = input('คะเเนนกลางภาค : ')
    final = input('คะเเนนปลายภาค : ')
    assignment = input('คะเเนนเก็บ : ')
    return name_surname, mid, final, assignment

def final_score (mid, final ,assignment):
    result = int(mid)+int(final)+int(assignment)
    return result
    

def create_file ():
    file = input('ให้ผู้ใช้ตั้งชื่อไฟล์เป็นชื่อวิชาเรียน : ')
    if not ".txt" in file :
        print('ไม่ใช่file.txt กรุณาป้อนใหม่')
    elif ".txt" in file :
        fileName = open(file,'w',encoding='utf-8')
        name_surname, mid, final, assignment = data()
        result = final_score(mid, final ,assignment)
        if result >= 50:
            fileName.write(f'กรุณากรอกชื่อ{name_surname}\nกรุณากรอกคะเเนนกลางภาค{mid}\nกรุณากรอกคะเเนนปลายภาค{final}\nกรุณากรอกคะเเนนคะเเนนเก็บ{assignment}\n{result}คุณผ่าน')
            fileName.close()
            print('สร้างไฟล์ใหม่และเพิ่มข้อมูลเรียบร้อยเเล้ว')
        else:
            fileName.write(f'กรุณากรอกชื่อ{name_surname}\nกรุณากรอกคะเเนนกลางภาค{mid}\nกรุณากรอกคะเเนนปลายภาค{final}\nกรุณากรอกคะเเนนคะเเนนเก็บ{assignment}\n{result}คุณไม่ผ่าน')
            fileName.close()
            print('สร้างไฟล์ใหม่และเพิ่มข้อมูลเรียบร้อยเเล้ว')

def searchFile():
    fileExplorer = os.listdir()
    if not fileExplorer:
        print('ไม่มีไฟล์ใดๆ')
    else:
        for showFile in fileExplorer:
            if showFile.endswith(".txt"):
                print(showFile)
        print('เลือกวิชาเเละเพิ่มข้อมูลต่อท้ายไฟล์')
        selectFile = input('เลือกไฟล์')
        if selectFile not in fileExplorer:
            print('พิมพ์ชื่อไฟล์ไม่ถูกหรือไม่มี.txt')
        else:
            fileName = open(selectFile,'a',encoding='utf-8')
            name_surname, mid, final, assignment = data()
            result = final_score(mid, final ,assignment)
            if result >= 50:
                fileName.write(f'กรุณากรอกชื่อ{name_surname}\nกรุณากรอกคะเเนนกลางภาค{mid}\nกรุณากรอกคะเเนนปลายภาค{final}\nกรุณากรอกคะเเนนคะเเนนเก็บ{assignment}\n{result}คุณผ่าน')
                fileName.close()
                print('เพิ่มข้อมูลต่อเรียบร้อย')
            else:
                fileName.write(f'กรุณากรอกชื่อ{name_surname}\nกรุณากรอกคะเเนนกลางภาค{mid}\nกรุณากรอกคะเเนนปลายภาค{final}\nกรุณากรอกคะเเนนคะเเนนเก็บ{assignment}\n{result}คุณไม่ผ่าน')
                fileName.close()
                print('เพิ่มข้อมูลต่อเรียบร้อย')
def readFile() :
    fileExplorer = os.listdir()
    if not fileExplorer:
        print('ไม่มีไฟล์ใดๆ')
    else:
        for showFile in fileExplorer:
            if showFile.endswith(".txt"):
                print(showFile)
        selectFile = input('เลือกไฟล์')
        if selectFile not in fileExplorer:
            print('พิมพ์ชื่อไฟล์ไม่ถูก')
        else: 
            data = open(selectFile,'r',encoding="utf-8")
            Read = data.read()
            print(Read)

def delete_file():
    fileExplorer = os.listdir()
    if not fileExplorer:
        print('ไม่มีไฟล์ใดๆ')
    else:
        for showFile in fileExplorer:
            if showFile.endswith(".txt"):
                print(showFile)
        selectFile = input('เลือกไฟล์')
        if selectFile not in fileExplorer:
            print('พิมพ์ชื่อไฟล์ไม่ถูก')
        elif selectFile in fileExplorer:
            os.remove(selectFile)
            print('ลบไฟล์เรียบร้อย')

def menu() :
    while True:
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 
        print('1.สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล 2.เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ 3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล 4.เลือกวิชาและลบไฟล์ 0.จบการทํางาน')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 
        try:
            Choice = input('กรุณาเลือก : ')
            if Choice == '1':
                create_file ()
                break
            elif Choice == '2':
                searchFile() 
                break
            elif Choice == '3':
                readFile()
                break
            elif Choice == '4':
                delete_file()
                break
            elif Choice == '0':
                print('ลาก่อน')
                break
            else:
                print('กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0เท่านั้น')
                break
        except Exception:
           print('กรุณากรอกข้อมูลให้ถูกต้อง') 
menu()