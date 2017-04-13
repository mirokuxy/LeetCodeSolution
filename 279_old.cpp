int numSquares(int n) {
    int* DP = (int*) malloc(sizeof(int) * (n+1));
    for(int i=0;i<=n;i++) DP[i] = 0;
    for(int i=1;i<=n;i++){
        int j=1;
        while(j*j <=i){
            int rest = i - j*j;
            int val = DP[rest] + 1;
            if (DP[i] == 0 || DP[i] > val){
                DP[i] = val;
            }
            j += 1;
        }
    }
    int ans = DP[n];
    free(DP);
    return ans;
}