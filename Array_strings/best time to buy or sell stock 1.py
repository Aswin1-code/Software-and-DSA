class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP=9999999999999;   #set some max value. but anyway its going to be replaced by some value
        int maxP=0;
        for(int i=0;i<prices.size();i++){
            if(prices[i]<minP){
                minP=prices[i];
            }
            else{
                int prft=prices[i]-minP;
                if(prft>maxP){
                    maxP=prft;
                }
            }
        }
        return maxP;
    }
};
