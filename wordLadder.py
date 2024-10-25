from typing import List


def binarySearch(val: str, lst: List[str]) -> int:
    l = 0
    h = len(lst) - 1
    while l <= h:
        m = l + (h - l) // 2
        if lst[m] == val:
            return m
        elif lst[m] > val:
            h = m - 1
        else:
            l = m + 1
    return l


def forward_backward_insert(val: str, forward: List[str], backward: List[str]) -> tuple:
    forward_idx = binarySearch(val, forward)
    backward_idx = binarySearch(val[::-1], backward)

    return (forward_idx, backward_idx)


def areNeighbors(str1: str, str2: str) -> bool:
    differ_ct = 0
    for i, j in zip(str1, str2):
        if i != j:
            differ_ct += 1

    return differ_ct == 1


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        forward = sorted(wordList)
        backward = sorted([word[::-1] for word in wordList])
        fid, bid = forward_backward_insert(beginWord, forward, backward)
        for i in range(len(backward)):
            backward[i] = backward[i][::-1]
        if forward[fid] != beginWord:
            forward.insert(fid, beginWord)
            backward.insert(bid, beginWord)

        forward_dict = dict({forward[i]: i for i in range(len(forward))})
        backward_dict = dict({backward[i]: i for i in range(len(backward))})

        # forward idx, backward idx, path length
        q = [(fid, bid, 1)]
        visited = set()

        while q:

            fid, bid, min_length = q.pop(0)
            word = forward[fid]
            min_length += 1

            original_fid = fid
            original_bid = bid

            while fid > 0:
                # check if left neighbor is endWord. if so, return min_length
                leftfid = fid - 1
                left = forward[leftfid]

                if not areNeighbors(left, word):
                    break

                if left == endWord:
                    return min_length
                # check if left is neighbor and add to q if not visited. then add to visited
                if left not in visited:
                    leftbid = backward_dict[left]
                    q.append((leftfid, leftbid, min_length))
                    visited.add(left)

                fid -= 1

            fid = original_fid

            while fid < len(forward) - 1:
                # check if right neighbor is endWord. if so, return min_length
                rightfid = fid + 1
                right = forward[rightfid]

                if not areNeighbors(right, word):
                    break

                if right == endWord:
                    return min_length
                # check if right is neighbor and add to q if not visited. then add to visited
                if right not in visited:
                    rightbid = backward_dict[right]
                    q.append((rightfid, rightbid, min_length))
                    visited.add(right)

                fid += 1

            # same for bid

            while bid > 0:
                # check if left neighbor is endWord. if so, return min_length
                leftbid = bid - 1
                left = backward[leftbid]

                if not areNeighbors(left, word):
                    break

                if left == endWord:
                    return min_length
                # check if left is neighbor and add to q if not visited. then add to visited
                if left not in visited:
                    leftfid = forward_dict[left]
                    q.append((leftfid, leftbid, min_length))
                    visited.add(left)

                bid -= 1

            bid = original_bid

            while bid < len(backward) - 1:
                # check if right neighbor is endWord. if so, return min_length
                rightbid = bid + 1
                right = backward[rightbid]

                if not areNeighbors(right, word):
                    break

                if right == endWord:
                    return min_length
                # check if right is neighbor and add to q if not visited. then add to visited
                if right not in visited:
                    rightfid = forward_dict[right]
                    q.append((rightfid, rightbid, min_length))
                    visited.add(right)

                bid += 1

        # no such sequence exists
        return 0

if __name__ == '__main__':
    beginWord = "cat"
    endWord = "fin"

    wordList = wordList = ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]

    test = Solution()
    result = test.ladderLength(beginWord, endWord, wordList)
    print(result)