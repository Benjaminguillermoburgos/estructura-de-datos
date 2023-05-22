// Crear una lista de enteros y caracteres
// donde solo se imprima los enteros
// Lista = ["A",2,0,"B",8,"C"]
void main(){
  List <dynamic> lista = ["A",2,0,"B",8,"C"];
  //.where() sirve para filtrar el tipo de elemento que se requiera
  // is sirve para indicar el tipo que es el elemento
  // en este caso "is num" quiere decir "es entero"
  lista.where((element) => element is num).forEach((Numero) {
    print(Numero);
  });

}