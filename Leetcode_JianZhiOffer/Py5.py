class Solution:
    def replaceSpace(self, s: str) -> str:

        # return "%20".join(s.split())
        return s.replace(" ","%20")