# Requisitos del producto

**Estado:** Aceptado para el MVP

## Requisitos funcionales

### Servicios

- **SRV-001:** crear, editar, duplicar, publicar, completar y archivar un servicio.
- **SRV-002:** registrar nombre, tipo, fecha, horas, lugar, descripción y estado.
- **SRV-003:** concentrar ministerios, asignaciones, repertorio, recursos, checklists, observaciones y actividad en un único Centro del Servicio.
- **SRV-004:** relacionar ensayos con el servicio que preparan, sin modelarlos obligatoriamente como un servicio independiente.
- **SRV-005:** al duplicar, conservar la estructura seleccionada, asignar una nueva fecha y reiniciar todas las confirmaciones.
- **SRV-006:** soportar tipos `worship`, `rehearsal`, `conference`, `youth`, `meeting` y `specialEvent` sin asumir que comparten idéntica preparación.

### Personas, ministerios y asignaciones

- **PPL-001:** una persona puede pertenecer a cero o más ministerios con una sola identidad.
- **PPL-002:** rol y ministerio son conceptos diferentes; el rol gobierna responsabilidad y el ministerio indica dónde sirve.
- **ASN-001:** una asignación relaciona servicio, persona, ministerio y función específica.
- **ASN-002:** solo el servidor asignado modifica su respuesta de asistencia; líderes y administradores la observan.
- **ASN-003:** los estados de asistencia son `pending`, `confirmed`, `declined` y `late`.
- **ASN-004:** una ausencia o llegada tarde debe producir una alerta visible para el liderazgo.
- **ASN-005:** una doble asignación incompatible en horarios superpuestos genera advertencia, sin bloquear en el MVP.

### Canciones y recursos

- **SNG-001:** `Song.originalKey` representa la referencia global y no cambia al editar un servicio.
- **SNG-002:** cada canción agregada a un servicio crea un `ServiceSong` con orden, tonalidad, BPM opcional, versión, notas y estado.
- **SNG-003:** el repertorio puede reordenarse mediante arrastre y mediante botones como alternativa accesible.
- **SNG-004:** el detalle de una canción muestra información general, recursos, historial y servicios donde fue utilizada.
- **RES-001:** un recurso debe relacionarse al menos con una canción, un servicio o un ministerio.
- **RES-002:** se admiten PDF, partitura, chord chart, secuencia, multitrack, audio, video, imagen, documento y otro.

### Preparación y trazabilidad

- **CHK-001:** los checklists son contextuales a un servicio, ministerio o persona; no existe un checklist universal.
- **CHK-002:** completar una tarea actualiza inmediatamente el progreso derivado.
- **ACT-001:** cambios relevantes generan actividad estructurada con actor, fecha, entidad y resumen.
- **ACT-002:** la actividad no admite conversaciones, reacciones ni funciones sociales.
- **NTF-001:** solo se presentan avisos accionables o sensibles al tiempo.

### Contexto, navegación y configuración

- **CTX-001:** el usuario demo puede cambiar entre contextos autorizados sin crear identidades distintas.
- **CTX-002:** dashboard, navegación, información y acciones se adaptan al contexto activo.
- **PER-001:** servidor, líder, pastor y administrador tienen capacidades diferenciadas aunque no exista autenticación real.
- **NAV-001:** inicio, calendario, listado, búsqueda y notificaciones abren el mismo Centro del Servicio.
- **SRC-001:** `Cmd/Ctrl + K` busca servicios, canciones, personas, recursos y ministerios.
- **SET-001:** configuración incluye tema, datos de iglesia, preferencias demo y restablecimiento confirmado.
- **DAT-001:** las modificaciones persisten en LocalStorage y pueden volver a un conjunto demo coherente.

### Sonido

- **SND-001:** sonido mantiene vistas de sala, monitoreo y una extensión futura para streaming.
- **SND-002:** un servicio puede definir patch, escena, prueba de sonido y asignaciones P16 propias.
- **SND-003:** la configuración no controla equipamiento físico; representa información operacional.
- **SND-004:** debe ser posible comparar cambios relevantes con un servicio anterior.

## Estados

| Concepto | Estados |
| --- | --- |
| Servicio | `planning`, `organizing`, `confirming`, `ready`, `completed`, `archived` |
| Asistencia | `pending`, `confirmed`, `declined`, `late` |
| Prueba de sonido | `pending`, `inProgress`, `completed` |
| Persona | `active`, `inactive` |
| Checklist item | incompleto o completo |

Las transiciones de servicio deben validarse en la capa de dominio. Archivar no elimina historial. Eliminar será una acción confirmada y, mientras no exista backend, su comportamiento exacto se decidirá antes de implementarlo.

## Requisitos no funcionales

- **NFR-001:** TypeScript sin errores y sin `any` injustificado en el dominio.
- **NFR-002:** responsive desde 360 px, con prioridad desktop pero sin pérdida de acciones críticas en móvil.
- **NFR-003:** temas claro y oscuro con contraste verificable; ningún estado depende solo del color.
- **NFR-004:** controles con nombre accesible, foco visible y operación por teclado.
- **NFR-005:** datos demo y métricas derivadas siempre consistentes.
- **NFR-006:** ninguna acción principal aparenta funcionar si no produce un resultado; las simulaciones se identifican.
- **NFR-007:** la aplicación funciona íntegramente en local y sin APIs externas.
- **NFR-008:** rutas críticas admiten recarga directa en el entorno local.

## Reglas de cálculo

- Los contadores de confirmación se derivan de asignaciones, nunca se almacenan.
- El progreso de checklist se deriva de sus ítems.
- El historial de uso de una canción se deriva de `ServiceSong` asociados a servicios pasados.
- Las alertas se derivan de ausencias, atrasos, conflictos y preparación incompleta.
- Los datos visuales nunca deben contradecir las entidades de origen.

## Matriz de cobertura

| Capacidad | Requisitos | Flujo de demo |
| --- | --- | --- |
| Coordinación del servicio | SRV-001–006, ASN-001 | Principal, Pastor |
| Confirmación personal | ASN-002–004 | Principal, Líder |
| Repertorio contextual | SNG-001–004 | Principal, Líder |
| Recursos y preparación | RES-001–002, CHK-001–002 | Principal, Sonido |
| Trazabilidad | ACT-001–002 | Principal, Líder |
| Experiencia contextual | CTX-001–002, PER-001 | Todos |
| Operación de sonido | SND-001–004 | Sonido |

