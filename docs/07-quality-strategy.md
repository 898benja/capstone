# Estrategia de calidad

**Estado:** Propuesto

## Pirámide de pruebas

### Dominio y unidades

Prioridad alta para invariantes y cálculos:

- un cambio en `ServiceSong.key` no modifica `Song.originalKey`;
- confirmar modifica una sola asignación;
- contadores y progreso coinciden con entidades reales;
- duplicar reinicia asistencia y mantiene solo la estructura elegida;
- recursos y checklists respetan sus relaciones mínimas;
- detección de conflictos horarios;
- permisos por contexto;
- migración, hidratación y reset del store.

### Integración de componentes

Cubrir formularios, confirmaciones, cambio de contexto, reordenamiento alternativo, toasts, diálogos destructivos y actividad resultante. Se prueban resultados observables, no detalles internos.

### End to end

Automatizar al menos los cuatro flujos descritos en [experiencia y flujos](04-ux-and-flows.md). Cada ejecución parte de seed conocido y recarga la página para verificar persistencia.

## Verificación manual

- Navegar directamente y mediante enlaces a todas las rutas.
- Recargar en cada ruta crítica.
- Probar 360, 768, 1024 y 1440 px.
- Probar temas claro y oscuro y preferencia de movimiento reducido.
- Recorrer solo con teclado y comprobar orden de foco.
- Revisar contraste, zoom a 200 % y textos extensos.
- Confirmar estados vacío, error local, toast y diálogo.
- Verificar cero errores importantes en consola.

## Integridad de datos demo

Un test de seed debe validar IDs únicos, referencias existentes, fechas válidas, órdenes coherentes y estadísticas derivadas. Ejemplos visuales como “6/7 confirmados” solo aparecen si existen siete asignaciones y seis confirmadas.

## Pruebas con usuarios

Cada sesión registra contexto del participante, tareas, tiempo, éxito sin ayuda, dudas, errores y comentarios. El facilitador evita explicar la interfaz. Los hallazgos se clasifican por impacto y frecuencia, no por preferencia estética aislada.

## Gate del candidato MVP

- build de producción exitoso;
- TypeScript, lint y suite automatizada sin fallos;
- cuatro flujos completos;
- persistencia y reset verificados;
- dark/light y responsive verificados;
- sin acciones principales falsas;
- limitaciones simuladas documentadas;
- requisitos críticos trazados a pruebas.

