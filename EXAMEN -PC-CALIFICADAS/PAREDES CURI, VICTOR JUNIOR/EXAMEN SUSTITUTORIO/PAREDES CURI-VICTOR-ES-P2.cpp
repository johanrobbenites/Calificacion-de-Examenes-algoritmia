#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

typedef char Cadena[31];

struct Nodo1{
	Cadena sexo;
	int edad;
	Nodo1 *punt1;
};

struct Nodo2{
	Cadena lugar;
	Nodo1 *punt1;
	Nodo2 *punt2;
};

void crear_Nodo1(Nodo1 *&p,Cadena sexo,int edad){
	if(p==NULL){
		p=new(Nodo1);
		strcpy(p->sexo,sexo);
		p->edad=edad;
		p->punt1=NULL;
	}
	else{
		crear_Nodo1(p->punt1,sexo,edad);
	}
}

void crear_Nodo2(Nodo2 *&p,Cadena lugar,Cadena sexo,int edad){
	if(p==NULL){
		p=new(Nodo2);
		strcpy(p->lugar,lugar);
		p->punt1=NULL;
		p->punt2=NULL;
		crear_Nodo1(p->punt1,sexo,edad);
	}
	else{
		if(strcmp(lugar,p->lugar)==0){
			crear_Nodo1(p->punt1,sexo,edad);
		}
		else{
			crear_Nodo2(p->punt2,lugar,sexo,edad);
		}
	}
}

void recorrer1(Nodo1 *p){
	if(p!=NULL){
		cout<<p->sexo<<"\t"<<p->edad<<endl;
		recorrer1(p->punt1);
	}
}

void recorrer2(Nodo2 *p){
	if(p!=NULL){
		cout<<p->lugar<<endl;
		recorrer1(p->punt1);
		recorrer2(p->punt2);
	}
}

int main(){
	Cadena lugar;
	Cadena sexo;
	int edad;
	Nodo2 *lista=NULL;
	ifstream ent;
	ent.open("COVID.TXT");
	if(!ent){
		cout<<"Error al abrir el texto COVID.TXT..."<<endl;
	}
	else{
		while(!ent.eof()){
			if(ent>>lugar>>edad>>sexo){
				crear_Nodo2(lista,lugar,sexo,edad);
			}
		}
		ent.close();
		recorrer2(lista);
	}
	return 0;
}
