'''Keywords'''
def list_average(num_list, avg_type = None)
    if num_list == []:
        return 0
    if avg_type == 'mean' or avg_type == None:
        return sum(num_list)/len(num_list)
    elif avg_type == 'mode':
        return max(num_list, key = num_list.count)
    elif avg_type == 'median':
        s = num_list.sort()
        n = len(num_list)
        return ((sum(s[n//2-1:n//2+1])/ 2.0, s[n//2])[n % 2])
        