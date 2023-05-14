# ARQ
Voy a poner todo aquí en carpetas distintas porque... esto de estar haciendo keys no está tan divertido.

-----------------------------------------------------------------------------------------
## ARQ Tarea Extra - Taxi Rides

SOLID en el código:

### main.py
  - S: El trabajo de 'main' es único: llamar a los procesos de creación de reportes.
  - O: 'main' permite que se agreguen nuevos tipos de reportes sin modificar el código.
  - L: No relevante.
  - I: No relevante.
  - D: La función 'main' depende de la abstracción de 'RepCreator' más que de las implementaciones de los objetos. Esto permite que el código sea más flexible.  
  
### csv_util.py
  - S: La función 'parse_file' tiene una sola responsabilidad: leer y parsear datos y convertirlos en Rides.
  - O: La clase 'Ride' no se necesita modificar aunque se añadan funcionalidades. La función 'parse_file' se puede extender para leer de otros tipos con la misma lógica.
  - L: No relevante.
  - I: No relevante.
  - D: No relevante.
  
### factory.py
  - S: Tanto 'parse_file' como 'generate' y 'parse' tienen una sola responsabilidad.
  - O: 'RepCreator' se puede expandir sin modificar el código existente por el patrón Factory Method.
  - L: No relevante.
  - I: No hay interfaces como tal, pero los métodos 'generate' y 'parse' se pueden considerar interfaces mínimas que distintos tipos de reporte necesitan implementar sin caer en métodos innecesarios.
  - D: Solo depende de la interfaz abstracta provista por los métodos 'generate' y 'parse'.  
  
### report.py
  - S: El único método no abstracto tiene la única función de inicializar la clase.
  - O: No relevante.
  - L: 'Report' define el esquema que todas las subclases deben seguir, y cada subclase puede ser usada en vez de su superclase sin cambiar el comportamiento del programa.
  - I: La clase define una interfaz abstracta con cinco métodos igualmente abstractos; cada uno de ellos siendo necesario. Ningun método es forzado a ser aplicado sin ser necesario.
  - D: No relevante.
  
### web_report.py
  - S: Cada función heredada o creada tiene un solo propósito, y la clase como tal también.
  - O: El abstract factory de donde viene 'WebReport' está abierta a extensión, por lo que, siendo una subclase, 'WebReport' también.
  - L: Mismo caso de la superclase.
  - I: Mismo caso de la superclase.
  - D: 'WebReport' no fuerza a la factory 'RepCreator' a depender de sus detalles de implementación; solo de su constructor. También, 'WebReport' depende de 'Report' pero no de sus implementaciones.  
  
### print_report.py
  - S: La única razón por la que pudiera cambiar es en la forma en la que se presentan los datos en el TXT.
  - O: El abstract factory de donde viene 'TextReport' está abierta a extensión, por lo que, siendo una subclase, 'TextReport' también.
  - L: Mismo caso de la superclase.
  - I: Mismo caso de la superclase.
  - D: 'TextReport' no fuerza a la factory 'RepCreator' a depender de sus detalles de implementación; solo de su constructor. También, 'textReport' depende de 'Report' pero no de sus implementaciones.  
 
-----------------------------------------------------------------------------------------
## ARQ Tarea 4 - SOLID (Completa)

¿Cómo aplica SOLID al código?

Single Response Principle:
El código estaba completo en el main cuando se podía dividir en varias funciones, cada una con una responsabilidad única. Ya, con el nuevo formato, queda cada cosa con una sola responsabilidad.

Open-Closed Principle:
Realmente no vi cómo el código original no cumplía con este. Pero, por si acaso, cambié el formato para hacerlo extensible si es que se fuera a modificar después con classes (por eso el segundo push).

Liskov Substitution Principle:
Pues... no hay herencias o polimorfismos...

Interface Segregation Principle:
...ni interfaces.

Dependency Inversion Principle:
El código no tiene dependencias obligatorias. Usa CSV pero realmente puede usar cualquier otro formato sin problemas. Aparte, tampoco depende, por ejemplo, de "requests" como tal. Se puede usar cualquier otra librería.

-----------------------------------------------------------------------------------------
## ARQ Tarea 3 - Starwars (Completa)

Tuve que correr la imagen como
docker run -p 3000:3000 [image code]

-----------------------------------------------------------------------------------------
## ARQ Tarea 2 (Completa)

No sé qué tanto debo describir cómo se usa, pero esto es lo que hice.

Corrí un container con Flask (con el Dockerfile en el proyecto)
La app corre en el puerto 7700

(Espero le guste el diseño)

-----------------------------------------------------------------------------------------
