import sys

sys.setrecursionlimit(1000000)


def get_room(hotel_dict, i):
    # if hotel_dict.get(i) is None:
    #    return i
    # else:
    #    return get_room(hotel_dict, i + 1)
    #
    # while 1:
    #     if hotel_dict.get(i) is None:
    #         return i
    #     else:
    #         i += 1
    """
    순차 탐색은 최악의 경우에 200000 * 200001 / 2
    dict가 다음 가야 할 곳을 가리키게 만들면 됨
    재귀로 하면 나중에 그냥 엮인 곳들도 본인이 거쳤던 곳도 한번에 같은 곳을 가리키게 만들기 때문에 많은 시간이 절약된다.
    ex ) [1, 2, 3, 4, 5, 6, 1, 7] 1이 2 2가 3 이런식으로 엮여 있다 1이 한번 나오면 1부터 7까지 모두 8을 가르키게 됨
    """
    if i not in hotel_dict:
        hotel_dict[i] = i + 1
        return i
    j = get_room(hotel_dict, hotel_dict[i])
    hotel_dict[i] = j + 1
    return j


def solution(k, room_number):
    answer = []
    room = {}

    for i in room_number:
        get_room(room, i)
    return list(room)

    # for i in room_number:
    #     if room.get(i) is None:
    #         answer.append(i)
    #         room[i] = get_room(room, i)
    #     else:
    #         answer.append(room[i])
    #         room[room[i]] = get_room(room, room[i])
    # return answer
