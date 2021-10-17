def register_news(titles, dates, file_path):
    with open(file_path, "w") as csv_file:
        for title, date in zip(titles, dates):
            csv_file.write(title)
            csv_file.write("|")
            csv_file.write(date)   
            csv_file.write("\n")
    return


 #retraite les données   