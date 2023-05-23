#include <iostream>
using namespace std;
bool funcion(int a[], int x, int min, int max, int &pos) {
    int mitad = (min + max) / 2;
    int valormedio = a[mitad];
    if (x == valormedio) {
        pos = mitad;
        return true;
    }
    if (x < valormedio) {
        max = mitad - 1;
        return funcion(a, x, min, max, pos);
    } else {
        min = mitad + 1;
        return funcion(a, x, min, max, pos);
    }
    return false;
}
int main() {
    int n;
    do {
        cout << "Ingrese el numero de elementos: ";
        cin >> n;
    } while (!(n > 0));
    cout << "Ingrese los numeros de forma ordenada (creciente)" << endl;
    int a[n], i;
    for (i = 0; i < n; i++) {
        cout << "#" << i + 1 << ": ";
        cin >> a[i];
    }
    int pos = -1, x;
    cout << "Ingrese el numero a buscar: ";
    cin >> x;
    if (funcion(a, x, 0, n - 1, pos)) {
        cout << x << " encontrado en la posicion " << pos
             << " del arreglo (empezando de pos=0)" << endl;
    } else {
        cout << "No se encontro " << x << ": posicion: " << pos << endl;
    }
    return 0;
}