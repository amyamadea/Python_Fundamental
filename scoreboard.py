angka0 = [' --- ', '|   |', '|   |', '|   |', ' --- '];
angka1 = ['-', '|', '|', '|', '-'];
angka2 = [' ----', '    |', ' ----', '|    ', ' ----'];
angka3 = ['---- ', '    |', '---- ', '    |', '---- '];
angka4 = ['-   -', '|   |', ' ----', '    |', '    |'];
angka5 = ['---- ', '|    ', '---- ', '    |', '---- '];
angka6 = ['---- ', '|    ', '---- ', '|   |', '---- '];
angka7 = ['---- ', '    |', '    |', '    |', '    -'];
angka8 = [' --- ', '|   |', ' --- ', '|   |', ' --- '];
angka9 = [' --- ', '|   |', ' --- ', '    |', ' --- '];


keluar = False;
myList = [];
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9];

def showMainMenu():
    print("\n1. Isi list");
    print("2. Lihat List");
    print("3. Keluar");

def inputNumber():
    number = int(input("Masukkan angka (1-9): "));
    if (number<10):
        myList.append(number);
    else:
        print("Masukkan angka (1-9) dong!!");

def printNumber(n, i, text):
    if (myList[n]==1):
        text += angka1[i];
    elif (myList[n]==2):
        text += angka2[i];
    elif (myList[n]==3):
        text += angka3[i];
    elif (myList[n]==4):
        text += angka4[i];
    elif (myList[n]==5):
        text += angka5[i];
    elif (myList[n]==6):
        text += angka6[i];
    elif (myList[n]==7):
        text += angka7[i];
    elif (myList[n]==8):
        text += angka8[i];
    elif (myList[n]==9):
        text += angka9[i];
    elif (myList[n]==0):
        text += angka0[i];
    text += "  ";

    return text;

def showList():
    text = "";
    if (len(myList)>0):
        for i in range (0,5):
            for n in range(len(myList)):
                text = printNumber(n, i, text);
            text += "\n";
        print(text);
    else:
        print("List masih kosong.")

while (keluar==False):
    showMainMenu();
    menu = int(input("Pilih menu: "));

    if (menu==1):
        inputNumber();
    elif (menu==2):
        showList();
    elif (menu==3):
        keluar = True;
    

# print("|");
# print("|");
# print("|");
# print("|");
# print("|");


# print(" --- ");
# print("|   |");
# print("|   |");
# print("|   |");
# print("|   |");
# print(" --- ");


# print("----");
# print("    |");
# print("----");
# print("    |");
# print("----");

# print("|   |");
# print("|   |");
# print(" ----");
# print("    |");
# print("    |");


# print("----");
# print("|   ");
# print("----");
# print("    |");
# print("----");


# print("----");
# print("|    ");
# print("----");
# print("|   |");
# print("----");

# print("----");
# print("    |");
# print("    |");
# print("    |");
# print("    |");


# print(" ---");
# print("|   |");
# print(" ---");
# print("|   |");
# print(" ---");

# print(" ---");
# print("|   |");
# print(" ---");
# print("    |");
# print(" ---");
