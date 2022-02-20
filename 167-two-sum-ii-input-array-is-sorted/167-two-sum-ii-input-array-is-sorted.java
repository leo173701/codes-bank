class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length-1;
        while (left < right){
            int sumvalue = numbers[left]+numbers[right];
            if (sumvalue ==target){
                return new int[]{left+1, right+1};
            }
            else if(sumvalue < target){
                left++;}
            else{
                right--;}
        }
        return new int[]{-1,-1};
    }
}