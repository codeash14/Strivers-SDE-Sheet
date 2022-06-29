def maximumMeetings(start, end):
    # Write your Code here.
    n=len(start)
    meet=[[start[i],end[i],i+1] for i in range(n)]
    meet.sort(key=lambda x:x[1])
    ans=[meet[0][2]]
    limit=meet[0][1]
    for i in range(1,n):
        if meet[i][0]>limit:
            ans.append(meet[i][2])
            limit=meet[i][1]
    return ans