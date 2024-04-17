-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-04-2024 a las 19:09:55
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cita`
--

CREATE TABLE `cita` (
  `id_cita` int(11) NOT NULL,
  `id_psicologo` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `sede` enum('soledad','barranquilla-paz') NOT NULL,
  `estado` enum('disponible','agendada','finalizada') NOT NULL DEFAULT 'disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cita`
--

INSERT INTO `cita` (`id_cita`, `id_psicologo`, `id_paciente`, `fecha`, `hora`, `sede`, `estado`) VALUES
(1, 1, NULL, '2024-04-26', '14:00:00', 'soledad', 'disponible'),
(2, 1, NULL, '2024-04-27', '08:00:00', 'barranquilla-paz', 'disponible'),
(3, 1, NULL, '2024-04-17', '15:00:00', 'soledad', 'disponible'),
(4, 1, NULL, '2024-04-28', '15:00:00', 'soledad', 'disponible'),
(5, 1, NULL, '2024-04-27', '14:00:00', 'soledad', 'disponible'),
(6, 2, NULL, '2024-04-24', '08:00:00', 'barranquilla-paz', 'disponible'),
(7, 2, NULL, '2024-04-25', '15:00:00', 'soledad', 'disponible'),
(8, 2, NULL, '2024-04-25', '08:00:00', 'barranquilla-paz', 'disponible'),
(9, 2, NULL, '2024-04-21', '14:00:00', 'soledad', 'disponible'),
(10, 2, NULL, '2024-04-26', '08:00:00', 'soledad', 'disponible'),
(11, 4, NULL, '2024-04-28', '14:00:00', 'soledad', 'disponible'),
(12, 4, NULL, '2024-04-20', '08:00:00', 'barranquilla-paz', 'disponible'),
(13, 4, NULL, '2024-04-24', '08:00:00', 'barranquilla-paz', 'disponible'),
(14, 4, NULL, '2024-04-19', '08:00:00', 'soledad', 'disponible'),
(15, 4, NULL, '2024-04-22', '15:00:00', 'soledad', 'disponible'),
(16, 5, NULL, '2024-04-28', '09:00:00', 'barranquilla-paz', 'disponible'),
(17, 5, NULL, '2024-04-27', '10:00:00', 'soledad', 'disponible'),
(18, 5, NULL, '2024-04-25', '14:00:00', 'soledad', 'disponible'),
(19, 5, NULL, '2024-04-28', '17:00:00', 'soledad', 'disponible'),
(20, 5, NULL, '2024-04-17', '11:00:00', 'barranquilla-paz', 'disponible'),
(21, 6, NULL, '2024-04-17', '09:00:00', 'soledad', 'disponible'),
(22, 6, NULL, '2024-04-21', '10:00:00', 'soledad', 'disponible'),
(23, 6, NULL, '2024-04-21', '15:00:00', 'soledad', 'disponible'),
(24, 6, NULL, '2024-04-28', '14:00:00', 'soledad', 'disponible'),
(25, 6, NULL, '2024-04-21', '17:00:00', 'barranquilla-paz', 'disponible'),
(26, 3, NULL, '2024-04-18', '11:00:00', 'soledad', 'disponible'),
(27, 3, NULL, '2024-04-25', '09:00:00', 'barranquilla-paz', 'disponible'),
(28, 3, NULL, '2024-04-30', '08:00:00', 'soledad', 'disponible'),
(29, 3, NULL, '2024-04-25', '14:00:00', 'soledad', 'disponible'),
(30, 3, NULL, '2024-04-30', '10:00:00', 'barranquilla-paz', 'disponible');

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
(1, 'paci', 'paci', 'paci', 'CC', 321, NULL, 'Bipolar Type-2', NULL);

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
(6, 'Laura Martínez', 'laura.martinez@unibarranquilla.edu.co', 'password12345', 1899001122, 3012759088);

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
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `avance_personal`
--
ALTER TABLE `avance_personal`
  ADD PRIMARY KEY (`id_avance`),
  ADD KEY `correo_institucional` (`correo_institucional`);

--
-- Indices de la tabla `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`id_cita`),
  ADD KEY `id_psicologo` (`id_psicologo`),
  ADD KEY `id_paciente` (`id_paciente`);

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
  MODIFY `id_avance` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cita`
--
ALTER TABLE `cita`
  MODIFY `id_cita` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id_paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `psicologo`
--
ALTER TABLE `psicologo`
  MODIFY `id_psicologo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `publicacion`
--
ALTER TABLE `publicacion`
  MODIFY `id_publicacion` int(1) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tarea`
--
ALTER TABLE `tarea`
  MODIFY `id_tarea` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `avance_personal`
--
ALTER TABLE `avance_personal`
  ADD CONSTRAINT `avance_personal_ibfk_1` FOREIGN KEY (`correo_institucional`) REFERENCES `paciente` (`correo_institucional`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cita`
--
ALTER TABLE `cita`
  ADD CONSTRAINT `cita_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id_paciente`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cita_ibfk_2` FOREIGN KEY (`id_psicologo`) REFERENCES `psicologo` (`id_psicologo`) ON DELETE CASCADE ON UPDATE CASCADE;

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
