# ADR 001 — MVP académico con adaptadores simulados

**Estado:** Aceptado
**Fecha:** 2026-09-02

## Contexto

La visión incluye verificación, pagos, mensajería y ubicación, pero operar esas capacidades con datos reales excede la fase de planificación y aumenta el riesgo académico, legal y de seguridad.

## Decisión

El MVP demostrará el recorrido completo con datos ficticios y adaptadores que simulan proveedores externos. Toda simulación será visible. Los contratos se diseñan para sustituirse por integraciones reales sin trasladar lógica de negocio a la interfaz.

## Consecuencias

### Positivas

- Permite validar la experiencia end-to-end.
- Evita procesar dinero, credenciales o direcciones reales.
- Conserva una ruta técnica hacia el piloto.

### Costos y riesgos

- No demuestra confiabilidad de proveedores reales.
- Puede generar expectativas incorrectas si la interfaz no etiqueta la simulación.
- Requerirá pruebas adicionales al integrar servicios externos.

## Alternativas consideradas

- Integraciones reales desde el primer incremento: descartadas por riesgo y tiempo.
- Eliminar pagos y verificación del prototipo: descartado porque impediría validar diferenciadores centrales.
