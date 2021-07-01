import os

def find_files(suffix, path):
    output = []
    if os.path.exists(path):
        items_in_dir = os.listdir(path)
        if len(items_in_dir) == 0:
            print("Dir {} is empty".format(path))
            return None
        for item in items_in_dir:
            if os.path.isfile(path + "/" + item):
                if item.endswith(suffix):
                    output.append(item)
            else:
                output.extend(find_files(suffix,path + '/' + item))
        return output
    else:
        print("Path {} doesnt exists".format(path))
        return None


print(find_files(".c", "./testdir"))

#Test not exists
print(find_files(".c", "./other"))

#Test empty dir
print(find_files(".c", "./empty"))