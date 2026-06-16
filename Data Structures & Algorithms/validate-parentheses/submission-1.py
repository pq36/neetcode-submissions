class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if st and ((st[-1]=='(' and i==')') or (st[-1]=='{' and i=='}') or (st[-1]=='[' and i==']')):
                st.pop()
            elif i in ['(','{','[']:
                st.append(i)
            else:
                return False
        return not st

        