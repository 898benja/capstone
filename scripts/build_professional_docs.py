from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "docx"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "102A43"
YELLOW = "F6C445"
INK = "172B3A"
MUTED = "52606D"
PALE = "FFF8E6"
LIGHT = "F2F5F7"
WHITE = "FFFFFF"
DATE = "2 de septiembre de 2026"
TEAM = "Benjamín Olmedo · Daniel Baeza · Felipe Arce"


def shade(cell, color):
    props = cell._tc.get_or_add_tcPr()
    node = props.find(qn("w:shd"))
    if node is None:
        node = OxmlElement("w:shd")
        props.append(node)
    node.set(qn("w:fill"), color)


def margins(cell, value=110):
    props = cell._tc.get_or_add_tcPr()
    node = props.first_child_found_in("w:tcMar")
    if node is None:
        node = OxmlElement("w:tcMar")
        props.append(node)
    for name in ("top", "start", "bottom", "end"):
        edge = node.find(qn(f"w:{name}"))
        if edge is None:
            edge = OxmlElement(f"w:{name}")
            node.append(edge)
        edge.set(qn("w:w"), str(value))
        edge.set(qn("w:type"), "dxa")


def font(run, size=10, color=INK, bold=False, italic=False, family="Aptos"):
    run.font.name = family
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), family)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), family)
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string(color)
    run.bold = bold
    run.italic = italic


def configure(title):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.78)
    section.bottom_margin = Inches(0.72)
    section.left_margin = Inches(0.82)
    section.right_margin = Inches(0.82)
    section.header_distance = Inches(0.3)
    section.footer_distance = Inches(0.3)

    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
    normal.font.size = Pt(9.8)
    normal.font.color.rgb = RGBColor.from_string(INK)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.08

    for name, size, color in (("Heading 1", 17, NAVY), ("Heading 2", 13, NAVY), ("Heading 3", 11, INK)):
        style = doc.styles[name]
        style.font.name = "Aptos Display"
        style._element.rPr.rFonts.set(qn("w:ascii"), "Aptos Display")
        style._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos Display")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = Pt(10)
        style.paragraph_format.space_after = Pt(5)

    header = section.header.paragraphs[0]
    r = header.add_run("FIX & GO  /  DOCUMENTACIÓN OFICIAL")
    font(r, 8.2, MUTED, True)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = footer.add_run(f"{title}  •  {DATE}")
    font(r, 7.8, MUTED)
    return doc


def cover(doc, title, subtitle, code):
    for _ in range(3):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run("FIX & GO")
    font(r, 16, YELLOW, True, family="Aptos Display")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(title)
    font(r, 30, NAVY, True, family="Aptos Display")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run(subtitle)
    font(r, 14, INK)
    callout(doc, "PROPÓSITO", "Fuente profesional para definir, validar y construir Fix & Go sin confundir la visión comercial con el MVP académico.")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(34)
    r = p.add_run(f"{code}  •  Versión 2.0\n{DATE}\nAPT122-005D  •  Equipo por definir\n{TEAM}")
    font(r, 9.5, MUTED, True)
    doc.add_page_break()
    callout(doc, "CONTROL DE FUENTE", "Documento basado en el archivo FIX&GO y la presentación Canva entregados por el equipo. Las cifras sin respaldo se mantienen como hipótesis por validar.", PALE)


def callout(doc, label, text, fill=PALE, trailing=True):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    shade(cell, fill)
    margins(cell, 150)
    p = cell.paragraphs[0]
    r = p.add_run(label + "\n")
    font(r, 8.2, NAVY, True)
    r = p.add_run(text)
    font(r, 10.2, INK)
    if trailing:
        doc.add_paragraph().paragraph_format.space_after = Pt(1)


def section(doc, title, paragraphs=None, bullets=None):
    doc.add_heading(title, level=1)
    for text in paragraphs or []:
        p = doc.add_paragraph(text)
        p.paragraph_format.widow_control = True
    for text in bullets or []:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.32)
        p.paragraph_format.first_line_indent = Inches(-0.16)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        font(r)


def numbered(doc, items):
    for text in items:
        p = doc.add_paragraph(style="List Number")
        p.paragraph_format.left_indent = Inches(0.38)
        p.paragraph_format.first_line_indent = Inches(-0.2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        font(r)


def table(doc, headers, rows, widths=None):
    tab = doc.add_table(rows=1, cols=len(headers))
    tab.alignment = WD_TABLE_ALIGNMENT.CENTER
    tab.style = "Table Grid"
    for idx, value in enumerate(headers):
        cell = tab.rows[0].cells[idx]
        shade(cell, NAVY)
        margins(cell)
        r = cell.paragraphs[0].add_run(value)
        font(r, 8.8, WHITE, True)
    for row_index, values in enumerate(rows):
        cells = tab.add_row().cells
        for idx, value in enumerate(values):
            if row_index % 2:
                shade(cells[idx], LIGHT)
            margins(cells[idx])
            cells[idx].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            r = cells[idx].paragraphs[0].add_run(str(value))
            font(r, 8.8)
    if widths:
        for row in tab.rows:
            for idx, cell in enumerate(row.cells):
                cell.width = Inches(widths[idx])
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def save(doc, filename, title, subject):
    props = doc.core_properties
    props.title = title
    props.subject = subject
    props.author = "Equipo Fix & Go"
    props.keywords = "Fix & Go, APT122, servicios técnicos, plataforma, MVP"
    props.comments = "Documento basado en la definición oficial consolidada de Fix & Go."
    doc.save(OUT / filename)


def build_index():
    title = "Índice Ejecutivo de Documentación"
    doc = configure(title)
    cover(doc, title, "Mapa del paquete profesional de producto y desarrollo", "FGO-DOC-000")
    section(doc, "1. Propósito", ["Alinear al equipo en una definición única de Fix & Go, separar hipótesis de decisiones y entregar una base verificable para el trabajo académico y técnico."])
    table(doc, ["Código", "Documento", "Uso"], [
        ("FGO-PROD-001", "Documento Maestro del Producto", "Visión, problema, usuarios, negocio y riesgos"),
        ("FGO-FUNC-001", "Especificación Funcional del MVP", "Capacidades, estados, permisos y aceptación"),
        ("FGO-ARCH-001", "Modelo de Dominio y Arquitectura", "Datos, invariantes, stack, seguridad y evolución"),
        ("FGO-PLAN-001", "Roadmap y Plan de Validación", "Etapas, experimentos, calidad y salida"),
    ], [1.4, 2.6, 2.8])
    section(doc, "2. Orden de lectura", bullets=[
        "Presentación académica: Maestro → Roadmap.",
        "Diseño y UX: Maestro → Especificación → Roadmap.",
        "Desarrollo: Especificación → Dominio y Arquitectura → Roadmap.",
        "Validación: Maestro → Especificación → Roadmap.",
    ])
    section(doc, "3. Control documental")
    table(doc, ["Campo", "Valor"], [
        ("Producto", "Fix & Go"), ("Versión", "2.0"), ("Fecha", DATE),
        ("Sección", "APT122-005D"), ("Equipo", "Número pendiente"),
        ("Estado", "Base oficial para planificación"),
    ], [1.8, 5.0])
    callout(doc, "IDENTIDAD", "Fix & Go — Tu arreglo confiable, en un clic.", trailing=False)
    save(doc, "00_FIX_AND_GO_Indice_Ejecutivo.docx", title, "Índice del paquete documental")


def build_master():
    title = "Documento Maestro del Producto"
    doc = configure(title)
    cover(doc, title, "Visión, alcance, modelo de negocio y riesgos", "FGO-PROD-001")
    section(doc, "1. Resumen ejecutivo", [
        "Fix & Go es una plataforma web y móvil que conecta a clientes con profesionales cercanos y verificables para resolver servicios técnicos del hogar. La entrada se concentra en gas, electricidad y agua.",
        "La solución reúne búsqueda, perfiles, credenciales, solicitudes, cotizaciones, mensajería, pago, seguimiento y reputación. El MVP académico representa el recorrido con datos ficticios e integraciones simuladas; el producto comercial exigirá infraestructura, cumplimiento y operación real.",
    ])
    callout(doc, "PROPUESTA DE VALOR", "Encontrar, contratar y evaluar a un profesional confiable desde un solo lugar.")
    section(doc, "2. Problema", bullets=[
        "Contratación fragmentada entre recomendaciones, redes sociales y avisos generales.",
        "Poca información comparable sobre especialidad, cobertura, disponibilidad y precio.",
        "Dificultad para comprobar identidad, certificaciones y experiencia.",
        "Escasa trazabilidad de acuerdos, cambios, pagos y reclamos.",
        "Profesionales formales con pocas herramientas para diferenciarse y construir reputación.",
    ])
    section(doc, "3. Actores y resultados")
    table(doc, ["Actor", "Necesidad", "Resultado"], [
        ("Cliente", "Resolver con menor incertidumbre", "Solicitud clara, seguimiento y respaldo"),
        ("Profesional", "Acceder a demanda y demostrar confianza", "Oportunidades trazables y pago ordenado"),
        ("Administrador", "Proteger la operación", "Validación, soporte y auditoría"),
    ], [1.3, 2.7, 2.8])
    section(doc, "4. Alcance de la visión", bullets=[
        "Perfiles diferenciados y permisos de cliente, profesional y administrador.",
        "Verificación de identidad, especialidad y credenciales pertinentes.",
        "Búsqueda por categoría, zona, disponibilidad, reputación y verificación.",
        "Solicitud, cotización, agenda, mensajería y seguimiento.",
        "Pago seguro, comisión, reembolso y disputa mediante proveedor externo.",
        "Evaluaciones vinculadas a servicios completados y moderación trazable.",
    ])
    section(doc, "5. Alcance del MVP académico", bullets=[
        "Datos e identidades completamente ficticios.",
        "Recorrido completo para gas, electricidad y agua.",
        "Verificación, mensajería, ubicación y pago simulados y etiquetados.",
        "Pruebas con clientes y profesionales potenciales.",
        "Sin dinero, documentos ni direcciones reales.",
    ])
    section(doc, "6. Modelo de negocio preliminar", [
        "La hipótesis comercial es una comisión del 20 % por servicio completado. Un trabajo de $50.000 genera $10.000 de ingreso bruto para la plataforma.",
        "La inversión inicial informada es $6.500.000 y los costos fijos mensuales se estiman entre $340.000 y $900.000. Con el ingreso unitario del ejemplo, el equilibrio contable está entre 34 y 90 servicios; 62 servicios equivale a un costo de $620.000. La recuperación en 1 año y 5 meses requiere un escenario financiero completo antes de comunicarse como proyección.",
    ])
    section(doc, "7. Hipótesis críticas", bullets=[
        "La verificación visible aumenta confianza e intención de contratar.",
        "Existe oferta suficiente de profesionales formales en las categorías iniciales.",
        "Clientes y profesionales aceptan el proceso digital y la comisión.",
        "La plataforma puede gestionar disputas sin un costo de soporte inviable.",
        "Gas, electricidad y agua son un foco inicial manejable y relevante.",
    ])
    section(doc, "8. Riesgos", bullets=[
        "Baja adopción o desequilibrio entre oferta y demanda.",
        "Fraude, suplantación, filtración de datos y fallas de pago.",
        "Credenciales difíciles de comprobar o con vigencias distintas.",
        "Competencia de plataformas establecidas y precios informales.",
        "Responsabilidad legal y reputacional por servicios deficientes.",
        "Tiempo y presupuesto limitados del equipo académico.",
    ])
    section(doc, "9. Expansión", ["Construcción, mecánica, barbería, gastronomía, kinesiología y otras categorías son oportunidades futuras. Cada una requiere validar demanda, oferta, seguridad y regulación antes de incorporarse."])
    callout(doc, "CRITERIO DE ÉXITO", "El MVP es exitoso si usuarios potenciales completan el recorrido, entienden la verificación y perciben más confianza y trazabilidad que en el proceso informal.", trailing=False)
    save(doc, "01_FIX_AND_GO_Documento_Maestro_Producto.docx", title, "Visión y alcance de Fix & Go")


def build_functional():
    title = "Especificación Funcional del MVP"
    doc = configure(title)
    cover(doc, title, "Requisitos, estados, permisos y criterios de aceptación", "FGO-FUNC-001")
    section(doc, "1. Roles")
    table(doc, ["Rol", "Capacidades"], [
        ("Cliente", "Buscar, solicitar, comparar, contratar, seguir, disputar y evaluar sus servicios"),
        ("Profesional", "Gestionar perfil, credenciales, disponibilidad, cotizaciones, trabajos y reputación"),
        ("Administrador", "Revisar credenciales, moderar, auditar y atender incidentes según privilegios"),
    ], [1.5, 5.3])
    section(doc, "2. Descubrimiento", bullets=[
        "Buscar por gas, electricidad o agua y zona de cobertura.",
        "Filtrar por disponibilidad, reputación y verificación.",
        "Mostrar perfil, experiencia declarada, credenciales vigentes y evaluaciones elegibles.",
        "No exponer dirección ni identidad privada durante la búsqueda.",
    ])
    section(doc, "3. Solicitud y cotización", bullets=[
        "El cliente registra categoría, descripción, zona, urgencia, disponibilidad y adjuntos opcionales.",
        "El profesional pregunta, rechaza o envía cotización con alcance, precio, fecha y vigencia.",
        "El cliente compara y acepta una única cotización vigente.",
        "Cada transición conserva actor, fecha y estado anterior/nuevo.",
    ])
    section(doc, "4. Servicio, mensajes y cierre", bullets=[
        "La cotización aceptada crea el servicio contratado.",
        "Cliente y profesional comparten agenda y mensajes asociados.",
        "El profesional inicia y declara finalización; el cliente confirma, disputa o solicita revisión.",
        "La plataforma conserva un historial cronológico comprensible.",
    ])
    section(doc, "5. Verificación", bullets=[
        "La credencial registra tipo, emisor, vigencia, evidencia, estado, revisor y motivo.",
        "Solo una aprobación vigente habilita el distintivo para la especialidad.",
        "Rechazo, expiración o suspensión retiran el distintivo sin borrar historial.",
    ])
    section(doc, "6. Pagos y reputación", bullets=[
        "El proveedor externo maneja los datos de pago; la plataforma conserva referencias y estados.",
        "Liberación y reembolso son idempotentes y auditables.",
        "La comisión, monto profesional, impuestos y ajustes se desglosan.",
        "Solo participantes de un servicio completado pueden evaluarse.",
    ])
    section(doc, "7. Estados principales")
    table(doc, ["Concepto", "Estados"], [
        ("Solicitud", "Borrador, publicada, cotizada, asignada, cancelada, expirada"),
        ("Cotización", "Borrador, enviada, aceptada, rechazada, retirada, expirada"),
        ("Servicio", "Agendado, en progreso, esperando cliente, completado, cancelado, disputado"),
        ("Credencial", "Borrador, enviada, en revisión, aprobada, rechazada, expirada"),
        ("Pago", "Creado, autorizado, retenido, liberado, reembolsado, fallido"),
    ], [1.5, 5.3])
    section(doc, "8. Recorrido de demostración")
    numbered(doc, [
        "Administrador revisa y aprueba una credencial ficticia.",
        "Cliente busca una categoría y compara perfiles.",
        "Cliente crea una solicitud y recibe dos cotizaciones ficticias.",
        "Cliente acepta una propuesta y observa el pago simulado.",
        "Profesional gestiona agenda, mensajes y estado del trabajo.",
        "Cliente confirma el cierre y publica una evaluación.",
        "Administrador consulta la trazabilidad y un caso de disputa.",
    ])
    section(doc, "9. Criterios globales", bullets=[
        "Responsive, accesible y operable con teclado.",
        "Permisos validados fuera de la interfaz.",
        "Estados de carga, vacío, error, reintento y permiso insuficiente.",
        "Datos ficticios coherentes y simulaciones identificables.",
        "Sin secretos, documentos personales ni pagos reales.",
    ])
    save(doc, "02_FIX_AND_GO_Especificacion_Funcional_MVP.docx", title, "Requisitos funcionales del MVP")


def build_architecture():
    title = "Modelo de Dominio y Arquitectura"
    doc = configure(title)
    cover(doc, title, "Datos, invariantes, stack y controles de seguridad", "FGO-ARCH-001")
    section(doc, "1. Núcleo de dominio", ["El servicio contratado es el centro operacional. Nace desde una cotización aceptada y relaciona agenda, participantes, mensajes, pagos, cierre, disputa y evaluación."])
    table(doc, ["Entidad", "Responsabilidad"], [
        ("User / Profiles", "Identidad digital y perfiles diferenciados"),
        ("ServiceCategory", "Categoría y requisitos de especialidad"),
        ("Credential", "Evidencia y decisión de verificación"),
        ("ServiceRequest", "Necesidad, zona y disponibilidad del cliente"),
        ("Quote", "Propuesta de alcance, precio y condiciones"),
        ("ServiceJob", "Ejecución y trazabilidad del trabajo"),
        ("Message", "Comunicación vinculada al servicio"),
        ("Payment", "Referencia, desglose y estado del proveedor"),
        ("Review / Dispute", "Reputación elegible y resolución de incidentes"),
        ("AuditEvent", "Actor, acción, objetivo y fecha"),
    ], [1.8, 5.0])
    section(doc, "2. Invariantes", bullets=[
        "Una sola cotización aceptada por solicitud.",
        "Verificación derivada de credencial aprobada y vigente.",
        "Evaluación limitada a participantes de un servicio completado.",
        "Pago desglosado e idempotente; la plataforma nunca almacena tarjeta completa.",
        "Dirección exacta visible solo para participantes y etapa autorizados.",
        "Acciones administrativas conservan responsable, motivo y fecha.",
    ])
    section(doc, "3. Stack recomendado")
    table(doc, ["Capa", "Tecnología", "Razón"], [
        ("Móvil", "React Native + Expo", "iOS/Android con TypeScript compartido"),
        ("Web", "Next.js", "paneles, accesibilidad y ecosistema"),
        ("API", "NestJS", "módulos, validación y pruebas"),
        ("Datos", "PostgreSQL + PostGIS", "transacciones, relaciones y geodatos"),
        ("Colas", "Redis", "límites, trabajos y coordinación"),
        ("Archivos", "S3 compatible", "privacidad, URLs firmadas y ciclo de vida"),
        ("Identidad", "OIDC gestionado", "MFA y recuperación robusta"),
        ("Observabilidad", "OpenTelemetry", "métricas y trazas portables"),
    ], [1.2, 2.2, 3.4])
    section(doc, "4. Estrategia estructural", ["Un monolito modular reduce la carga de un equipo de tres personas. Identidad, verificación, solicitudes, cotizaciones, servicios, pagos, mensajes, reputación y administración mantienen límites internos y adaptadores externos."])
    section(doc, "5. Seguridad y privacidad", bullets=[
        "Autorización por rol y pertenencia al recurso en cada operación.",
        "MFA para administración; cifrado y secretos fuera del código.",
        "Archivos privados, URLs breves, validación y análisis antimalware.",
        "Webhooks firmados, idempotencia y conciliación de pagos.",
        "Rate limiting, protección contra enumeración y auditoría.",
        "Minimización, retención, borrado y respaldos probados.",
        "Geolocalización aproximada para búsqueda y exacta solo al contratar.",
    ])
    section(doc, "6. MVP académico", ["Puede usar una API local o de desarrollo, datos ficticios y adaptadores simulados. Los contratos deben permitir reemplazar pagos, mensajería, identidad y almacenamiento sin reescribir reglas del dominio."])
    section(doc, "7. Decisiones pendientes", bullets=[
        "Proveedor de identidad y pagos con soporte en Chile.",
        "Nube, región, costos y objetivos de disponibilidad.",
        "Retención legal de credenciales y datos financieros.",
        "Mensajería en tiempo real o asincrónica según validación.",
    ])
    save(doc, "03_FIX_AND_GO_Modelo_Dominio_Arquitectura.docx", title, "Modelo y arquitectura técnica")


def build_roadmap():
    title = "Roadmap y Plan de Validación"
    doc = configure(title)
    cover(doc, title, "Alcance, tiempo, costos, interesados, financiamiento y validación", "FGO-PLAN-001")
    section(doc, "1. Estrategia", ["El orden reduce incertidumbre: problema y confianza antes que tecnología costosa; recorrido antes que integración; piloto controlado antes que expansión."])
    table(doc, ["Fase", "Trabajo", "Salida"], [
        ("0. Evidencia", "Entrevistas, categorías, verificación, comisión", "Hipótesis medibles y alcance"),
        ("1. Prototipo", "Flujos de cliente, profesional y administrador", "Usabilidad y lenguaje corregidos"),
        ("2. MVP", "Recorrido completo con simulaciones", "Demo reproducible y probada"),
        ("3. Piloto", "Integraciones, seguridad, soporte y cumplimiento", "Operación cerrada y monitoreada"),
        ("4. Aprendizaje", "Métricas, costos, disputas y satisfacción", "Decisión de iterar o escalar"),
        ("5. Escala", "Geografía, oferta y nuevas categorías", "Crecimiento con controles"),
    ], [1.1, 3.5, 2.2])
    section(doc, "2. Alcance controlado", bullets=[
        "Incluye cliente, profesional y administrador; gas, electricidad y agua; búsqueda, perfiles, solicitud, cotización, seguimiento, mensajería, pago/verificación simulados y evaluación.",
        "Excluye operación pública, dinero o documentos reales, GPS productivo, tiendas de aplicaciones, nuevas categorías, automatización avanzada y microservicios.",
        "Todo cambio debe declarar beneficio, horas, costo, riesgo y trabajo equivalente que se retirará.",
    ])
    section(doc, "3. Cronograma y capacidad")
    table(doc, ["Semanas", "Objetivo", "Evidencia"], [
        ("1–2", "Definición, interesados y entrevistas", "Alcance y riesgos"),
        ("3–4", "Requisitos, flujos y prototipo", "Backlog y prueba UX"),
        ("5–6", "Arquitectura, datos y entorno", "ADR y base integrada"),
        ("7–10", "Perfiles, búsqueda, solicitud y cotización", "Primer flujo vertical"),
        ("11–13", "Servicio e integraciones simuladas", "MVP end-to-end"),
        ("14–15", "Calidad, accesibilidad y seguridad", "Reportes y correcciones"),
        ("16–18", "Validación, estabilización y cierre", "Evidencia y presentación"),
    ], [1.1, 3.6, 2.1])
    section(doc, "4. Presupuesto y financiamiento", [
        "La línea base supone 18 semanas, tres estudiantes y 8 horas semanales por persona: 432 horas-persona brutas. Se reserva 15 %, dejando aproximadamente 367 horas planificables. El equipo debe recalibrar este supuesto con registros reales.",
        "El MVP se financia con tiempo, computadores, conectividad y herramientas gratuitas o educativas. El desembolso base es $0 y el techo propuesto es $150.000 CLP: hasta $30.000 en nube, $25.000 en publicación opcional, $60.000 en pruebas y $35.000 de contingencia. Todo gasto superior a $20.000 requiere acuerdo de los tres.",
        "Los $6.500.000 del material original corresponden a un escenario comercial por validar, no al costo del Capstone. Un piloto posterior podrá evaluar aporte de fundadores, alianzas, fondos de emprendimiento o inversión temprana con un presupuesto independiente.",
    ])
    section(doc, "5. Gestión de interesados")
    table(doc, ["Interesado", "Estrategia", "Información"], [
        ("Equipo", "Gestionar de cerca", "Tareas, riesgos y decisiones semanales"),
        ("Docente/evaluadores", "Gestionar de cerca", "Evidencia y cumplimiento por hito"),
        ("Clientes", "Involucrar", "Prototipo, privacidad y hallazgos"),
        ("Profesionales", "Involucrar", "Verificación, comisión y flujo"),
        ("Soporte futuro", "Consultar", "Carga operativa e incidentes"),
        ("Proveedores/reguladores", "Mantener satisfechos", "Requisitos, límites y cumplimiento"),
        ("Inversionistas", "Informar con evidencia", "Métricas, costos y riesgos"),
        ("Competidores", "Monitorear", "Propuesta y cambios de mercado"),
    ], [1.6, 2.1, 3.1])
    section(doc, "6. Gobierno y comunicación", bullets=[
        "Planificación semanal y seguimiento breve dos veces por semana.",
        "Revisión demostrable quincenal y revisión de riesgos/costos.",
        "Benjamín lidera frontend y prototipado; backend/datos y calidad/documentación se asignan entre Daniel y Felipe en la semana 2.",
        "Cada entregable tiene responsable y revisor distinto.",
        "Alcance, dinero, publicación y uso de datos reales requieren acuerdo de los tres.",
    ])
    section(doc, "7. Validaciones prioritarias", bullets=[
        "Entrevistas separadas con clientes y profesionales.",
        "Prueba de confianza antes/después de mostrar credenciales y reseñas.",
        "Test de comparación de cotizaciones y comprensión del precio.",
        "Disposición profesional a una comisión del 20 %.",
        "Proceso manual de revisión de credenciales por categoría.",
        "Modelo financiero con costos variables y crecimiento mensual.",
    ])
    section(doc, "8. Métricas", bullets=[
        "Finalización del recorrido sin ayuda y tiempo por etapa.",
        "Conversión solicitud → cotización → aceptación → cierre.",
        "Tiempo de respuesta profesional y cumplimiento de agenda.",
        "Cancelación, disputa, reembolso y repetición.",
        "Costo de adquisición, soporte y verificación.",
        "Ingreso neto por servicio y margen de contribución.",
    ])
    section(doc, "9. Calidad del MVP", bullets=[
        "Tres recorridos de categoría inicial y tres roles demostrables.",
        "Permisos, transiciones, comisión y reputación cubiertos por pruebas.",
        "Accesibilidad, responsive y estados de error verificados.",
        "Simulaciones visibles; cero datos personales y secretos.",
        "Documentación y trazabilidad actualizadas.",
    ])
    section(doc, "10. Riesgos y respuesta")
    table(doc, ["Riesgo", "Respuesta inicial"], [
        ("Baja adopción", "Entrevistas, prototipo y piloto geográfico acotado"),
        ("Poca oferta", "Incorporación manual y categorías limitadas"),
        ("Fraude", "Verificación, permisos, auditoría y límites"),
        ("Disputas", "Estados claros, evidencia y soporte definido"),
        ("Costo", "Monolito modular, servicios gestionados y presupuesto por etapa"),
        ("Alcance", "No ampliar categorías antes de validar el núcleo"),
    ], [2.0, 4.8])
    section(doc, "11. Hito académico", ["La referencia propone un MVP hacia la semana 18. El equipo debe reconciliar ese objetivo con el calendario oficial de APT122 y trabajar en incrementos quincenales demostrables."])
    callout(doc, "REGLA DE CIERRE", "La fase no termina por cantidad de pantallas: termina cuando la evidencia demuestra que el recorrido es comprensible, seguro en su simulación y coherente con el problema.", trailing=False)
    save(doc, "04_FIX_AND_GO_Roadmap_Plan_Validacion.docx", title, "Roadmap y validación")


if __name__ == "__main__":
    build_index()
    build_master()
    build_functional()
    build_architecture()
    build_roadmap()
    print(f"Generated 5 DOCX files in {OUT}")
