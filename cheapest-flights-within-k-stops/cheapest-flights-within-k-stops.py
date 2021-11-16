class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src==dst:
            return 0
        graph = collections.defaultdict(list)
        for cur, to, price in flights:
            graph[cur].append((to,price))
        queue = deque([(-1,src,0)])  # (到当前结点的步数step，当前结点cur，到当前结点的累计价钱)
        
        
        # price = {src:0}  #从起点到当前结点的距离
        # price = collections.defaultdict(lambda: float('inf')) # 距离哈希表
        price = [float('inf') for _ in range(n)]
        price[src]=0
        
        
        while queue:
            step, cur, cum_price=queue.popleft()
            if step>=k:   #如果k==K， 已经走了k步了，不能再从这个结点出发走下一步了
                continue
            if cur == dst: #pos==dst:并不是到达终点就可以收工，可能还有更小的price 存在
                continue
            for nextnode, price_tonext in graph[cur]:#遍历当前结点能去的下一节点 
                temp = price_tonext+cum_price #如果从当前结点出发 到 下一节点 的总路程 temp
                if  price[nextnode] > temp :  #如果temp 比原有到下一节点的价钱更少， 
                    price[nextnode]= temp     #那就更新到下一节点的价钱
                    queue.append((step+1, nextnode, price[nextnode]))

        return price[dst] if price[dst]!=float('inf') else -1