#include<iostream>
#include<conio.h>
using namespace std;
struct nodo{
            int nro;
            struct nodo *sgte;
           };
int main(){
	struct nodo h;
	struct nodo *q;
	int i, n;
	h.sgte=NULL;
	cout<<"Numero de elementos(<50):";
	cin>>n;
	for(i=0;i<n;i++){
		cout<<"Elemento:"<<(i+1)<<endl;
		q=new(struct nodo);
		cin>>q->nro;
		q->sgte=h.sgte;
		h.sgte=q;
  	}
	cout<<endl<<"Listado:"<<endl;
  	q=h.sgte;
  	while(q!=NULL){
  		cout<<q->nro<<endl;
  		q=q->sgte;
  	}
  getch();
  return 0;
}