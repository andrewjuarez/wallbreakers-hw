# https://leetcode.com/problems/subdomain-visit-count/description/
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = defaultdict(int)
        for domain in cpdomains:
            visit_count, domain = domain.split(" ")
            subdomains = domain.split(".")
            for num in range(len(subdomains)):
                visited_domain = ".".join(subdomains[num::])
                visits[visited_domain] += int(visit_count)
        
        
        
        return [str(count) + " " + str(domain) for domain, count in visits.items()]
            