import heapq

def solution(h, w, bricks):
    runs = {0: [w, 0, None, None]}
    heap = [(0, 0)]

    for i in range(len(bricks)):
        hb, wb = bricks[i]
        while True:
            if not heap:
                return i + 1
            m, y = heapq.heappop(heap)
            node = runs.get(y)
            if node is not None and node[1] == m:
                break

        end, height, prev_s, next_s = node
        del runs[y]
        L = end - y
        if m + hb > h or L < wb:
            return i + 1

        newh = m + hb
        cons_end = y + wb
        has_leftover = cons_end < end
        final_start, final_end = y, cons_end
        final_prev, final_next = prev_s, next_s

        if not has_leftover and next_s is not None:
            nxt = runs.get(next_s)
            if nxt is not None and nxt[1] == newh:
                del runs[next_s]
                final_end = nxt[0]
                final_next = nxt[3]

        if prev_s is not None:
            prv = runs.get(prev_s)
            if prv is not None and prv[1] == newh:
                del runs[prev_s]
                final_start = prev_s
                final_prev = prv[2]

        if has_leftover:
            runs[cons_end] = [end, m, final_start, next_s]
            if next_s is not None:
                runs[next_s][2] = cons_end
            heapq.heappush(heap, (m, cons_end))
            final_next = cons_end

        runs[final_start] = [final_end, newh, final_prev, final_next]
        if final_prev is not None:
            runs[final_prev][3] = final_start
        if final_next is not None:
            runs[final_next][2] = final_start
        heapq.heappush(heap, (newh, final_start))

    return 0