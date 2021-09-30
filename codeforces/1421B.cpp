int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
 
    ll t;
    cin>>t;
    while(t--)
    {
        vp.clear();
        ll n;
        cin>>n;
        for(int i=1; i<=n; i++)
        {
            string s;
            cin>>s;
            for(int j=1; j<=n; j++)
            {
                A[i][j]=(s[j-1]-'0');
            }
        }
        ll ur=A[1][2],ud=A[2][1],lu=A[n][n-1],lf=A[n-1][n];
        if(ur==ud)  // Case 1
        {
            if(ur==1)
            {
                if(lu==1)
                {
                    vp.push_back({n,n-1});
                }
                if(lf==1)
                {
                    vp.push_back({n-1,n});
                }
            }
            else
            {
                if(lu==0)
                {
                    vp.push_back({n,n-1});
                }
                if(lf==0)
                {
                    vp.push_back({n-1,n});
                }
            }
        }
        else  // Case 2
        {
            if(lf==lu)
            {
                if(lu==1)
                {
                    if(ur==1)
                    {
                        vp.push_back({1,2});
                    }
                    else
                        vp.push_back({2,1});
                }
                else
                {
                    if(ur==0)
                    {
                        vp.push_back({1,2});
                    }
                    else
                        vp.push_back({2,1});
                }
            }
            else
            {
                if(ur==0)
                {
                    vp.push_back({1,2});
                }
                if(ud==0)
                    vp.push_back({2,1});
                if(lf==0)
                    vp.push_back({n,n-1});
                if(lu==0)
                    vp.push_back({n-1,n});
            }
        }
        cout<<vp.size()<<endl;
        for(int i=0; i<vp.size(); i++)
        {
            cout<<vp[i].first<<" "<<vp[i].second<<endl;
        }
    }
    return 0;
}