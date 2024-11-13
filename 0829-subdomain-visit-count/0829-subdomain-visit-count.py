class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count=defaultdict(int)
        domain_str=[]
        for str in cpdomains:
            visits,domain=str.split(" ")
            count=int(visits)
            domain_str=(domain.split("."))
            #domain_count[visits].append(domain.split("."))
            for i in range(len(domain_str)):
                subdomain=".".join(domain_str[i:])
                domain_count[subdomain]+=count

        print(domain_count)
        result=[]
        for domain,count in domain_count.items():
            result.append(f"{count} {domain}")


        return result