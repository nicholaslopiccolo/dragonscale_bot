from auth import params


def get_ids(array):
    ids = []
    for i in array:
        ids.append(array[i]['uid'])
    return ids


print(get_ids(params['admins']))
