import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

cal_list = [int(input()) for _ in range(N)]


class MaxHeap:
    def __init__(self):
        self.heap_arr = [None]

    def move_up(self, insert_idx):
        if insert_idx <= 1:
            return False
        parent_idx = insert_idx // 2
        if self.heap_arr[insert_idx] > self.heap_arr[parent_idx]:
            return True
        else:
            return False

    def insert(self, value):
        if len(self.heap_arr) < 1:
            self.heap_arr.append(None)
            self.heap_arr.append(value)
            return True

        self.heap_arr.append(value)
        insert_idx = len(self.heap_arr) - 1
        while self.move_up(insert_idx):
            parent_idx = insert_idx // 2
            self.heap_arr[parent_idx], self.heap_arr[insert_idx] = \
                self.heap_arr[insert_idx], self.heap_arr[parent_idx]
            insert_idx = parent_idx
        return True

    def move_down(self, idx):
        if len(self.heap_arr) > idx * 2:
            if len(self.heap_arr) > idx * 2 + 1:
                if self.heap_arr[idx] < max(self.heap_arr[idx * 2], self.heap_arr[idx * 2 + 1]):
                    return True
                else:
                    return False
            else:
                if self.heap_arr[idx] < self.heap_arr[idx * 2]:
                    return True
                else:
                    return False
        else:
            return False

    def pop(self):
        if len(self.heap_arr) <= 1:
            print(0)
            return True
        returned_data = self.heap_arr[1]
        self.heap_arr[1] = self.heap_arr[-1]
        self.heap_arr.pop()
        idx = 1
        while self.move_down(idx):
            if len(self.heap_arr) > idx * 2 + 1:
                if self.heap_arr[idx * 2] >= self.heap_arr[idx * 2 + 1]:
                    self.heap_arr[idx], self.heap_arr[idx * 2] = \
                        self.heap_arr[idx * 2], self.heap_arr[idx]
                    idx = idx * 2
                else:
                    self.heap_arr[idx], self.heap_arr[idx * 2 + 1] = \
                        self.heap_arr[idx * 2 + 1], self.heap_arr[idx]
                    idx = idx * 2 + 1
            else:
                self.heap_arr[idx], self.heap_arr[idx * 2] = \
                    self.heap_arr[idx * 2], self.heap_arr[idx]
                idx = idx * 2
        print(returned_data)
        return True


heap_ = MaxHeap()

for cal in cal_list:
    if cal == 0:
        heap_.pop()
    else:
        heap_.insert(cal)
