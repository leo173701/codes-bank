class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int[][] g = new int[n][n];
        for (int[] f : flights) {
            g[f[0]][f[1]] = f[2];
        }

        // (1) adding the distance array to track min distance to each node
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE / 2);

        //  PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        // (2) change heap to normal queue
        Queue<int[]> heap = new LinkedList<>();

        heap.offer(new int[]{0, src, K + 1});
        distance[src] = 0;

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int price = cur[0], place = cur[1], remainStops = cur[2];
            
          //  if (place == dst) return price;
            
            if (remainStops > 0) {
                for (int i = 0; i < n; i++) {
                    if (g[place][i] > 0 && distance[i] >= price + g[place][i]) {                        
                        heap.offer(new int[]{price + g[place][i], i, remainStops - 1});
                        distance[i] = price + g[place][i];
                    }
                }
            }
        }
        
        return distance[dst] == Integer.MAX_VALUE / 2 ? -1 : distance[dst];
    }
}