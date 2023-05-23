#include <iostream>
#include <fstream>
using namespace std;
typedef char cadena[31];

struct Nodo{
	int edad;
	char* sexo;
	char* estado;
	char* distrito;
	Nodo *siguiente;
};

Nodo *p;

void crear_nodo(Nodo *&p, int edad, cadena sexo, cadena estado, cadena distrito){
	p=new(Nodo);
	p->edad=edad;
	p->sexo=sexo;
	p->estado=estado;
	p->distrito=distrito;
	p->siguiente=NULL;
}

void mostrar(Nodo *p){
	while(p!=NULL){
		cout<<p->edad<<" "<<p->sexo<<" "<<p->estado<<" "<<p->distrito<<" -> "<<endl;
		p=p->siguiente;
	}
}

int main(){
	int edad;
	cadena estado;
	cadena sexo;
	cadena distrito;
	ifstream ent;
	ent.open("COVID.TXT");
	if(!ent){
		cout<<" ERROR EN LA APERTURA ";
	}
    else{
    	while(ent){
    		if(ent>>edad>>sexo>>estado>>distrito){
    			cout<<edad<<"\t"<<sexo<<"\t"<<estado<<"\t"<<distrito<<endl;
    			Nodo *q;
    			if(p==NULL){
    				crear_nodo(p,edad,sexo,estado,distrito);
				}
				else{
					crear_nodo(q,edad,sexo,estado,distrito);
			        q->siguiente=p;
			        p=q;
				}
			}
		}
		ent.close();
	}
	mostrar(p);
	return 0;
	
}