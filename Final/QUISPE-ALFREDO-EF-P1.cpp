#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;
typedef char Cadena[10];
struct NodoC{
	int nota;
	NodoC *puntC;
};
struct NodoA{
	char curso;
	NodoC *puntC;
	NodoA *puntA;
};
void Crea_NodoC(NodoC *&p, int nota){
	if(p==NULL){
		p=new(NodoC);
		p->nota=nota;
		p->puntC=NULL;
	}
	else{
		Crea_NodoC(p->puntC, nota);
	}
}
void Crea_NodoA(NodoA *&p, char curso, int nota){
	if(p==NULL){
		p=new(NodoA);
		p->curso=curso;
		p->puntA=NULL;
		p->puntC=NULL;
		Crea_NodoC(p->puntC, nota);
	}
	else{
		if(p->curso==curso){
			Crea_NodoC(p->puntC, nota);
		}
		else{
			Crea_NodoA(p->puntA, curso, nota);
		}
	}
}

void RecorreC(NodoC *p){
	if(p!=NULL){
		cout<<p->nota<<endl;
		RecorreC(p->puntC);
	}
}

void RecorreA(NodoA *p){
	if(p!=NULL){
		cout<<p->curso<<endl;
		RecorreC(p->puntC);
		RecorreA(p->puntA);
	}
}
NodoA *Lista;
int main(){
	ifstream ent;
	int i,j,n,aux;
	char curso;
	Cadena s1;
	Lista=NULL;
	ent.open("ALGORITMIA.TXT");
	if(!ent){
		cout<<"Error de apertura del archivo...";
	}
	else{
		
		while(!ent.eof()){
			if(ent>>s1){
				curso=s1[0];
				i=0;
				n=strlen(s1);
				while(i<n){
				if(((s1[i])!='0') and ((s1[i])!='1') and ((s1[i])!='2') and ((s1[i])!='3') and ((s1[i])!='4') and ((s1[i])!='5') and ((s1[i])!='6') and ((s1[i])!='7') and ((s1[i])!='8') and ((s1[i])!='9')){
				j=i;
				aux++;
			while(j<n){
				s1[j]=s1[j+1];
				j++;
			}
			n--;
		}
		else{
			i++;
		}
	}
				int nota=atoi(s1);
				Crea_NodoA(Lista, curso, nota);
			}
		}
		ent.close();
	}

	RecorreA(Lista);
	return 0;
}
