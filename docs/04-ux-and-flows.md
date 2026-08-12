# Experiencia, navegación y flujos

**Estado:** Propuesto para diseño detallado

## Arquitectura de información

Rutas base:

| Ruta | Destino |
| --- | --- |
| `/` | Inicio contextual |
| `/services` | Servicios |
| `/services/:serviceId` | Centro del Servicio |
| `/calendar` | Calendario |
| `/songs` | Biblioteca de canciones |
| `/songs/:songId` | Detalle de canción |
| `/people` | Personas |
| `/resources` | Recursos |
| `/ministries` | Ministerios |
| `/sound` | Preparación de sonido |
| `/settings` | Configuración |

El Centro del Servicio es el destino canónico desde dashboard, calendario, búsqueda, notificaciones e historial. No se crean variantes desconectadas de la misma pantalla.

## Jerarquía de una pantalla

1. Qué está pasando.
2. Qué necesita saber el usuario.
3. Qué debe hacer ahora.
4. Información secundaria y trazabilidad.

Cada pantalla posee una acción principal. Los estados vacíos explican qué ocurrirá y ofrecen el siguiente paso. Las simulaciones deben comunicar su alcance.

## Inicio por contexto

| Contexto | Prioridad | Acción primaria |
| --- | --- | --- |
| Servidor/músico | próximo servicio, asistencia, canciones, cambios, ensayo | responder asistencia |
| Líder | próximo servicio, confirmaciones, repertorio, pendientes | gestionar servicio |
| Sonido | próximo servicio, cambios técnicos, checklist, P16 y patch | continuar preparación |
| Pastor | estado, ministerios, alertas y observaciones | abrir servicio |
| Administrador | servicios, ministerios, personas y estado general | crear servicio |

El cambio de contexto modifica menú, dashboard, permisos y acciones; no es un filtro cosmético.

## Centro del Servicio

El encabezado muestra nombre, fecha, horario, lugar, tipo, estado y acción principal. El contenido ofrece una síntesis antes del detalle:

- ministerios con confirmados sobre asignados;
- personas, función y asistencia;
- repertorio ordenado con tonalidad contextual;
- recursos relacionados;
- checklists y progreso;
- alertas y observaciones;
- actividad reciente.

En móvil, la síntesis, la confirmación y el repertorio aparecen antes de las áreas administrativas.

## Navegación adaptativa

La barra lateral se expande o colapsa en desktop. En móvil se convierte en navegación inferior o drawer; la decisión final se toma durante prototipado según la cantidad de destinos por contexto. Las rutas siguen siendo estables aunque un destino no aparezca en el menú de un rol.

## Flujos de aceptación

### Flujo principal

1. Abrir Inicio y reconocer el próximo servicio.
2. Abrir su Centro y consultar asignaciones.
3. Como servidor, confirmar la propia asistencia.
4. Cambiar a líder y comprobar el contador actualizado.
5. Abrir una canción, observar su tono original y volver al servicio.
6. Cambiar solo el tono del `ServiceSong` y verificar que el original permanece.
7. Asociar un recurso, completar una tarea y comprobar la actividad.
8. Abrir el servicio desde Calendario.
9. Duplicarlo, cambiar la fecha y comprobar confirmaciones pendientes.

### Flujo de sonido

1. Cambiar a contexto Sonido y reconocer el próximo servicio.
2. Consultar músicos, cambios desde el servicio anterior, P16 y patch.
3. Revisar la prueba de sonido y completar preparación.
4. Comprobar el nuevo progreso en la vista y dashboard.

### Flujo líder de adoración

1. Abrir servicio y reconocer quién falta por confirmar.
2. Agregar canción, reordenarla por drag and drop y mediante fallback.
3. Cambiar tonalidad, agregar nota y asociar PDF.
4. Comprobar cada cambio en actividad.

### Flujo pastor

1. Reconocer preparación general, alertas y ministerios desde Inicio.
2. Abrir el servicio y comprender su estado sin entrar a configuración técnica.

## Principios visuales

- Identidad tranquila, tecnológica y elegante; cristiana sin clichés gráficos.
- Base neutral con azul y morado como acentos controlados.
- Inter como tipografía inicial y escala compacta, legible y consistente.
- Dark mode diseñado con jerarquía propia, no como simple inversión.
- Movimiento sutil para navegación, cambios de estado, modales, toasts y reordenamiento.
- No abusar de gradientes, sombras, glassmorphism ni texto gigante.

## Accesibilidad

La experiencia admite teclado, foco visible, controles de al menos 44 × 44 px cuando sean táctiles, contraste WCAG AA y mensajes textuales para estados. El reordenamiento nunca depende exclusivamente de arrastrar. `prefers-reduced-motion` desactiva movimiento no esencial.

