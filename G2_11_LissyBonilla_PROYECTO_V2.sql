-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2021 a las 02:44:30
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
-- Base de datos: `db_sistema`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_cuenta_ahorro`
--

CREATE TABLE `tbl_cuenta_ahorro` (
  `N_CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(20) NOT NULL,
  `APELLIDO` varchar(20) NOT NULL,
  `MONTO` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_depositos`
--

CREATE TABLE `tbl_depositos` (
  `N_CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(20) NOT NULL,
  `APELLIDO` varchar(20) NOT NULL,
  `MONTO` int(10) NOT NULL,
  `MONTO_DEPOSITAR` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_prestamo`
--

CREATE TABLE `tbl_prestamo` (
  `N_CUENTA` int(11) NOT NULL,
  `NOMBRE` varchar(20) NOT NULL,
  `APELLIDO` varchar(20) NOT NULL,
  `MONTO` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `N_CUENTA` int(11) NOT NULL,
  `EDAD` int(5) NOT NULL,
  `NOMBRE_APELLIDO` varchar(50) NOT NULL,
  `CONTRASENA` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_cuenta_ahorro`
--
ALTER TABLE `tbl_cuenta_ahorro`
  ADD KEY `FK_USUARIOS_CUENTA` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_depositos`
--
ALTER TABLE `tbl_depositos`
  ADD KEY `FK_USUARIOS_DEPOSITO` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  ADD KEY `FK_USUARIOS_PRESTAMO` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`N_CUENTA`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `N_CUENTA` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_cuenta_ahorro`
--
ALTER TABLE `tbl_cuenta_ahorro`
  ADD CONSTRAINT `FK_USUARIOS_CUENTA` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_depositos`
--
ALTER TABLE `tbl_depositos`
  ADD CONSTRAINT `FK_USUARIOS_DEPOSITO` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  ADD CONSTRAINT `FK_USUARIOS_PRESTAMO` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
