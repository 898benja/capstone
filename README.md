# Fix & Go

> Tu arreglo confiable, en un clic.

Fix & Go es una plataforma web y móvil que conecta a personas que necesitan resolver problemas técnicos del hogar con profesionales verificados de su zona. La primera validación se concentra en servicios de gas, electricidad y agua, con un flujo trazable desde la búsqueda hasta la evaluación del trabajo.

## Estado del proyecto

**Fase:** definición, validación del problema y planificación del MVP académico.

Este repositorio es la fuente de trabajo del equipo de APT122, sección 005D:

- Benjamín Olmedo
- Daniel Baeza
- Felipe Arce

El número de equipo aún no ha sido asignado. La definición vigente reemplaza completamente la propuesta anterior de gestión de iglesias.

## Propuesta de valor

Fix & Go busca reducir la incertidumbre de contratar servicios mediante:

- perfiles de profesionales con credenciales y especialidades verificables;
- búsqueda por categoría, ubicación y disponibilidad;
- solicitud, cotización y seguimiento del servicio;
- mensajería interna asociada a cada solicitud;
- pagos seguros y liberación contra hitos o cierre del trabajo;
- reputación basada en servicios efectivamente realizados.

La visión comercial considera una comisión del 20 % por servicio completado. El modelo y sus cifras son hipótesis que deben validarse antes de implementarse.

## Alcance por etapas

| Etapa | Resultado |
| --- | --- |
| Validación | Confirmar problemas, disposición de uso, categorías iniciales y proceso de verificación |
| MVP académico | Prototipo funcional del recorrido esencial con datos de prueba y servicios simulados |
| Piloto | Operación limitada con usuarios, profesionales y procesos de soporte controlados |
| Producto | Plataforma web/móvil, pagos, mensajería, verificación y operación escalable |

La visión completa incluye seguridad, pagos y verificación. El MVP académico puede simular integraciones sensibles, pero debe representar el flujo y sus reglas sin prometer garantías que todavía no existen.

## Documentación

| Documento | Propósito |
| --- | --- |
| [Fuente oficial consolidada](docs/00-official-source.md) | Definición vigente, decisiones, hipótesis y datos por validar |
| [Visión y alcance](docs/01-product-brief.md) | Problema, usuarios, propuesta de valor y límites |
| [Requisitos](docs/02-product-requirements.md) | Funciones, reglas y criterios de aceptación |
| [Modelo de dominio](docs/03-domain-model.md) | Entidades, relaciones, estados e invariantes |
| [Experiencia y flujos](docs/04-ux-and-flows.md) | Navegación y recorridos de cliente, profesional y administrador |
| [Arquitectura](docs/05-technical-architecture.md) | Stack propuesto, seguridad, datos y evolución |
| [Roadmap](docs/06-roadmap.md) | Etapas, prioridades y entregables |
| [Calidad](docs/07-quality-strategy.md) | Pruebas, seguridad y criterios de salida |
| [Plan de gestión Capstone](docs/08-project-management-plan.md) | Alcance, tiempo, costo, financiamiento, interesados y control |
| [Evidencias APT122](APT122_005D/Equipo_Por_Definir/Fase_1/README.md) | Orden oficial de la entrega académica |

## Criterios no negociables

- Ningún profesional se presenta como verificado sin evidencia y revisión trazable.
- La reputación proviene de servicios registrados en la plataforma.
- Los datos sensibles y pagos requieren controles de servidor; una interfaz local solo puede simularlos.
- La dirección exacta del cliente se comparte únicamente cuando el proceso lo necesita.
- Cliente, profesional y administrador poseen capacidades distintas.
- Las cifras comerciales sin fuente permanecen marcadas como hipótesis.
- Cada incremento debe poder demostrarse y validarse con usuarios.
