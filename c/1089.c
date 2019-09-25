#include <stdio.h>

int main(){
    int n,v[3],result, p0, p1,i;

    while(1){
        scanf("%d", &n);

        result = 0;
        if(n == 0)break;
        
        scanf("%d", &v[0]);
        scanf("%d", &v[1]);


        if(n == 0)
            break;

        if(n == 2){
            if(v[0] != v[1])
                result = 2;
        }else {
            p0 = v[0];
            p1 = v[1];
            for(i = 2; i<n; i++){
                scanf("%d", &v[2]);

                if(((v[1] > v[0] && v[1] > v[2]) || (v[1] < v[0] && v[1] < v[2])))
                        ++result;
                v[0] = v[1];
                v[1] = v[2];
            }
            printf("%d %d %d %d", p0,p1,v[2],result);

            if ((p0 > p1 && p0 > v[2]) || (p0<p1 && p0<v[2])) 
                ++result;
            if ((v[2]>v[0] && v[2] > p0) || (v[2]<v[0] && v[2]<p0))
                ++result;
        }

        // printf("%d\n", result);
        
    }



    return 0;
}