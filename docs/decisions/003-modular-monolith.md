# ADR 003 — Monolito modular para el inicio

**Estado:** Propuesto
**Fecha:** 2026-09-02

## Contexto

El equipo es de tres estudiantes y necesita entregar valor antes de asumir la carga operacional de múltiples servicios distribuidos. A la vez, pagos, mensajería y verificación requieren fronteras claras.

## Decisión

Construir un backend modular desplegado como una unidad, con PostgreSQL como fuente transaccional y adaptadores para servicios externos. Los módulos se comunican mediante contratos internos y eventos cuando sea útil.

## Consecuencias

### Positivas

- Desarrollo y despliegue simples para un equipo pequeño.
- Transacciones coherentes y pruebas integradas.
- Límites preparados para extraer componentes solo con evidencia.

### Costos y riesgos

- Disciplina necesaria para evitar acoplamiento entre módulos.
- Escalamiento independiente limitado al comienzo.

## Alternativas consideradas

- Microservicios desde el inicio: descartados por complejidad desproporcionada.
- Backend sin módulos: descartado porque dificultaría seguridad y evolución.
