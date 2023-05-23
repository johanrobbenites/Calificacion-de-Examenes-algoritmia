#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

struct nodo;
{int dato;
nodo *ste;
};

nodo *h;
nodo *p, *q;

int main() {
	h = new nodo;
	int edad;
	char sexo, estado, distrito;
	FILE * archivo;
	archivo = open("COVID19.TXT","w");
	p = h;
	while True{
		cout << "Ingrese la edad de la persona: ";
		cin >> edad = p->dato;
		q = new nodo;
		cout << "Sexo de la persona M/F: ";
		cin >> sexo = q->dato;
		p = new nodo;
		cout << "Estado de la persona: ";
		cin >> estado = p->dato;
		q = new nodo;
		cout >> "Distrito de la persona: ";
		cin >> distrito = q->dato;
		linea >> str(edad) << " " << sexo << " " << estado << " " << distrito << "\n";
		p.write(linea);
		cout << "Desea ingresar mas datos (si/no): ";
		cin >> rpta;
		if rpta == "si"{
			continue;
		}
		if rpta == "no"{
			break;
		}
		archivo.close();
	return 0;
}
