class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int wr=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=val){
                nums[wr]=nums[i];
                wr++;
            }
        }return wr;
    }
};
