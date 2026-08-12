# ADR 001 — MVP local-first con frontera de repositorio

**Estado:** Aceptado  
**Fecha:** 2026-08-12

## Contexto

La prioridad es validar experiencia y reglas de negocio antes de financiar backend, autenticación y operación cloud. Sin una frontera técnica, el uso directo de LocalStorage desde la UI haría costosa la evolución posterior.

## Decisión

El MVP funciona sin red y persiste un store versionado en LocalStorage. Los casos de uso dependen de contratos de repositorio y serialización, no de la API del navegador. Los datos demo se pueden restablecer.

## Consecuencias

### Positivas

- Iteración y demostración rápidas.
- Flujos completos sin infraestructura externa.
- Sustitución posterior del adaptador con menor impacto.

### Costos y riesgos

- No hay sincronización, colaboración real ni seguridad de servidor.
- Límites de almacenamiento y archivos simulados.
- Las migraciones locales deben mantenerse desde el inicio.

## Alternativas consideradas

- Backend desde el primer incremento: descartado por costo antes de validar el problema.
- LocalStorage directo en componentes: descartado por acoplamiento y difícil migración.

