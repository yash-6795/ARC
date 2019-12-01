import sys
import json

def find_blob(input, i, j, visited_mask):
    w = 0
    h = 0
    for j_tmp in range(j, len(input[0])):
        if input[i][j_tmp] != 0:
            w = w+1
        else:
            break
    for i_tmp in range(i,len(input)):
        if input[i_tmp][j] != 0:
            h = h + 1
        else:
            break
    return j,i,w,h

def visit_masks(input,visited_mask,x,y,w,h):
    num = 0
    diff_color_list = []
    for i in range(h):
        for j in range(w):
            if input[y+i][x+j] not in diff_color_list:
                num = num + 1
                diff_color_list.append(input[y+i][x+j])
            visited_mask[y+i][x+j] = 1
    return num

def find_blobs(input):
    blobs = []
    visited_mask = [[0 for j_tmp in range(len(input[0]))] for i_tmp in range(len(input))]
    count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != 0 and visited_mask[i][j] == 0:
                x,y,w,h = find_blob(input,i,j,visited_mask)
                diff_num_of_color = visit_masks(input,visited_mask,x,y,w,h)
                blobs.append((x,y,w,h,diff_num_of_color))
                count = count +1
    return blobs

def solve(json_data):
    # Training data formet : list
    # Each item in training_data is a dict with input and output as keys
    training_data = json_data['train']
    testing_data = json_data['test']
    blobs = []
    for item in testing_data:
        input = item['input']
        output = item['output']
        blob = find_blobs(input)
        blobs.append((input,blob))
    # for item in testing_data:
    #     input = item['input']
    #     output = item['output']
    #     blob = find_blobs(input)
    #     blobs.append((input,blob))
    # print(blobs)
    # Now we have blobs for each input grid with num of color for each blob
    results = []
    for input, blob in blobs:
        output = input.copy()
        for item in blob:
            x, y, w, h, n = item
            for i in range(n):
                for j in range(w):
                    output[y+h+i][x+j] = 1
            results.append({'input':input, 'output':output})

    for result in results:
        first_output = result['output']
        for i in range(len(first_output)):
            print(first_output[i])
        print("")
    return 0, json_data

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
