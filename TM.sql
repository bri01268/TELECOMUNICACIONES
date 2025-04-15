-- Base de datos: TM (Telecomunicaciones)
CREATE DATABASE TM;
USE TM;

-- =========================
-- 🟩 Dimensiones
-- =========================

CREATE TABLE dim_cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    segmento VARCHAR(30),
    tipo_documento VARCHAR(20),
    nro_documento VARCHAR(20),
    edad INT,
    sexo VARCHAR(10)
);

CREATE TABLE dim_plan (
    id_plan INT PRIMARY KEY,
    nombre_plan VARCHAR(50),
    tipo_plan VARCHAR(30),
    velocidad_internet VARCHAR(20),
    minutos_incluidos INT,
    datos_incluidos DECIMAL(10,2),
    precio_mensual DECIMAL(10,2),
    roaming BIT
);

CREATE TABLE dim_dispositivo (
    id_dispositivo INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    tipo_dispositivo VARCHAR(30),
    sistema_operativo VARCHAR(30),
    almacenamiento VARCHAR(20),
    pantalla VARCHAR(20),
    año_lanzamiento INT
);

CREATE TABLE dim_ubicacion (
    id_ubicacion INT PRIMARY KEY,
    pais VARCHAR(50),
    region VARCHAR(50),
    ciudad VARCHAR(50),
    codigo_postal VARCHAR(10),
    zona_cobertura VARCHAR(30),
    tipo_area VARCHAR(20),
    torre_cercana VARCHAR(50)
);

CREATE TABLE dim_facturacion (
    id_facturacion INT PRIMARY KEY,
    metodo_pago VARCHAR(30),
    ciclo_facturacion VARCHAR(20),
    estado_pago VARCHAR(20),
    monto DECIMAL(10,2),
    fecha_pago DATE,
    mora BIT,
    descuento_aplicado DECIMAL(5,2)
);

CREATE TABLE dim_promocion (
    id_promocion INT PRIMARY KEY,
    nombre_promocion VARCHAR(50),
    tipo_promocion VARCHAR(30),
    descuento_porcentaje DECIMAL(5,2),
    fecha_inicio DATE,
    fecha_fin DATE,
    aplica_a_planes VARCHAR(100),
    aplica_a_dispositivos VARCHAR(100)
);

CREATE TABLE dim_fecha (
    id_fecha INT PRIMARY KEY,
    fecha DATE,
    dia INT,
    mes INT,
    año INT,
    trimestre INT,
    dia_semana VARCHAR(15),
    es_feriado BIT
);

CREATE TABLE dim_soporte (
    id_soporte INT PRIMARY KEY,
    tipo_incidente VARCHAR(50),
    canal_contacto VARCHAR(30),
    resolucion VARCHAR(100),
    tiempo_respuesta INT,
    agente VARCHAR(50),
    satisfaccion VARCHAR(20),
    fecha_contacto DATE
);

CREATE TABLE dim_servicio (
    id_servicio INT PRIMARY KEY,
    tipo_servicio VARCHAR(30),
    descripcion VARCHAR(100),
    proveedor VARCHAR(50),
    tecnologia VARCHAR(20),
    limite_uso VARCHAR(50),
    tarifa_base DECIMAL(10,2),
    region_disponible VARCHAR(50)
);

CREATE TABLE dim_evento (
    id_evento INT PRIMARY KEY,
    tipo_evento VARCHAR(30),
    descripcion VARCHAR(100),
    canal VARCHAR(30),
    estado VARCHAR(20),
    fecha_evento DATE,
    responsable VARCHAR(50),
    observaciones VARCHAR(100)
);

-- =========================
-- 🟨 Tabla de hechos
-- =========================

CREATE TABLE hechos_telecom (
    id_cliente INT,
    id_plan INT,
    id_dispositivo INT,
    id_ubicacion INT,
    id_facturacion INT,
    id_promocion INT,
    id_fecha INT,
    id_soporte INT,
    id_servicio INT,
    id_evento INT,
    duracion_llamada DECIMAL(10,2),
    datos_consumidos_gb DECIMAL(10,2),
    minutos_usados INT,
    mensajes_enviados INT,
    costo_total DECIMAL(10,2),
    ancho_banda VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES dim_cliente(id_cliente),
    FOREIGN KEY (id_plan) REFERENCES dim_plan(id_plan),
    FOREIGN KEY (id_dispositivo) REFERENCES dim_dispositivo(id_dispositivo),
    FOREIGN KEY (id_ubicacion) REFERENCES dim_ubicacion(id_ubicacion),
    FOREIGN KEY (id_facturacion) REFERENCES dim_facturacion(id_facturacion),
    FOREIGN KEY (id_promocion) REFERENCES dim_promocion(id_promocion),
    FOREIGN KEY (id_fecha) REFERENCES dim_fecha(id_fecha),
    FOREIGN KEY (id_soporte) REFERENCES dim_soporte(id_soporte),
    FOREIGN KEY (id_servicio) REFERENCES dim_servicio(id_servicio),
    FOREIGN KEY (id_evento) REFERENCES dim_evento(id_evento)
);

select * from dim_cliente

DROP TABLE hechos_telecom;
DROP TABLE dim_cliente;
DROP TABLE dim_plan;
DROP TABLE dim_dispositivo;
DROP TABLE dim_ubicacion;
DROP TABLE dim_facturacion;
DROP TABLE dim_promocion;
DROP TABLE dim_fecha;
DROP TABLE dim_soporte;
DROP TABLE dim_servicio;
DROP TABLE dim_evento;



