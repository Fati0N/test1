
"""def read_file():
    total=0
    file1=open('numbers.txt','r')
    for line in file1:
        total+=int(line)
        print(total)
    return total
def mesatare(total):
    mesatare=total/4
    return mesatare

def main():
    total=read_file()
    print(f"Mesatarja e numrave eshte {mesatare(total)}")
main()"""

"""try:
    num=int(input("Vendos nje numer: "))
    def answer(num):
        total=0
        for x in range(1,num+1):
            total+=x
        print(f"Totali i numrit {num} te vendosur eshte {total}")

    def main():
        answer(num)

    main()
except ValueError:
    print("Ju lutem vendosni nje vlere numerike.")"""


"""def cal_factor():
    num = int(input("Vendos nje NR: "))
    for x in range(1,num+1):
        if x%num==0:
            print(x)


cal_factor()"""

"""fjala=str(input("Vendosni nje fjali: "))
fjala.split()
nr=4
for word in fjala:
    if len(word)>nr:
        print(word)"""



"""def get_num():
    numrat = [74, 2119, 1005, 200, -2, 673, 775, 124, -45, 383]
    numrat_vlefshem = []
    for x in numrat:
        if x>100 and x<1000:
            numrat_vlefshem.append(x)

    print(numrat_vlefshem)
    print(min(numrat_vlefshem))
    print(max(numrat_vlefshem))
get_num()"""

"""def info():
    file1=open('studenta.txt','w')
    studentat=4
    for x in range(studentat):
        emri=str(input("Vendos emrin e studentit."))
        n1=int(input("Vendos noten 1: "))
        n2=int(input("Vendos noten 2: "))
        n3=int(input("Vendos noten 3: "))
        student_info=emri,n1,n2,n3
        file1.write(str(student_info))"""

def read_file():
    try:
        file1=open('studenta.txt','r')
        for line in file1:
            data=line.split()
            emri=data[0]
            mbiemri = data[1]
            nota1 = int(data[2])
            nota2= int(data[3])
            nota3= int(data[4])
            total=int(nota1)+int(nota2)+int(nota3)
            mesatare=total/3
            print(f"Mesatarja per studentin {emri} {mbiemri} eshte {round(mesatare)}")
            print(emri,mbiemri)
    except FileNotFoundError:
        print("File nuk ekziston.")
    finally:
        print("Done")
        file1.close()



read_file()