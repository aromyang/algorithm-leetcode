class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:       
        d = defaultdict(list)

        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            for i, matched_emails in enumerate(d[name]):
                if emails & matched_emails:
                    emails |= matched_emails
                    matched_emails.clear()
            d[name].append(emails)
        
        return [[k] + sorted(list(value)) for k, values in d.items() for value in values if value]