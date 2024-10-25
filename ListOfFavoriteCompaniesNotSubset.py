from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        company_to_person = dict()

        remaining_persons = set()
        for i in range(len(favoriteCompanies)):
            remaining_persons.add(i)
            favorites = favoriteCompanies[i]
            for company in favorites:
                if company in company_to_person.keys():
                    company_to_person[company].add(i)
                else:
                    company_to_person[company] = {i}

        output = []
        while remaining_persons:
            company_idx = remaining_persons.pop()
            company_lst = favoriteCompanies[company_idx]
            company1 = company_lst[0]
            superset = company_to_person[company1]
            for i in range(1, len(favoriteCompanies[company_idx])):
                superset = superset.intersection(company_to_person[company_lst[i]])
            if len(superset) == 1:
                output.append(company_idx)

        return output

if __name__ == '__main__':
    favoriteCompanies = [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]
    test = Solution()
    peopleIdxs = test.peopleIndexes(favoriteCompanies)
    print(peopleIdxs)



