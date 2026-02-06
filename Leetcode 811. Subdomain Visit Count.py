from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # temp = []
        # for domain in cpdomains:
        #     temp.append(domain.split())
        # domains_store = defaultdict(int)
        # # print(temp)
        # for domains in temp:
        #     for i in range(len(domains) - 1, 0, -1):
        #         dom = []
        #         for j in range(len(domains[i]) - 1, -1, -1):
        #             if domains[i][j] == ".":
        #                 domains_store["".join(reversed(dom))] += int(domains[0])
        #             dom.append(domains[i][j])
        # print(domains_store)
        # return 0
        temp = []
        for domain in cpdomains:
            temp.append(domain.split())

        domains_store = defaultdict(int)

        for domains in temp:
            count = int(domains[0])
            full_domain = domains[1]

            parts = full_domain.split(".")
            for i in range(len(parts)):
                dom = ".".join(parts[i:])
                domains_store[dom] += count

        return [f"{domains_store[dom]} {dom}" for dom in domains_store]

