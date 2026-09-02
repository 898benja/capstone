# Documentación de Fix & Go

## Orden de autoridad

1. [Fuente oficial consolidada](00-official-source.md).
2. ADR aceptados en [`decisions/`](decisions/README.md).
3. Requisitos e invariantes de producto.
4. UX, arquitectura, roadmap y calidad.
5. Implementación actual, mientras se reconcilia con los documentos.

La fuente oficial consolida la información entregada por el equipo en el documento FIX&GO y la presentación Canva. Los elementos sin respaldo suficiente se mantienen como hipótesis o datos por validar; no se convierten en hechos por repetición.

## Convenciones

- **Debe** indica una condición obligatoria; **puede**, una opción.
- Los requisitos estables usan identificadores trazables.
- Los estados documentales son `Propuesto`, `Aceptado`, `Reemplazado` u `Obsoleto`.
- “Visión de producto” describe la solución final; “MVP académico” describe lo demostrable durante APT122.
- Los montos se expresan en pesos chilenos (CLP) y requieren fecha y supuesto.

## Mantenimiento

Los documentos se revisan al cerrar cada hito. Una funcionalidad no se considera terminada si contradice una decisión vigente o deja documentación y pruebas desactualizadas.

