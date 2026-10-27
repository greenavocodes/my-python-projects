# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here

    # print (A)
    move_by = 0
    A_dict = {}
    if len(set(A)) == 1:
        print (A)
        return (A)
    else:
        if K == 0:
            # print (A)
            return (A)
        elif K == len(A):
            # print (A)
            return (A)
        else:
            # if K > len(A):
            #     move_by = K - len(A)
            #     print (f"needs to be shifted by {move_by} spaces")
            # else:
            #     move_by = len(A) - K
            # # for i in range(0, len(A)):
            #     print (f"needs to be shifted by {move_by} spaces")

            move_by = K % len(A)
            for idx, ch in enumerate(A):
                A_dict[idx] = ch
                print(A_dict)

            # print (f"Move by ---- {move_by}")
            # x=0
            # if move_by == 1:
            #     for x in range (0, len(A)):
            #         A_dict[len(A)+x]=A_dict[x]
            #         print (A_dict)
            #         # x += 1
            # else:
            for x in range(0, len(A)):
                A_dict[len(A) + x] = A_dict[x]
                print (A_dict)
                # x += 1

            new_list = []
            for i in range(0, len(A)):
                new_list.append(A_dict[len(A) + i - move_by])
                print(new_list)
            #return (new_list)
    pass

solution ([1,2,3,4,5],8)