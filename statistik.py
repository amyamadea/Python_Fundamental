import math;

# angka = [1,2,3,2,5,2,7,2];
angka = [1,1,2,2,3,3,4];

total = 0;
myDictionary = {};
modus = [];

def getModus(myDictionary, modus):
    max = 0;
    
    for key, value in myDictionary.items():
        if (value>max):
            max = value;
    
    for key, value in myDictionary.items():
        if (value==max):
            modus.append(key);
    
    if (len(modus)==len(myDictionary)):
        modus = [];

    return modus;


def getMedian(angka):
    newAngka = angka.sort();
    # newAngka = angka.sort(reverse=True);
    
    if (len(newAngka) % 2 == 0):
        median = (newAngka[round(len(newAngka)/2)-1] + newAngka[round((len(newAngka)/2))])/2;
    else:
        median = newAngka[round((len(newAngka)/2))];

    return median;

for i in range(len(angka)):
    # set myDictionary untuk jml angka muncul
    cekDictionary = myDictionary.get(angka[i], "None");
    if (cekDictionary == "None"):
        myDictionary[angka[i]] = 1;
    else:
        myDictionary[angka[i]] += 1;

    # total untuk mencari mean
    total += angka[i];

mean = total/len(angka);

# getModus(myDictionary);
# getMedian(angka);
# print("Median " + str(getMedian(angka)));
# print("Mean: " + str(mean));
print(getModus(myDictionary, modus));

