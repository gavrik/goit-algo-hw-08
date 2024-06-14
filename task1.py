import heapq

def heap_sort(items):
    h = []
    for val in items:
        heapq.heappush(h, val)

    return h

if __name__ == "__main__":
    arr = [12,11,13,5,6,7]
    #arr = [4,7,9,6]
    h = heap_sort(arr)

    final_cost = 0

    while len(h) > 1:
        val1 = heapq.heappop(h)
        val2 = heapq.heappop(h)
        cost = val1 + val2
        print(val1, val2, "cost: ", cost)
        heapq.heappush(h, cost)
        final_cost += cost
   
    print('final length: ',final_cost)
