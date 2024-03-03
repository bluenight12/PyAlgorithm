def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    del_id = []
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in ('-', '_', '.'):
            del_id.append(i)
    del_id = ''.join(del_id)
    old_len = len(del_id)
    while '..' in del_id:
        del_id = del_id.replace('..', '.')
    """
    글자를 찾을 때는 in을 활용하자
    del_id = del_id.replace('..', '.')
    while old_len != len(del_id):
        old_len = len(del_id)
        del_id = del_id.replace('..', '.')
    """
    del_id = del_id.strip('.')
    """
    . 처리를 제대로 못했기 때문에 while을 썼어야 통과 된 것
    while len(del_id) != 0 and del_id[0] == '.':
        del_id = del_id[1:]
    while len(del_id) != 0 and del_id[-1] == '.':
        del_id = del_id[:-1]
    """
    if del_id == '':
        del_id += 'a'
    if len(del_id) >= 16:
        del_id = del_id[:15]
    if del_id[-1] == '.':
        del_id = del_id[:-1]
    while len(del_id) <= 2:
        del_id += del_id[-1]

    answer = del_id

    return answer

print(solution("..........................-.............................................._......................................................."))