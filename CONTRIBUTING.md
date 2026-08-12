# Contribuir a RUAHTONE

## Flujo de trabajo

1. Elegir un requisito o historia con criterio de aceptación claro.
2. Crear una rama con prefijo `codex/` para trabajo realizado desde Codex, o `feat/`, `fix/`, `docs/` para trabajo humano acordado.
3. Implementar el incremento más pequeño que recorra UI, caso de uso, dominio y persistencia cuando corresponda.
4. Ejecutar verificaciones locales y recorrer el flujo afectado.
5. Abrir un PR pequeño con evidencia y riesgos conocidos.

## Convenciones de commits

Se recomienda Conventional Commits:

```text
feat(services): add personal attendance confirmation
fix(songs): preserve original key when editing a service song
docs(domain): clarify resource ownership invariant
```

## Pull requests

El PR debe indicar:

- problema que resuelve y requisitos relacionados;
- comportamiento antes y después;
- pruebas automáticas y manuales ejecutadas;
- capturas para cambios visuales relevantes;
- impacto en LocalStorage o migración;
- accesibilidad y responsive revisados;
- limitaciones o trabajo posterior.

No mezclar refactors amplios con una funcionalidad salvo que sean imprescindibles.

## Código

- Mantener reglas del negocio fuera de componentes.
- Preferir funciones puras y selectores para datos derivados.
- No duplicar entidades relacionadas en el estado.
- Evitar `any`, IDs mágicos, estadísticas hardcodeadas y acceso directo a LocalStorage.
- Toda acción que cambia preparación relevante debe evaluar si genera actividad.
- Los textos visibles se escriben en español de Chile; los identificadores de código, en inglés.

## Decisiones

Crear un ADR cuando el cambio afecte arquitectura, modelo, alcance, persistencia, seguridad conceptual o una dependencia estructural. Copiar la plantilla de `docs/decisions/000-template.md`, asignar el siguiente número y enlazar documentos impactados.

## Seguridad y datos

El MVP contiene únicamente datos ficticios. No agregar teléfonos, archivos ni información real de miembros. LocalStorage no es almacenamiento seguro y la interfaz no debe presentarlo como tal.

