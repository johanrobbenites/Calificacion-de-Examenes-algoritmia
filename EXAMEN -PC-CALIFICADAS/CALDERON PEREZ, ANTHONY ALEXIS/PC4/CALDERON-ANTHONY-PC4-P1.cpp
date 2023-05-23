# include<iostream>
# include<conio.h>
using namespace std;
struct nodo {
	int dato;
	nodo *sgte;
};
nodo *h; 
nodo *p, *q ; 

int main(){
	int n, num;
	h=new nodo;
	p=h;
	cout<<"Ingrese cantidad: ";cin>>n;
	cout<<"Ingrese dato: ";cin>>num;
	    p->dato=num;
	n= (n-1)/2;
	while(n!=0){
	    q=new nodo;
	    cout<<"Ingrese dato: ";
	    cin>>num;
	    q->dato=num;
	    p->sgte=q;
	    p=new nodo;
	    cout<<"Ingrese dato: ";cin>>num;
	    p->dato=num;
	    q->sgte=p;
	    n=n-1;
	}
	p->sgte=NULL;

    p=h;
    while (p!=NULL){
	    cout<< p->dato <<" -> ";
	    p=p->sgte;
    }
    p=h;

return 0;
}