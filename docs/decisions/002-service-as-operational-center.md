# ADR 002 — Servicio como agregado y destino principal

**Estado:** Aceptado  
**Fecha:** 2026-08-12

## Contexto

El problema real no es almacenar listas aisladas, sino preparar un servicio con personas, repertorio, recursos, tareas y cambios relacionados. Un dashboard o calendario genérico fragmentaría nuevamente la información.

## Decisión

`Service` es el agregado operacional principal y `/services/:serviceId` su destino canónico. Calendario, búsqueda, Inicio y notificaciones conducen a ese centro. Canciones y personas conservan identidad global, pero su participación se modela mediante `ServiceSong` y `ServiceAssignment`.

## Consecuencias

### Positivas

- La navegación refleja el modelo mental de la iglesia.
- Tonalidad, asistencia, tareas y recursos mantienen contexto.
- Los flujos de los distintos roles convergen en una fuente coherente.

### Costos y riesgos

- El Centro del Servicio puede crecer en complejidad y necesita divulgación progresiva.
- Las fronteras entre entidades globales y contextuales deben respetarse rigurosamente.

## Alternativas consideradas

- Calendario como página principal: descartado porque permite encontrar eventos, pero no prepararlos.
- Módulos CRUD independientes: descartado porque reproduce la fragmentación que el producto busca eliminar.

