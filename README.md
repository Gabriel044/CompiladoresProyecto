Para proyecto final de esta materia crearemos un pequeño compilador, para un lenguaje con las siguientes funcionalidades:

Operaciones permitidas:
Aritméticas:
Suma +
Resta -
Multiplicación *
División /
Exponenciación ^
Comparación:
==
!= 
>
<
>=
<=
Booleanas
and 
or
Operaciones de bloques:
( )
{}
Un sistema de tipos:
Int
Float
Bolean
Operaciones permitidas entre el sistema de tipos:
int	float	boolean
int	Aritmeticas, comparacion	Aritmeticas, comparacion	
float	Aritmeticas, comparacion	Aritmeticas, comparacion	
boolean	----	----	and, or, ==, !=
Flujos de control existentes, deberan seguir una estructura similar al lenguaje C, por simplicidad todo deberán llevar llaves:
If , else, elif
while () {}
for (;;) {}
Para marcar el final de una sentencia se utilizara ";"
Es permitido el declarar y asignar una variable en la misma linea
La salida de este compilador debe de ser codigo de 3 direcciones.
