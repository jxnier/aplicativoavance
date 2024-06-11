-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-04-2024 a las 05:16:00
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `avance_personal`
--

CREATE TABLE `avance_personal` (
  `id_avance` int(11) NOT NULL,
  `correo_institucional` varchar(50) NOT NULL,
  `contenido` text NOT NULL,
  `fecha_avance` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `avance_personal`
--

INSERT INTO `avance_personal` (`id_avance`, `correo_institucional`, `contenido`, `fecha_avance`) VALUES
(1, 'paci', 'bonito dia el de hoy', '2024-04-17 14:41:56'),
(2, 'aisabelgomez@unibarranquilla.edu.co', 'hoy hice un taller de gilberto, q bien xD', '2024-04-17 15:59:39'),
(3, 'marga@unibarranquilla.edu.co', 'Hoy me senti un poco cansada, por mis trabajos ', '2024-04-17 18:03:50'),
(4, 'marga@unibarranquilla.edu.co', 'siento que perdi un examen ', '2024-04-17 18:04:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id_paciente` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `correo_institucional` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `tipo_documento` enum('CC','TI') NOT NULL,
  `identificacion` int(13) NOT NULL,
  `telefono` int(15) DEFAULT NULL,
  `prediccion_ia` varchar(50) DEFAULT NULL,
  `historial_clinico` mediumblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`id_paciente`, `nombre`, `correo_institucional`, `contraseña`, `tipo_documento`, `identificacion`, `telefono`, `prediccion_ia`, `historial_clinico`) VALUES
(1, 'paci', 'paci', 'paci', 'CC', 321, NULL, 'Depression', NULL),
(12, 'Juan Pérez', 'juan.perez@unibarranquilla.edu.co', 'password123', 'CC', 1022334455, 2147483647, NULL, NULL),
(13, 'María González', 'maria.gonzalez@unibarranquilla.edu.co', 'pass1234', 'TI', 1234567890, 2147483647, NULL, NULL),
(14, 'Pedro Sánchez', 'pedro.sanchez@unibarranquilla.edu.co', '12345pass', 'CC', 1345678901, 2147483647, NULL, NULL),
(15, 'Laura Martínez', 'laura.martinez@unibarranquilla.edu.co', 'password12345', 'TI', 1456789012, 2147483647, NULL, NULL),
(16, 'Andrés López', 'andres.lopez@unibarranquilla.edu.co', 'securepass', 'CC', 1567890123, 2147483647, NULL, NULL),
(17, 'Sofía Ramírez', 'sofia.ramirez@unibarranquilla.edu.co', 'pass123456', 'TI', 1678901234, 2147483647, NULL, NULL),
(18, 'Carlos Rodríguez', 'carlos.rodriguez@unibarranquilla.edu.co', '123456pass', 'CC', 789012345, 2147483647, NULL, NULL),
(19, 'Ana Gómez', 'ana.gomez@unibarranquilla.edu.co', 'password1234567', 'TI', 1045123456, 2147483647, NULL, NULL),
(20, 'Diego Hernández', 'diego.hernandez@unibarranquilla.edu.co', 'pass12345678', 'CC', 7420707, 2147483647, NULL, NULL),
(21, 'Gabriela Martínez', 'gabriela.martinez@unibarranquilla.edu.co', '12345678pass', 'TI', 1012345678, 2147483647, NULL, NULL),
(22, 'Andrea Isabel Gómez Núñez', 'aisabelgomez@unibarranquilla.edu.co', '1044610671Aign*', 'CC', 1044610671, NULL, 'Bipolar Type-2', NULL),
(23, 'margarita ', 'marga@unibarranquilla.edu.co', '10445Jo*', 'TI', 2147483647, NULL, 'Bipolar Type-2', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `psicologo`
--

CREATE TABLE `psicologo` (
  `id_psicologo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `correo_institucional` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `identificacion` int(13) NOT NULL,
  `telefono` bigint(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `psicologo`
--

INSERT INTO `psicologo` (`id_psicologo`, `nombre`, `correo_institucional`, `contraseña`, `identificacion`, `telefono`) VALUES
(1, 'psico', 'psico', 'psico', 123, 123),
(2, 'Diana Ramírez', 'diana.ramirez@unibarranquilla.edu.co', 'password123', 1122334455, 3016899959),
(3, 'Juan Pérez', 'juan.perez@unibarranquilla.edu.co', 'securepass', 1988776655, 3006481091),
(4, 'María González', 'maria.gonzalez@unibarranquilla.edu.co', 'pass1234', 1344556677, 3045986232),
(5, 'Pedro Sánchez', 'pedro.sanchez@unibarranquilla.edu.co', '12345pass', 1566778899, 3008084520),
(6, 'Laura Martínez', 'laura.martinez@unibarranquilla.edu.co', 'password12345', 1899001122, 3012759088),
(7, 'pablo', 'pabloloco@unibarranquilla.edu.co', '10445Jo*', 1044619277, NULL),
(8, 'Pablo Cuesta Novoa', 'pablocuesta@unibarranquilla.edu.co', '1044619278Jo*', 2147483647, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicacion`
--

CREATE TABLE `publicacion` (
  `id_publicacion` int(1) NOT NULL,
  `id_psicologo` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `contenido` text NOT NULL,
  `fecha_publicacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `tipo` enum('evento','anuncio','consejo','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `publicacion`
--

INSERT INTO `publicacion` (`id_publicacion`, `id_psicologo`, `titulo`, `contenido`, `fecha_publicacion`, `tipo`) VALUES
(1, 1, 'Evento jovenes primer ingreso', 'Dia 20 de abril 2024 \nlugar auditorio sede Barranquilla-Plaza de la paz', '2024-04-17 19:27:14', 'evento'),
(2, 1, 'Sesión de orientación académica', '¡No te pierdas nuestra sesión de orientación académica para nuevos estudiantes!', '2024-04-17 20:23:20', 'evento'),
(3, 2, 'Charla sobre salud mental', 'Te invitamos a una charla informativa sobre cuidado de la salud mental.', '2024-04-17 20:23:20', 'evento'),
(4, 3, 'Taller de habilidades de estudio', 'Participa en nuestro taller práctico para mejorar tus habilidades de estudio.', '2024-04-17 20:23:20', 'evento'),
(5, 4, 'Feria de emprendimiento', '¡Descubre nuevas oportunidades en nuestra feria de emprendimiento!', '2024-04-17 20:23:20', 'evento'),
(6, 5, 'Concierto benéfico', 'Asiste a nuestro concierto benéfico para recaudar fondos para proyectos sociales.', '2024-04-17 20:23:20', 'evento'),
(7, 1, 'Consejo de estudio', 'Organiza tu tiempo y establece metas alcanzables para mejorar tu rendimiento académico.', '2024-04-17 20:23:20', 'consejo'),
(8, 2, 'Consejo de bienestar', 'Cuida tu salud física y mental realizando ejercicio regularmente y practicando técnicas de relajación.', '2024-04-17 20:23:20', 'consejo'),
(9, 3, 'Consejo de alimentación', 'Mantén una dieta balanceada y evita la comida chatarra para tener más energía y concentración.', '2024-04-17 20:23:20', 'consejo'),
(10, 4, 'Consejo de planificación financiera', 'Haz un presupuesto mensual y ahorra parte de tus ingresos para imprevistos o futuros proyectos.', '2024-04-17 20:23:20', 'consejo'),
(11, 5, 'Consejo de networking', 'Construye una red de contactos profesionales participando en eventos y actividades extracurriculares.', '2024-04-17 20:23:20', 'consejo'),
(12, 1, '¡Matrículas abiertas!', 'Inicia tu proceso de matrícula para el próximo semestre y asegura tu cupo en nuestros programas académicos.', '2024-04-17 20:23:20', 'anuncio'),
(13, 2, 'Oferta laboral', 'Empresa X busca estudiantes para prácticas profesionales remuneradas en el área de marketing digital.', '2024-04-17 20:23:20', 'anuncio'),
(14, 3, 'Convocatoria de becas', 'Consulta nuestra convocatoria de becas para estudios de pregrado y posgrado en el exterior.', '2024-04-17 20:23:20', 'anuncio'),
(15, 4, 'Horario de atención', 'Recordamos a nuestros estudiantes que la oficina de atención al estudiante estará abierta de lunes a viernes de 8:00 a.m. a 5:00 p.m.', '2024-04-17 20:23:20', 'anuncio'),
(16, 5, 'Encuesta de satisfacción', 'Participa en nuestra encuesta para conocer tu opinión sobre nuestros servicios y mejorar tu experiencia universitaria.', '2024-04-17 20:23:20', 'anuncio'),
(17, 8, 'Primer Ingreso Informacion', 'Sede plaza de la paz \nAuditorio \n6 pm\n17-05-2024', '2024-04-17 23:01:40', 'evento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarea`
--

CREATE TABLE `tarea` (
  `id_tarea` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `id_psicologo` int(11) NOT NULL,
  `titulo` varchar(25) NOT NULL,
  `descripcion` text NOT NULL,
  `completada` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tarea`
--

INSERT INTO `tarea` (`id_tarea`, `id_paciente`, `id_psicologo`, `titulo`, `descripcion`, `completada`) VALUES
(1, 1, 1, 'traer lapiz ', 'TRAIGA', 0),
(2, 22, 1, 'TRAER LAPIZ Y COLORES ', 'proxima cita', 1),
(3, 13, 8, 'Traer historial clinico ', 'Proximo cita traer historial clinico ', 0),
(4, 23, 1, 'Traer historial clinico ', 'prueba de tareas ', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `avance_personal`
--
ALTER TABLE `avance_personal`
  ADD PRIMARY KEY (`id_avance`),
  ADD KEY `correo_institucional` (`correo_institucional`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id_paciente`,`correo_institucional`),
  ADD UNIQUE KEY `identificacion` (`identificacion`),
  ADD UNIQUE KEY `correo_institucional` (`correo_institucional`),
  ADD KEY `correo_institucional_2` (`correo_institucional`);

--
-- Indices de la tabla `psicologo`
--
ALTER TABLE `psicologo`
  ADD PRIMARY KEY (`id_psicologo`,`correo_institucional`),
  ADD UNIQUE KEY `identificacion` (`identificacion`);

--
-- Indices de la tabla `publicacion`
--
ALTER TABLE `publicacion`
  ADD PRIMARY KEY (`id_publicacion`),
  ADD KEY `id_psicologo` (`id_psicologo`);

--
-- Indices de la tabla `tarea`
--
ALTER TABLE `tarea`
  ADD PRIMARY KEY (`id_tarea`),
  ADD KEY `id_paciente` (`id_paciente`,`id_psicologo`),
  ADD KEY `id_psicologo` (`id_psicologo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `avance_personal`
--
ALTER TABLE `avance_personal`
  MODIFY `id_avance` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id_paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `psicologo`
--
ALTER TABLE `psicologo`
  MODIFY `id_psicologo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `publicacion`
--
ALTER TABLE `publicacion`
  MODIFY `id_publicacion` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `tarea`
--
ALTER TABLE `tarea`
  MODIFY `id_tarea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `avance_personal`
--
ALTER TABLE `avance_personal`
  ADD CONSTRAINT `avance_personal_ibfk_1` FOREIGN KEY (`correo_institucional`) REFERENCES `paciente` (`correo_institucional`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `publicacion`
--
ALTER TABLE `publicacion`
  ADD CONSTRAINT `publicacion_ibfk_1` FOREIGN KEY (`id_psicologo`) REFERENCES `psicologo` (`id_psicologo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tarea`
--
ALTER TABLE `tarea`
  ADD CONSTRAINT `tarea_ibfk_2` FOREIGN KEY (`id_psicologo`) REFERENCES `psicologo` (`id_psicologo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tarea_ibfk_3` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
