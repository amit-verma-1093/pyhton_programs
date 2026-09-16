# import textwrap

# def merge_the_tools(string, k):
#     result = textwrap.wrap(string,k)
#     for i in result:
#         val=set(i)
#     print(val)
# string="AABCAAADA"
# k=3
# merge_the_tools(string, k)  
string="AABCAAADA"
lst=[string[i:i+3] for i in range(0,len(string),3)]
for i in lst:
    print( "".join(dict.fromkeys(i)))