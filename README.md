# RUAHTONE

> Todo lo que necesitas para preparar el servicio. En un solo lugar.

RUAHTONE es un sistema operativo para organizar una iglesia y sus ministerios. Su primera validación busca demostrar que un servicio puede prepararse y coordinarse sin usar WhatsApp como sistema de organización.

## Estado del proyecto

**Fase:** definición y preparación del MVP frontend local.

El repositorio contiene por ahora la documentación que guiará el diseño, la implementación y la validación. El MVP utilizará React, TypeScript, Vite, Tailwind CSS, shadcn/ui, Lucide, Framer Motion y persistencia en LocalStorage. No incluye backend, autenticación real, pagos ni servicios cloud.

## Cómo orientarse

| Documento | Propósito |
| --- | --- |
| [Visión y alcance](docs/01-product-brief.md) | Problema, propuesta de valor, usuarios y límites del MVP |
| [Requisitos del producto](docs/02-product-requirements.md) | Capacidades, reglas de negocio y criterios de aceptación |
| [Modelo de dominio](docs/03-domain-model.md) | Entidades, relaciones, estados e invariantes |
| [Experiencia y navegación](docs/04-ux-and-flows.md) | Arquitectura de información, roles y flujos de demo |
| [Arquitectura técnica](docs/05-technical-architecture.md) | Stack, capas, estado, persistencia y estructura propuesta |
| [Roadmap](docs/06-roadmap.md) | Fases de entrega, prioridades y definición de terminado |
| [Calidad](docs/07-quality-strategy.md) | Estrategia de pruebas y checklist de lanzamiento |
| [Forma de trabajo](CONTRIBUTING.md) | Convenciones, ramas, commits, PR y decisiones |
| [Registro de decisiones](docs/decisions/README.md) | ADRs del proyecto |

## Principios no negociables

- El **servicio** es la unidad operacional central; el calendario solo ayuda a encontrarlo.
- Una persona tiene una identidad y puede servir en varios ministerios.
- La asistencia pertenece a una asignación y la confirma el propio servidor.
- La tonalidad original pertenece a `Song`; la tonalidad usada pertenece a `ServiceSong`.
- Los recursos siempre se relacionan con una canción, servicio o ministerio.
- La actividad es un historial estructurado, no un chat.
- La experiencia y los permisos cambian según el contexto del usuario.
- Primero se valida un frontend local coherente; luego se diseña el SaaS real.

## Primer hito

El primer incremento debe cubrir el flujo vertical completo: abrir el próximo servicio, consultar asignaciones, confirmar asistencia, gestionar repertorio con tonalidad contextual, actualizar checklist y observar la actividad resultante, todo persistido en LocalStorage.

