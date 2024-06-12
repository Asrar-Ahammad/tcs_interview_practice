"""Write a python function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string """""""".
 
Example 1:
Input: strs = [""""flower"""",""""flow"""",""""flight""""]
Output: """"fl""""
"""

def common_prefix(strs):
    common_prefix = ""
    n = len(strs)
    strs_sorted = sorted(strs)
    first_ele = strs_sorted[0]
    last_ele = strs_sorted[-1]
    for i in range(min(len(first_ele),len(last_ele))):
        if(first_ele[i] != last_ele[i]):
            return common_prefix
        common_prefix+=first_ele[i]
    return common_prefix
    
inp_str = ["flower","flow","flight"]
print(common_prefix(inp_str))