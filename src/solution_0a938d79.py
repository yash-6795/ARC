import sys
import json

def get_problem_type(input):
    tmp_tuple = (first_row, last_row, first_col, last_col) = input[0], input[len(input)-1], [x[0] for x in input], [x[len(x)-1] for x in input]
    for index, item in enumerate(tmp_tuple):
        if any(item):
            return index

def solve(json_data):
    # Training data formet : list
    # Each item in training_data is a dict with input and output as keys
    training_data = json_data['train']
    testing_data = json_data['test']
    blobs = []
    for item in training_data:
        input = item['input']
        output = item['output']
        # print('---------Input---------')
        # for i in range(len(input)):
        #     print(input[i])
        problem_type = get_problem_type(input)
        if problem_type == 0 or problem_type == 1:
            print('problem type is col : ' + str(problem_type))
            problem_type_col = True
        else:
            print('problem type is row one  : ' + str(problem_type))
            problem_type_col = False

        if problem_type_col:
            col_indexes = []
            tmp_tuple = (first_row, last_row) = input[0], input[len(input)-1]
            for item in tmp_tuple:
                for index, x in enumerate(item):
                    if x:
                        col_indexes.append((index,x))
            output_pred = input.copy()
            offset_value, first_index, second_index, first_value, second_value = calculate_offset(col_indexes)
            value = first_value
            for col in range(first_index,len(input[0]),offset_value ):
                for i in range(len(input)):
                    output_pred[i][col] = value
                value = second_value if value == first_value else first_value
            print('----------Output----------')
            for i in range(len(output_pred)):
                print(output_pred[i])
            print('----------------------------')
        else:
            row_indexes = []
            tmp_tuple = (first_col, last_col) = [x[0] for x in input ], [x[len(x)-1] for x in input]
            for item in tmp_tuple:
                for index, x in enumerate(item):
                    if x:
                        row_indexes.append((index,x))
            output_pred = input.copy()
            offset_value, first_index, second_index, first_value, second_value = calculate_offset(row_indexes)
            value = first_value
            for row in range(first_index,len(input),offset_value ):
                for i in range(len(input[0])):
                    output_pred[row][i] = value
                value = second_value if value == first_value else first_value
            for i in range(len(output_pred)):
                print(output_pred[i])
            print('--------------------')

    return 0, json_data


def calculate_offset(indexes):
    print(indexes)
    first_index, first_value = indexes[0]
    second_index, second_value = indexes[1]
    return second_index - first_index, first_index, second_index, first_value, second_value

def main():
    file_loc = './../data/training/'
    file_name = str(sys.argv[1])
    file_path = file_loc + file_name
    print(file_path)
    with open(file_path) as f:
        json_data = json.load(f)
    f.close()

    # Input should be data in json formet
    # It should return data in the same formet i.e. json
    return_code, result = solve(json_data)
    if return_code is not 0:
        print('Somethign went wrong in task 1')
    else:
        print('Solve returned with success')

if __name__ == "__main__":
    main()
