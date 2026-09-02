# Experiencia y flujos

**Estado:** Propuesto

## Principios de experiencia

- Confianza antes que velocidad aparente.
- El siguiente paso siempre es visible.
- La verificación se explica; no se reduce a un ícono ambiguo.
- Precio, alcance, fecha y condiciones se confirman antes de aceptar.
- Los estados críticos combinan color, texto e icono.
- La interfaz distingue simulaciones académicas de capacidades reales.

## Arquitectura de información

### Cliente

Inicio, Buscar, Solicitudes, Servicios, Mensajes, Pagos simulados, Perfil y Ayuda.

### Profesional

Inicio, Oportunidades, Cotizaciones, Agenda, Servicios, Mensajes, Credenciales, Reputación y Perfil.

### Administrador

Resumen, Verificaciones, Usuarios, Servicios, Pagos, Disputas, Reportes y Auditoría.

## Flujo principal del cliente

1. Selecciona gas, electricidad o agua.
2. Indica zona, urgencia y una descripción segura del problema.
3. Revisa profesionales y entiende por qué están verificados.
4. Abre un perfil y compara reputación, cobertura y disponibilidad.
5. Crea la solicitud y recibe cotizaciones.
6. Compara alcance, precio, fecha y condiciones.
7. Acepta una cotización y revisa el resumen antes de confirmar.
8. Sigue el servicio, conversa dentro del contexto y confirma el cierre.
9. Evalúa al profesional desde el servicio completado.

## Flujo del profesional

1. Completa perfil, especialidades y zona de cobertura.
2. Presenta credenciales y observa su estado de revisión.
3. Define disponibilidad.
4. Revisa una oportunidad compatible y solicita aclaraciones si corresponde.
5. Envía una cotización con alcance y condiciones.
6. Gestiona agenda, ejecución y evidencias del servicio.
7. Marca el trabajo como finalizado y espera confirmación o resolución.
8. Consulta el desglose de pago y reputación.

## Flujo del administrador

1. Abre la cola de credenciales y prioriza vencimientos o riesgo.
2. Revisa evidencia sin descargarla innecesariamente.
3. Aprueba, rechaza o solicita corrección con motivo.
4. Atiende reportes o disputas desde una vista cronológica.
5. Ejecuta acciones reversibles y deja auditoría.

## Estados de interfaz obligatorios

Cada pantalla crítica contempla carga, vacío, error, sin conexión, permiso insuficiente y éxito. Las operaciones de pago o revisión muestran estado pendiente y evitan dobles envíos.

## Diseño visual

La identidad usa amarillo como acento de acción y azul oscuro para confianza y estructura. Se evita saturar cada pantalla con amarillo. La tipografía debe ser legible, los controles táctiles de al menos 44 × 44 px y la jerarquía consistente en móvil y web.

## Validación de usabilidad

Las pruebas moderadas deben observar si el usuario:

- diferencia profesional “verificado” de perfil simplemente completo;
- entiende qué información será compartida y cuándo;
- compara cotizaciones sin ayuda;
- reconoce el estado actual y siguiente paso;
- identifica que los pagos y mensajes del prototipo son simulados;
- completa el recorrido sin depender de explicación del facilitador.

