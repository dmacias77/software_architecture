# ARQ
Voy a poner todo aquí en carpetas distintas porque... esto de estar haciendo keys no está tan divertido.

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
