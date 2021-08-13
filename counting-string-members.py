# author : Sarvin Nami
name = input('please enter your name here : ').lower().replace(" ","")
checkList = []
for x in name :
    if x not in checkList :
        print(f"your name has {name.count(x)} {x}")
        checkList.append(x)
