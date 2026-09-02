# ADR 002 — Servicio contratado como centro operacional

**Estado:** Aceptado
**Fecha:** 2026-09-02

## Contexto

La búsqueda y la solicitud atraen al usuario, pero la confianza se materializa al acordar, ejecutar, pagar y evaluar un trabajo. Separar esas acciones sin un vínculo central debilitaría la trazabilidad.

## Decisión

`ServiceJob` será el agregado operacional creado desde una cotización aceptada. Agenda, participantes, mensajes, pagos, cierre, disputa y evaluación referencian el mismo servicio.

## Consecuencias

### Positivas

- Historial coherente para cliente, profesional y soporte.
- Reglas claras para pagos y evaluaciones.
- Auditoría de estados y responsabilidades.

### Costos y riesgos

- Requiere transiciones cuidadosas y manejo de concurrencia.
- El agregado debe evitar crecer con detalles que pertenecen a módulos externos.

## Alternativas consideradas

- Conversación como centro: descartada porque no representa acuerdos ni dinero.
- Solicitud como único agregado: descartada porque mezcla exploración con ejecución contractual.
