# Requisitos del producto

**Estado:** Propuesto para validar el MVP

## Identidad y acceso

- **IAM-001:** registrar cuentas de cliente y profesional con consentimiento de términos y privacidad.
- **IAM-002:** autenticar sesiones y permitir recuperación segura de acceso.
- **IAM-003:** aplicar permisos de cliente, profesional y administrador en servidor.
- **IAM-004:** mantener separados los datos públicos del perfil y los datos privados de identidad.

## Verificación profesional

- **VER-001:** el profesional registra especialidades, cobertura y antecedentes requeridos.
- **VER-002:** cada credencial posee tipo, emisor, vigencia, evidencia, estado y revisor.
- **VER-003:** los estados son `draft`, `submitted`, `underReview`, `approved`, `rejected` y `expired`.
- **VER-004:** solo una aprobación vigente habilita el distintivo “verificado” para la especialidad correspondiente.
- **VER-005:** toda decisión administrativa conserva fecha, responsable y motivo.

## Descubrimiento y perfiles

- **DSP-001:** buscar profesionales por categoría y zona de cobertura.
- **DSP-002:** filtrar por disponibilidad, reputación y estado de verificación.
- **DSP-003:** mostrar especialidad, experiencia declarada, credenciales aprobadas, cobertura, reputación y disponibilidad.
- **DSP-004:** ocultar datos privados y dirección exacta antes de una relación autorizada.

## Solicitud y cotización

- **REQ-001:** el cliente crea una solicitud con categoría, descripción, zona, urgencia, disponibilidad y archivos opcionales.
- **REQ-002:** el profesional acepta participar, solicita aclaraciones o rechaza.
- **REQ-003:** una cotización registra alcance, precio, fecha, vigencia y condiciones.
- **REQ-004:** el cliente acepta una única cotización vigente.
- **REQ-005:** toda transición queda en un historial trazable.

## Servicio y comunicación

- **JOB-001:** un servicio nace desde una cotización aceptada.
- **JOB-002:** estados: `scheduled`, `inProgress`, `awaitingClient`, `completed`, `cancelled` y `disputed`.
- **MSG-001:** cliente y profesional intercambian mensajes dentro del contexto de una solicitud o servicio.
- **MSG-002:** la comunicación conserva autor, fecha y vínculo; no reemplaza el canal de emergencia.
- **NTF-001:** avisos informan cambios accionables sin exponer contenido sensible en la pantalla bloqueada.

## Pagos y disputas

- **PAY-001:** registrar intención, autorización, retención, liberación, reembolso y fallo mediante un proveedor externo.
- **PAY-002:** nunca almacenar datos completos de tarjetas.
- **PAY-003:** la liberación requiere una transición válida del servicio y operación idempotente.
- **PAY-004:** calcular comisión, monto del profesional, impuestos y devoluciones de forma auditable.
- **DSPT-001:** cliente o profesional puede abrir una disputa con motivo y evidencia.

## Reputación

- **REV-001:** solo participantes de un servicio completado pueden evaluarlo.
- **REV-002:** una evaluación registra puntuación, comentario, autor, destinatario y servicio.
- **REV-003:** moderación conserva el registro original y el motivo de cualquier ocultamiento.
- **REV-004:** los promedios se calculan desde evaluaciones elegibles; no se editan manualmente.

## Administración

- **ADM-001:** revisar credenciales y perfiles reportados.
- **ADM-002:** consultar solicitudes, servicios, pagos, disputas y auditoría según privilegios.
- **ADM-003:** suspender una cuenta mediante un flujo justificado y reversible.
- **ADM-004:** gestionar categorías y requisitos sin alterar historial.

## Requisitos del prototipo académico

- **MVP-001:** usar únicamente datos ficticios.
- **MVP-002:** demostrar cliente, profesional y administrador.
- **MVP-003:** simular pagos, revisión documental, geolocalización y mensajería si no existen integraciones seguras.
- **MVP-004:** etiquetar claramente toda simulación.
- **MVP-005:** cubrir un recorrido de gas, uno de electricidad y uno de agua.

## No funcionales

- **NFR-001:** experiencia responsive y accesible con contraste WCAG AA, teclado y foco visible.
- **NFR-002:** cifrado en tránsito y en reposo para infraestructura productiva.
- **NFR-003:** autorización, rate limiting, auditoría, validación de entrada y protección contra abuso.
- **NFR-004:** disponibilidad y rendimiento se medirán con objetivos definidos antes del piloto.
- **NFR-005:** respaldo, restauración y eliminación de datos deben probarse.
- **NFR-006:** observabilidad sin registrar documentos, mensajes o direcciones sensibles.
- **NFR-007:** cumplir normativa chilena aplicable y condiciones de los proveedores externos.

## Criterio de aceptación del recorrido principal

Con datos de prueba, un cliente encuentra un profesional verificado, crea una solicitud, compara y acepta una cotización, observa la ejecución, confirma el cierre y publica una evaluación. El profesional gestiona su disponibilidad, responde y completa el servicio. El administrador revisa la credencial y puede auditar el proceso.

