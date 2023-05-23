#include <iostream>
using namespace std;
struct nodo{
	int num;
	nodo *puntero;
};

nodo *lista;
void crear_nodo(nodo *&p, int num){
	p=new(nodo);
	p->num=num;
	p->puntero=NULL;
}
void crear_lista(nodo *&p){
	int i,n,num;
	nodo *q,*r;
	do{
		cout<<"Ingrese el número de datos:"; cin>>n;
	}while(n>50||n<=0);
	p=NULL; 
	for(i=1; i<=n; i++){
		cout<<"Dato"<<i<<endl;
		cout<<"Ingrese numero:"; cin>>num;
		if(p==NULL){
			crear_nodo(p,num);
			r=p;
		}
		else{
			crear_nodo(q,num);
			r->puntero=q;
			r=q;
		}
	}
}
void recorre(nodo *p){
	while(p!=NULL){
		cout<<p->num<<"\t"<<endl;
		p=p->puntero;
	}
}
void ordenar(nodo *p){
	nodo *q;
	int auxC;
	while(p!=NULL){
		q=p->puntero;
		while(q!=NULL){
			auxC=p->num; p->num=q->num; q->num=auxC;
			q=q->puntero;
		}
		p=p->puntero;
	}
}
int main(){
	crear_lista(lista);
	cout<<"Lista inicial"<<endl;
	recorre(lista);
	cout<<"Lista final"<<endl;
	ordenar(lista);
	recorre(lista);
}
