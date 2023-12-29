import csv

with open("firma.csv",encoding='utf-8') as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'NAZWA KOLUMNY: {", ".join(row)}')
            line_count += 1
        else:
            print(f"\t{row[0]} pracuje na stanowisku {row[1]} i ma urodziny w miesiącu: {row[2]}, "
                  f"otrzymuje nagrodę finansową w wysokości: {row[3]} zł")
            line_count += 1

    print(f'dodano {line_count} linii')
    print(f'dodano {line_count-1} osób')

print("________ zapis danych do pliku CSV __________")

with open("pracownik.csv","w",encoding="utf-8") as dc:
    prac_writer = csv.writer(dc,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONE,lineterminator='\n')

    prac_writer.writerow(('Karol Kot','Finanse','Luty',345))
    prac_writer.writerow(['Nadia Kot','Finanse','Marzec',453])
    prac_writer.writerow(['Olga Nowak','IT','Maj',567])
