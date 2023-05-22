// Multiplicar dos listas de 5 elementos
// a: [4,3,2,2,1]
// b: [-3,2,8,0,1]
// La lista obtenida se concatena a una nueva lista de 5 elementos aleatorios
// de -1 al -5. Luego ordenarla de forma descendente
import 'dart:math';
void main() {
  List<int> lista_1 = [4, 3, 2, 2, 1];
  List<int> lista_2 = [-3, 2, 8, 0, 1];
  //Generar una lista random
  Random random = Random();
  List c = List.generate(5, (index) => -random.nextInt(5) - 1);
  print("La lista random es: ");
  print(c);
  //Consiguiendo la lista resultado
  List lista_mult = [];
  for (int i = 0; i < 5; i++){
    lista_mult.add(lista_1[i] * lista_2[i]);
    }
  List lista_conc = c + lista_mult;
  print ("La lista resultante entre a y b es: $lista_mult");
  print ("La lista concatenada es: ");
  print(lista_conc);
  (lista_conc).sort((a,b)=> b.compareTo(a));
  print("La lista ordenada descendentemente es:");
  print (lista_conc);

}
