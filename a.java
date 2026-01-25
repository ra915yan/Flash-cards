import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        
        //case no negative or positive numbers
        // x + y + z = 0 --> x + y = -z we need to have positive and negative numbers togather
        if(nums[0] >= 0 || nums[nums.length-1] <= 0){
            return list;
        }

        for (int i = 0; i < nums.length; i++) {
            //the rest are all negative numbers
            if(nums[i] < 0)
            

            int left  = i + 1;
            int right = nums.length - 1;
        }
    }
}