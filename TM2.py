import pandas as pd
import random
from faker import Faker
fake = Faker()

Faker.seed(0)
random.seed(0)

N_DIM = 1000
N_HECHOS = 15000

# -----------------------------
# Generar tablas de dimensiones
# -----------------------------

dim_cliente = pd.DataFrame({
    'id_cliente': range(1, N_DIM+1),
    'nombre': [fake.first_name() for _ in range(N_DIM)],
    'apellido': [fake.last_name() for _ in range(N_DIM)],
    'segmento': [random.choice(['Residencial', 'Empresarial', 'Corporativo']) for _ in range(N_DIM)],
    'tipo_documento': [random.choice(['DNI', 'Pasaporte', 'Carnet']) for _ in range(N_DIM)],
    'nro_documento': [fake.unique.random_number(digits=8) for _ in range(N_DIM)],
    'edad': [random.randint(18, 80) for _ in range(N_DIM)],
    'sexo': [random.choice(['Masculino', 'Femenino']) for _ in range(N_DIM)]
})

dim_plan = pd.DataFrame({
    'id_plan': range(1, N_DIM+1),
    'nombre_plan': [f"Plan {i}" for i in range(1, N_DIM+1)],
    'tipo_plan': [random.choice(['Prepago', 'Postpago']) for _ in range(N_DIM)],
    'velocidad_internet': [random.choice(['10Mbps', '50Mbps', '100Mbps', '1Gbps']) for _ in range(N_DIM)],
    'minutos_incluidos': [random.randint(100, 1000) for _ in range(N_DIM)],
    'datos_incluidos': [round(random.uniform(1, 100), 2) for _ in range(N_DIM)],
    'precio_mensual': [round(random.uniform(10, 100), 2) for _ in range(N_DIM)],
    'roaming': [random.choice([0, 1]) for _ in range(N_DIM)]
})

dim_dispositivo = pd.DataFrame({
    'id_dispositivo': range(1, N_DIM+1),
    'marca': [random.choice(['Samsung', 'Apple', 'Xiaomi', 'Motorola']) for _ in range(N_DIM)],
    'modelo': [fake.word() for _ in range(N_DIM)],
    'tipo_dispositivo': [random.choice(['Smartphone', 'Tablet', 'Router']) for _ in range(N_DIM)],
    'sistema_operativo': [random.choice(['Android', 'iOS', 'HarmonyOS']) for _ in range(N_DIM)],
    'almacenamiento': [random.choice(['64GB', '128GB', '256GB']) for _ in range(N_DIM)],
    'pantalla': [random.choice(['5"', '6.5"', '7.2"']) for _ in range(N_DIM)],
    'año_lanzamiento': [random.randint(2015, 2024) for _ in range(N_DIM)]
})

dim_ubicacion = pd.DataFrame({
    'id_ubicacion': range(1, N_DIM+1),
    'pais': ['Perú']*N_DIM,
    'region': [fake.state() for _ in range(N_DIM)],
    'ciudad': [fake.city() for _ in range(N_DIM)],
    'codigo_postal': [fake.postcode() for _ in range(N_DIM)],
    'zona_cobertura': [random.choice(['Urbana', 'Rural']) for _ in range(N_DIM)],
    'tipo_area': [random.choice(['Residencial', 'Comercial']) for _ in range(N_DIM)],
    'torre_cercana': [f'Torre_{random.randint(1, 100)}' for _ in range(N_DIM)]
})

dim_facturacion = pd.DataFrame({
    'id_facturacion': range(1, N_DIM+1),
    'metodo_pago': [random.choice(['Tarjeta', 'Transferencia', 'Efectivo']) for _ in range(N_DIM)],
    'ciclo_facturacion': [random.choice(['Mensual', 'Bimestral']) for _ in range(N_DIM)],
    'estado_pago': [random.choice(['Pagado', 'Pendiente']) for _ in range(N_DIM)],
    'monto': [round(random.uniform(20, 150), 2) for _ in range(N_DIM)],
    'fecha_pago': [fake.date_between(start_date='-1y', end_date='today') for _ in range(N_DIM)],
    'mora': [random.choice([0, 1]) for _ in range(N_DIM)],
    'descuento_aplicado': [round(random.uniform(0, 20), 2) for _ in range(N_DIM)]
})

dim_promocion = pd.DataFrame({
    'id_promocion': range(1, N_DIM+1),
    'nombre_promocion': [f"Promo {i}" for i in range(1, N_DIM+1)],
    'tipo_promocion': [random.choice(['Temporada', 'Fidelidad']) for _ in range(N_DIM)],
    'descuento_porcentaje': [round(random.uniform(5, 50), 2) for _ in range(N_DIM)],
    'fecha_inicio': [fake.date_between(start_date='-2y', end_date='-6m') for _ in range(N_DIM)],
    'fecha_fin': [fake.date_between(start_date='-5m', end_date='today') for _ in range(N_DIM)],
    'aplica_a_planes': [random.choice(['Todos', 'Postpago', 'Prepago']) for _ in range(N_DIM)],
    'aplica_a_dispositivos': [random.choice(['Todos', 'Smartphones', 'Tablets']) for _ in range(N_DIM)]
})

dim_fecha = pd.DataFrame({
    'id_fecha': range(1, N_DIM+1),
    'fecha': [fake.date_between(start_date='-2y', end_date='today') for _ in range(N_DIM)],
    'dia': [random.randint(1, 31) for _ in range(N_DIM)],
    'mes': [random.randint(1, 12) for _ in range(N_DIM)],
    'año': [random.randint(2022, 2025) for _ in range(N_DIM)],
    'trimestre': [random.randint(1, 4) for _ in range(N_DIM)],
    'dia_semana': [random.choice(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']) for _ in range(N_DIM)],
    'es_feriado': [random.choice([0, 1]) for _ in range(N_DIM)]
})

dim_soporte = pd.DataFrame({
    'id_soporte': range(1, N_DIM+1),
    'tipo_incidente': [random.choice(['Corte', 'Consulta', 'Reclamo']) for _ in range(N_DIM)],
    'canal_contacto': [random.choice(['Teléfono', 'Web', 'App']) for _ in range(N_DIM)],
    'resolucion': [fake.sentence(nb_words=5) for _ in range(N_DIM)],
    'tiempo_respuesta': [random.randint(1, 120) for _ in range(N_DIM)],
    'agente': [fake.name() for _ in range(N_DIM)],
    'satisfaccion': [random.choice(['Alta', 'Media', 'Baja']) for _ in range(N_DIM)],
    'fecha_contacto': [fake.date_between(start_date='-1y', end_date='today') for _ in range(N_DIM)]
})

dim_servicio = pd.DataFrame({
    'id_servicio': range(1, N_DIM+1),
    'tipo_servicio': [random.choice(['Internet', 'TV', 'Telefonía']) for _ in range(N_DIM)],
    'descripcion': [fake.sentence(nb_words=4) for _ in range(N_DIM)],
    'proveedor': [random.choice(['Claro', 'Movistar', 'Entel', 'Bitel']) for _ in range(N_DIM)],
    'tecnologia': [random.choice(['4G', '5G', 'Fibra']) for _ in range(N_DIM)],
    'limite_uso': [random.choice(['Ilimitado', '100GB', '50GB']) for _ in range(N_DIM)],
    'tarifa_base': [round(random.uniform(30, 120), 2) for _ in range(N_DIM)],
    'region_disponible': [fake.state() for _ in range(N_DIM)]
})

dim_evento = pd.DataFrame({
    'id_evento': range(1, N_DIM+1),
    'tipo_evento': [random.choice(['Campaña', 'Reclamo', 'Mantenimiento']) for _ in range(N_DIM)],
    'descripcion': [fake.sentence(nb_words=5) for _ in range(N_DIM)],
    'canal': [random.choice(['Email', 'SMS', 'Llamada']) for _ in range(N_DIM)],
    'estado': [random.choice(['Activo', 'Finalizado']) for _ in range(N_DIM)],
    'fecha_evento': [fake.date_between(start_date='-1y', end_date='today') for _ in range(N_DIM)],
    'responsable': [fake.name() for _ in range(N_DIM)],
    'observaciones': [fake.text(max_nb_chars=30) for _ in range(N_DIM)]
})

# -----------------------------
# Tabla de hechos
# -----------------------------

hechos_telecom = pd.DataFrame({
    'id_cliente': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_plan': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_dispositivo': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_ubicacion': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_facturacion': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_promocion': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_fecha': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_soporte': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_servicio': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'id_evento': [random.randint(1, N_DIM) for _ in range(N_HECHOS)],
    'duracion_llamada': [round(random.uniform(0.5, 60), 2) for _ in range(N_HECHOS)],
    'datos_consumidos_gb': [round(random.uniform(0.1, 50), 2) for _ in range(N_HECHOS)],
    'minutos_usados': [random.randint(1, 1000) for _ in range(N_HECHOS)],
    'mensajes_enviados': [random.randint(0, 500) for _ in range(N_HECHOS)],
    'costo_total': [round(random.uniform(10, 300), 2) for _ in range(N_HECHOS)],
    'ancho_banda': [random.choice(['10Mbps', '50Mbps', '100Mbps']) for _ in range(N_HECHOS)]
})

# -----------------------------
# Exportar a CSV
# -----------------------------

dim_cliente.to_csv("dim_cliente.csv", index=False)
dim_plan.to_csv("dim_plan.csv", index=False)
dim_dispositivo.to_csv("dim_dispositivo.csv", index=False)
dim_ubicacion.to_csv("dim_ubicacion.csv", index=False)
dim_facturacion.to_csv("dim_facturacion.csv", index=False)
dim_promocion.to_csv("dim_promocion.csv", index=False)
dim_fecha.to_csv("dim_fecha.csv", index=False)
dim_soporte.to_csv("dim_soporte.csv", index=False)
dim_servicio.to_csv("dim_servicio.csv", index=False)
dim_evento.to_csv("dim_evento.csv", index=False)
hechos_telecom.to_csv("hechos_telecom.csv", index=False)

print("✅ ¡Todos los archivos .csv fueron creados con éxito!")