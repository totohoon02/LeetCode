class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        graph = [[] for _ in range(n + 1)]
        for time in times:
            start, end, cost = time
            graph[start].append([end, cost])
        distance = [INF] * (n + 1)

        print(graph) #

        import heapq
        q = []
        # 시작, 거리 == 0
        heapq.heappush(q, [k, 0])
        distance[k] = 0
        while q:
            node, dist = heapq.heappop(q)

            # 현재 거리가 작을 경우
            if distance[node] < dist:
                continue

            # 인접 노드 탐색
            for adj in graph[node]:
                new_node, dist = adj
                
                # sum of path
                dist += distance[node]
                
                # 기존 보다 작다면
                if dist < distance[new_node]:
                    distance[new_node] = dist
                    heapq.heappush(q, [new_node, dist])
        
        distance = distance[1:]
        
        if max(distance) == INF:
            return -1
        else:
            return max(distance)