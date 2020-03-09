import os, os.path

# # # # #
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

# # #
create_folder('advent')

for year in range(2015,2020):
    path = "advent/"+str(year)
    create_folder(path)
    for day in range(1,26):
        daypath = path + '/day' + str(day)
        create_folder(daypath)
        open (f'{daypath}/day{day}.py', 'a').close()
        open (f'{daypath}/day{day}.in', 'a').close()
        open (f'{daypath}/day{day}.test', 'a').close()




#


# # # # #
