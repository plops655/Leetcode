class Solution:

    def splitmerge(self, ranges, l, m, h):

    def order(self, ranges, l, h):
        pass

    def find_hoses(self, n, ranges):
        pass
        l = 0
        h = len(ranges) - 1

        self.order(ranges, l, h)

        # ranges is now ordered by start time with last end date breaking ties at start time

        hose_lst = []
        curr_interval = ranges[0]
        hose_lst.append(curr_interval)
        next_interval = ranges[0]

        for i in range(len(ranges)):
            curr_end = curr_interval[1]

            interval = ranges[i]
            int_start = i - interval[0]
            int_end = i + interval[1]

            next_end = next_interval[1]

            if int_start > curr_end:
                curr_interval = interval
            else:
                if min(int_end, n) > next_end:
                    next_interval = interval

        next_end = next_interval[1]
        if next_end < n:
            return -1


