import os
import time
import datetime
import solver
import csv


def get_input_size(input_name):
    input_arr = solver.read_file('./Input/' + input_name)
    return str(len(input_arr))+'x'+str(len(input_arr[0]))


main_output_file = open('./Output/_Main_output.csv', 'a', newline='')
for filename in os.listdir('./Input/'):
    start_time = time.time()
    result = solver.control_main('./Input/' + filename)
    end_time = time.time()

    input_size = get_input_size(filename)
    # string_to_main = input_size + ' - ' + str(end_time-start_time)
    # print(string_to_main + ' ' + str(datetime.datetime.today()))
    # main_output_file.write(string_to_main + '\n')
    writer = csv.writer(main_output_file)
    writer.writerow([input_size, str(end_time-start_time)])
    with open("./Output/" + filename[:-4] + '(out).txt', 'w') as output_file:
        for vector in result:
            output_file.write(str(vector)+'\n')
