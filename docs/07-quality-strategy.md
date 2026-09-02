# Estrategia de calidad

**Estado:** Propuesto

## Prioridades

1. Proteger identidad, documentos, ubicación, mensajes y pagos.
2. Mantener transiciones y cálculos consistentes.
3. Evitar promesas engañosas de verificación o seguridad.
4. Garantizar un recorrido comprensible y accesible.
5. Detectar fallos antes de afectar una operación real.

## Pruebas de dominio

- una sola cotización aceptada por solicitud;
- verificación derivada de credencial aprobada y vigente;
- evaluaciones limitadas a servicios completados;
- cálculo de comisión y monto neto;
- pagos idempotentes;
- transiciones válidas de solicitud, servicio, disputa y credencial;
- permisos por actor y relación con el recurso;
- exposición gradual de ubicación.

## Integración

Probar base de datos, almacenamiento privado, proveedor de identidad, webhooks de pago, notificaciones y colas mediante dobles controlados y ambientes de prueba. Los contratos externos deben cubrir demora, duplicación, caída y reintento.

## End to end

- cliente crea solicitud y acepta cotización;
- profesional presenta credencial, cotiza y completa servicio;
- administrador revisa credencial y atiende una disputa;
- pago simulado evita doble liberación;
- participantes publican evaluación elegible.

## Seguridad

- análisis estático y de dependencias en CI;
- pruebas de autorización por objeto y rol;
- límites de velocidad y resistencia a enumeración;
- carga de archivos maliciosos y tipos falsificados;
- verificación de webhooks e idempotencia;
- revisión de exposición en logs y analítica;
- respaldo y restauración;
- evaluación de amenazas antes del piloto.

## Usabilidad y accesibilidad

Revisar 360, 768, 1024 y 1440 px; teclado; foco visible; contraste; zoom a 200 %; lectores de pantalla en recorridos críticos; estados de carga, vacío, error y conectividad limitada.

## Datos de prueba

Los datos son ficticios pero coherentes: identidades inventadas, credenciales marcadas como simuladas, direcciones no reales y pagos de entorno de prueba. Cada conjunto incluye casos felices, vencidos, rechazados y disputados.

## Gate del MVP académico

- build, tipos y pruebas sin fallos;
- tres recorridos por categoría inicial;
- roles y permisos demostrables;
- ninguna integración simulada se presenta como real;
- cero secretos o datos personales en el repositorio;
- documentación y matriz de requisitos actualizadas;
- evidencia de pruebas con usuarios y hallazgos priorizados.

