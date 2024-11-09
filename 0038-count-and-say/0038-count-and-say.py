class Solution:
    def countAndSay(self, n: int) -> str:
        # f(n)은 f(n-1)의 인코딩
        # f(2) -> "1" -> "11" 1이 한번
        # f(3) -> "11" -> "21"
        # n번째 인코딩 스트링

        encodings = ["Null", "1", "11", "21", "1211"]
        if n < 5:
            return encodings[n]

        for i in range(5, n + 1):
            prev = encodings[i - 1]
            next = ""
            cur = prev[0]
            count = 1

            for j in range(1, len(prev)):
                if prev[j] == cur:
                    count += 1
                else:
                    next += str(count) + cur
                    count = 1
                    cur = prev[j]
                    
            next += str(count) + cur
            encodings.append(next)

        return encodings[n]