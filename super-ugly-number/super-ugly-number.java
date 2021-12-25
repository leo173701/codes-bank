class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int m = primes.length;
        PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->a[0]-b[0]); 
        for (int i = 0; i < m; i++) {
            q.add(new int[]{primes[i], i, 0});
        }
        int[] ans = new int[n];
        ans[0] = 1;
        for (int j = 1; j < n; ) {
            int[] poll = q.poll();
            int val = poll[0], i = poll[1], idx = poll[2];
            if (val != ans[j - 1]) ans[j++] = val;
            q.add(new int[]{ans[idx + 1] * primes[i], i, idx + 1});
        }
        return ans[n - 1];
    }
}
