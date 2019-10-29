def main():
    temp= input("Please input the average daily temperatures, separate with commas: ")
    temp=temp.split(",")

    cool=0
    heat=0

    for i in temp:
        if int(i) < 60 or int(i) > 80:
            if int(i) > 80:
                cool= cool + (int(i)-80)
            else:
                heat = heat + (60-int(i))

    print("Cooling degree days:",  cool)
    print("Heating degree days:", heat)

main()
