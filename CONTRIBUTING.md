# Contribuir a Fix & Go

## Flujo de trabajo

1. Elegir un requisito o historia con criterio de aceptación claro.
2. Crear una rama breve con prefijo `feat/`, `fix/`, `docs/`, `test/` o `chore/`.
3. Implementar el incremento más pequeño que atraviese interfaz, caso de uso, dominio y datos cuando corresponda.
4. Ejecutar verificaciones automáticas y recorrer manualmente el flujo afectado.
5. Abrir un pull request con evidencia, riesgos y relación con los requisitos.

## Convención de commits

```text
feat(requests): create service request flow
fix(payments): prevent duplicate release action
docs(product): clarify professional verification scope
test(reputation): cover completed-service review rule
```

## Pull requests

Cada PR debe indicar el problema, requisitos relacionados, comportamiento antes y después, pruebas, capturas si cambia la interfaz, impacto en datos o seguridad, limitaciones y trabajo posterior.

No se incluyen datos personales reales, credenciales, direcciones, documentos de identidad ni llaves de servicios externos. Los secretos se almacenan fuera del repositorio.

## Convenciones técnicas

- Reglas de negocio fuera de componentes visuales.
- TypeScript estricto y sin `any` injustificado.
- Identificadores de código en inglés; textos visibles en español de Chile.
- Estados derivados no se duplican en la base de datos.
- Toda operación sensible valida permisos en el backend, no solo en la interfaz.
- Integraciones de pago, mensajería y verificación se abstraen mediante adaptadores.
- Un cambio de arquitectura, alcance o seguridad requiere un ADR.

## Documentación

La fuente principal es [docs/00-official-source.md](docs/00-official-source.md). Si cambia una decisión, el mismo PR debe actualizar requisitos, modelo, arquitectura y pruebas afectados.

