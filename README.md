# Controlador de brazo robot

Proyecto realizado para la clase de Programación orientada a objetos de la carrera Mecatrónica en la Facultad de Ingeniería de la Universidad Nacional de Cuyo 

Integrantes del grupo

Antonella Aldao https://github.com/AntoAldao
Brenda Gudiño https://github.com/brendagudino12
Ignacio Berridy https://github.com/NachoBerridy

## Se pide

Desarrollar un aplicativo para controlar un robot de 3 grados de libertad con efector final.

![image](https://user-images.githubusercontent.com/63414974/140430692-6ddf9e39-fbc2-4717-ba32-bab7e1032af3.png)

* Tipo: robot 3DF.
* Configuración: RRR
* Efector final: simple (pinza, minitorno o pistola de pintura a elección).
* Dimensiones (extremas): anchura=A mm, profundidad=B mm, altura=C mm
* Velocidades máximas: lineal=VL mm/s, angular=VA rad/s
* El controlador recibe órdenes en formato G-Code y devuelve mensajes con
información de estado.
* El controlador, es quien conoce los parámetros geométricos y cinemáticos del
robot. Realiza un control parcial de la viabilidad de cada orden recibidas.

### Servicios del lado servidor:
* Panel de control del robot, mediante consola (CLI) que permita realizar:
  * Conexión/desconexión al Robot usando comunicación serial.
  * Activación/Desactivación del robot.
  * Listado de los comandos de control
  * Ayuda al operador, con ejemplificación de la sintaxis requerida para los comandos que lo requieran.
  * [modo manual]: Movimiento circular independiente de cada uno de los vínculos especificando la velocidad, sentido y ángulo a recorrer.
  * [modo manual]: Movimiento lineal del efector especificando la velocidad y la posición final.
  * [modo manual]: Actividad del efector final (propias de la herramienta particular elegida) especificando velocidad, tiempo de operación y entido de operación (si correspondieran).
  * [modo manual]: Movimiento a su “posición de origen/descanso”.
  * [modo manual]: Aprendizaje de trayectoria con almacenamiento de las órdenes correspondientes en un archivo de texto (legible) que ermita reproducir la misma.
  * [modo automático]: Carga y ejecución de un archivo conteniendo una secuencia de trabajo específica.
* Servidor XML-RPC, capaz de ejecutar las mismas operaciones anteriores
solicitadas en forma remota.
* La aplicación de consola debe implementar herencia desde la clase Cmd

### Servicios del lado Cliente. La interfaz principal debe ofrecer:
* Panel de control del robot, con funcionalidades similares a las de la interfaz de consola (es opcional en este caso la funcionalidad de aprendizaje mencionada).
  * Reporte mostrando la conexión, el estado de actividad del Robot, el instante de tiempo (acumulado) desde el inicio de actividad, el instante de inicio y el detalle de cada orden.
  * [opcional] GUI de control y monitoreo de parámetros.
  * [opcional] Despliegue visual del robot, usando vista 3D o proyecciones. En cualquiera de los casos puede usarse una estructura simplificada del robot, ejes/planos y escala (a su criterio).
  * [opcional] Tabla o curvas que muestren la velocidad de cada uno de los vínculos.
  * [opcional] Streaming de video mostrando el comportamiento del Robot usando una cámara remota.
  * [opcional] Efectos de sonido que indiquen el arranque/parada del robot, los cambios de posición del efector final y los momentos de actividad del mismo.
  * [opcional] Generación de alarmas visuales/auditivas cuando se intenten desplazamientos fuera del espacio de trabajo (aproximado).
* El efector final no agrega grados de libertad especiales, más allá de algún desplazamiento fijo en las coordenadas asumidas para el punto de operación.
* El aplicativo debe operar de manera completa con control desacoplado (aunque resulta mejor valorada aquella propuesta que avance en el control acoplado).
* Definir constantes apropiadas para los parámetros extremos (límites de trabajo).
* Otros datos constructivos del robot o plataforma son indicados durante el desarrollo

## Solución

Lenguaje: Python
Software del simulador 3D: Coppeliasim
Protocolo del servidor: XMLRPC
Libreria para el GUI: TKinter


![image](https://user-images.githubusercontent.com/63414974/140453346-ea8fa08e-983b-482c-9d0d-1a64b26384c3.png)

![image](https://user-images.githubusercontent.com/63414974/140453380-ed6f3878-1047-4d0a-b3dd-2b8a74b84033.png)

![image](https://user-images.githubusercontent.com/63414974/140453405-ca9d2562-6c9b-4d8a-815c-5fe7a2d0d66d.png)

