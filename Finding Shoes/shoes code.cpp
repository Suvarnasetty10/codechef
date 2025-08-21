//code
#include <bits/stdc++.h>
using namespace std;
int main() {
	// your code goes here
	int t,h;
	cin>>h;
	for(t=h;t>0;t--)
	{
	    int n,m,c,e;
	    cin>>n>>m;
	    if(m==0)
	    {
	       cout<<n*2<<endl;
	    }
	    else if(n<m)
	    {
	        cout<<n<<endl;
	    }
	    else
	    {
	        c=n-m;
	        e=c+n;
	        cout<<e<<endl;
	    }
	}
}

