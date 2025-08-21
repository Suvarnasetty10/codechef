 problem :Chef received N candies on his birthday. He wants to put these candies in some bags. A bag has K pockets and each pocket can hold at most M candies. 
   Find the minimum number of bags Chef needs so that he can put every candy into a bag.
code:
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here	for(t)
	int t,h;
    cin>>h;
    for(t=h;t>0;t--)
    {
        int n,k,m,y,o;
        cin>>n>>k>>m;
        o=k*m;
        
        y = ceil((double)n /o);
    
        cout<<y<<endl;
    }
}

