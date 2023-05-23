#include<iostream>
using namespace std;
struct Nodo{
	int num;
	Nodo *punt;	
};
void crear_nodo(Nodo *&p,int num){
	if(p==NULL){
		p=new(Nodo);
		p->num=num;
		p->punt=NULL;
	}
	else{
		if(num!=p->num){
			crear_nodo(p->punt,num);			
		}
	}
}
void ingresar_datos(Nodo *&p){
	p=NULL; 
	int n,num;
	do{
		cout<<"Ingresar el # de numeros: ";cin>>n;
	}while(!(0<n && n<=50));
	for(int i=0;i<n;i++){
		do{
			cout<<"Numero #"<<i+1<<": ";cin>>num;
		}while(!(0<=num && num<=99));
		crear_nodo(p,num);
	}
}
void imprimir_lista(Nodo *p){
	if(p!=NULL){
		cout<<p->num<<"\t";
		imprimir_lista(p->punt);
	}
	else{
		cout<<endl;
	}
}
void crear_pila(Nodo *&p,int num){
	if(p==NULL){
		p=new(Nodo);
		p->num=num;
		p->punt=NULL;
	}
	else{
		Nodo *nuevo;
		nuevo=new(Nodo);
		nuevo->num=num;
		nuevo->punt=p;
		p=nuevo;
	}
}
void invertir_lista(Nodo *&p){
	Nodo *inversa,*act=p;
	inversa=NULL;
	while(act!=NULL){
		crear_pila(inversa,act->num);
		p=act->punt;
		delete(act);
		act=p;
	}
	p=inversa;
}
int main(){
	Nodo *lista;
	ingresar_datos(lista);
	cout<<"\n--Lista normal--\n";
	imprimir_lista(lista);
	invertir_lista(lista);
	cout<<"\n--Lista inversa--\n";
	imprimir_lista(lista);	
	return 0;
}
