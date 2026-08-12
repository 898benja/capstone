# Documentación de RUAHTONE

## Fuentes de verdad

La documentación se usa en este orden cuando exista una contradicción:

1. Decisiones aceptadas en `docs/decisions/`.
2. Requisitos e invariantes de `02-product-requirements.md` y `03-domain-model.md`.
3. Visión y alcance de `01-product-brief.md`.
4. Arquitectura, UX, roadmap y calidad.
5. Implementación actual, si todavía no se ha reconciliado con los documentos anteriores.

Una decisión no debe cambiarse silenciosamente. Si afecta el modelo, el alcance, una dependencia importante o un principio de UX, se registra mediante un ADR y se actualizan los documentos afectados en el mismo cambio.

## Convenciones

- Los términos del dominio se escriben en español en producto y UX.
- Los nombres de tipos y código se escriben en inglés.
- **Debe** expresa una condición obligatoria; **puede** expresa una opción.
- Cada requisito estable tiene un identificador para poder referenciarlo desde issues y pruebas.
- El estado documental se clasifica como `Propuesto`, `Aceptado`, `Reemplazado` u `Obsoleto`.

## Mantenimiento

La documentación se revisa al cerrar cada hito. Una funcionalidad no se considera terminada si cambia el comportamiento acordado y su documentación no fue actualizada.

