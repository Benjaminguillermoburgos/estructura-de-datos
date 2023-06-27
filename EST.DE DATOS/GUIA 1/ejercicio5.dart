// Obtener el promedio de 3 listas con 7 elementos
// Los elementos se generan de forma aleatoria (de 30 a 100)
import 'dart:math';
void main() {
  Random random = Random();
  List lista_1 = List.generate(7, (index) => random.nextInt(70)+30);
  List lista_2 = List.generate(7, (index) => random.nextInt(70)+30);
  List lista_3 = List.generate(7, (index) => random.nextInt(70)+30);

  print("La lista 1 es: $lista_1");
  print("La lista 2 es: $lista_2");
  print("La lista 3 es: $lista_3");

  int suma_1 = lista_1.reduce((a,b) => a + b);
  double promedio_1 = suma_1 / 7;
  String Pr_1 = promedio_1.toStringAsFixed(3);

  int suma_2 = lista_2.reduce((a,b) => a + b);
  double promedio_2 = suma_2 / 7;
  String Pr_2 = promedio_2.toStringAsFixed(3);

  int suma_3= lista_3.reduce((a,b) => a + b);
  double promedio_3 = suma_3 /7;
  String Pr_3 = promedio_3.toStringAsFixed(3);

  List Promedios = [Pr_1,Pr_2,Pr_3];
  print("La lista con los promedios es: $Promedios");


}