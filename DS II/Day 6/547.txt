class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if isConnected[i][j] == 1:
                        adj_list[i].append(j)
        
        def bfs(node):
            queue = collections.deque()
            queue.append(node)
            visited.add(node)
            while queue:
                curr_node = queue.popleft()
                for neighbor in adj_list[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        visited = set()
        provinces = 0
        for idx in range(n):
            if idx not in visited:
                bfs(idx)
                provinces += 1
        return provinces
#TC: O(n^2)
#SC: O(n)