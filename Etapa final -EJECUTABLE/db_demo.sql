-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-08-2021 a las 06:42:48
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_demo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_ahorro`
--

CREATE TABLE `tbl_ahorro` (
  `CUENTA` int(15) NOT NULL,
  `NOMBRE` varchar(200) NOT NULL,
  `MONTO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_deposito`
--

CREATE TABLE `tbl_deposito` (
  `CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(200) NOT NULL,
  `MONTO` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_prestamo`
--

CREATE TABLE `tbl_prestamo` (
  `CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(200) NOT NULL,
  `MONTO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(255) NOT NULL,
  `CONTRASENA` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_usuarios`
--

INSERT INTO `tbl_usuarios` (`CUENTA`, `NOMBRE`, `CONTRASENA`) VALUES
(1, 'María José López', '900'),
(458, 'Malcoln Francisco López', '100'),
(500, 'Lennyn Sánchez', '300'),
(12312, 'DADAD', '123123'),
(55500, 'Antonio Melgar', '600'),
(78920, 'Mauricio José López', '700');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_ahorro`
--
ALTER TABLE `tbl_ahorro`
  ADD PRIMARY KEY (`CUENTA`);

--
-- Indices de la tabla `tbl_deposito`
--
ALTER TABLE `tbl_deposito`
  ADD PRIMARY KEY (`CUENTA`);

--
-- Indices de la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  ADD PRIMARY KEY (`CUENTA`);

--
-- Indices de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`CUENTA`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_ahorro`
--
ALTER TABLE `tbl_ahorro`
  MODIFY `CUENTA` int(15) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_deposito`
--
ALTER TABLE `tbl_deposito`
  MODIFY `CUENTA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  MODIFY `CUENTA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `CUENTA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
