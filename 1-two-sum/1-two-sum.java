class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> temp = new HashMap<Integer, Integer>();
        int [] res = new int[2];
        for (int i=0; i<nums.length;i++){
            if (temp.containsKey(target-nums[i])){
                res[0]=i;
                res[1]=temp.get(target-nums[i]);
            }
            else{
                temp.put(nums[i],i);
            }
        }
        return res;
        
    }
}