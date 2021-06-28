import os

def find_files(suffix, path):
    output = []
    items_in_dir = os.listdir(path)
    for item in items_in_dir:
        if os.path.isfile(path + "/" + item):
            if item.endswith(suffix):
                output.append(item)
        else:
            output.extend(find_files(suffix,path + '/' + item))
    return output


print(find_files(".c", "./testdir"))