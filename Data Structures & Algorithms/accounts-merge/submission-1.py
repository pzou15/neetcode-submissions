class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_parents = dict() # email: parent
        email_to_acct = dict() # track which email belongs to which account
        email_rank = dict()

        def find_parent(email):
            if email != email_parents[email]:
                email_parents[email] = find_parent(email_parents[email])
            return email_parents[email]
        
        def union(email_1, email_2):
            p1 = find_parent(email_1)
            p2 = find_parent(email_2)

            if p1 == p2: return False

            if email_rank[p1] > email_rank[p2]:
                email_parents[p2] = p1
            elif email_rank[p1] < email_rank[p2]:
                email_parents[p1] = p2
            else:
                email_parents[p1] = p2
                email_rank[p2] += 1
            
        # init emails as individual nodes
        for acct in accounts:
            emails = acct[1:]
            email_parents.update({email: emails[0] for email in emails}) #initial adjacency list -> any emails that belong to other accounts will have a different parent
            email_rank.update({email: 0 for email in emails})
            email_to_acct.update({email: acct[0] for email in emails})

        # union parent emails if any emails in an account has a different parent
        for acct in accounts:
            acct_name = acct[0]
            for email in acct[1:]:
                parent = find_parent(email)
                if parent != acct[1]:
                    union(parent, acct[1])
            

        email_list = dict() # parent: email list
        for email in email_parents.keys():
            parent = find_parent(email)
            if parent in email_list:
                email_list[parent].append(email)
            else:
                email_list[parent] = [email]
            
        ret = []
        for email_key, emails in email_list.items():
            acc = email_to_acct[email_key]
            val = [acc]
            emails.sort()
            val.extend(emails)
            ret.append(val)




        return ret

                

                
