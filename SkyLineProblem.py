from typing import List
import heapq as pq


class Solution:

    def shuffle_by_first(self, list1, *other_lists):

        idx = sorted(range(len(list1)), key=lambda k: list1[k])
        shuffled_list1 = list1[idx]
        shuffled_other_lists = [lst[idx] for lst in other_lists]
        result = [shuffled_list1] + shuffled_other_lists
        return result

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # order indexes according to start, end. lst = [[2, 0, "start"], [3, 1, "start"], ..., [2, 9, "end"], ...]

        if len(buildings) <= 1:
            # do stuff preemptively
            pass

        x_vals = []
        idxs = []
        start_end = []

        for i in range(len(buildings)):
            info = buildings[i]
            start = info[0]
            end = info[1]

            x_vals.append(start)
            idxs.append(i)
            start_end.append("start")

            x_vals.append(end)
            idxs.append(i)
            start_end.append("end")

        x_vals, idxs, start_end = self.shuffle_by_first(x_vals, idxs, start_end)

        fallback = []

        # {height: [true start, true end]}
        track_interval = dict()

        def heap_remove(val):
            fallback.remove(-val)
            pq.heapify(fallback)

        def heap_pop():
            return -pq.heappop(fallback)

        def heap_peek():
            return -fallback[0]

        def heap_push(val):
            pq.heappush(fallback, -val)

        def get_height(idx):
            return buildings[idx][2]

        def get_start(idx):
            return buildings[idx][0]

        def get_end(idx):
            return buildings[idx][1]

        ongoing = get_height(0)
        result = [[x_vals[0], ongoing]]

        for i in range(1, len(x_vals)):
            idx = idxs[i]
            start_end_val = start_end[idx]
            height = get_height(idx)

            current_end = track_interval[height][1]
            track_interval[height][1] = max(get_end(idx), current_end)

            if start_end_val == "end":
                end = get_end(idx)
                if track_interval[height][1] <= end:
                    if height == ongoing:
                        if len(fallback) != 0:
                            ongoing = heap_pop()
                        else:
                            ongoing = 0
                        result.append([get_start(idx), ongoing])
                    else:
                        heap_remove(height)
            else:
                if height > ongoing:
                    heap_push(ongoing)
                    ongoing = height
                    start = get_start(idx)
                    end = get_end(idx)
                    track_interval[ongoing] = [start, end]












