-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 05-Jan-2018 às 14:49
-- Versão do servidor: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banco`
--
CREATE DATABASE banco;
USE banco;
-- --------------------------------------------------------

--
-- Estrutura da tabela `teste`
--

CREATE TABLE `teste` (
  `id` int(45) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `num` int(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `teste`
--

INSERT INTO `teste` (`id`, `nome`, `num`) VALUES
(1, 'luffy', 1),
(2, 'meliodas', 1),
(3, 'aaaa', 2),
(4, 'asta', 3),
(5, 'alan', 4),
(6, 'anta', 5),
(7, 'alberto', 1),
(8, 'adolfo', 7),
(9, 'alvoro', 8),
(10, 'emilia', 2),
(11, 'nami', 3),
(12, 'hatsune miku', 4),
(13, 'ban', 2),
(14, 'diane', 13),
(15, 'subaru', 3),
(16, 'souta', 15),
(17, 'alexandre', 16),
(18, 'meliodafuu', 2),
(19, 'kaido', 18),
(20, 'kaneki', 19),
(21, 'yukihira soma', 6),
(22, 'asasas', 21),
(23, 'nanbaka', 4),
(24, 'bhda', 5),
(25, 'h\\jza', 24),
(26, 'awpod', 25),
(27, 'a', 26),
(28, 'a', 27),
(29, 'a', 28),
(30, 'a', 29),
(31, 'a', 30),
(32, 'a', 31),
(33, 'a', 32),
(34, 'a', 33),
(35, 'a', 34),
(36, 'a', 35),
(37, 'a', 36),
(38, 'a', 37),
(39, 'a', 38),
(40, 'a', 39),
(41, 'a', 40),
(42, 'a', 41),
(43, 'a', 42),
(44, 'a', 43),
(45, 'a', 44),
(46, 'a', 45),
(47, 'a', 46),
(48, 'a', 47),
(49, 'a', 48),
(50, 'a', 49),
(51, 'a', 50),
(52, 'a', 51),
(53, 'a', 52),
(54, 'a', 53),
(55, 'a', 54),
(56, 'a', 55),
(57, 'a', 56),
(58, 'a', 57),
(59, 'a', 58),
(60, 'a', 59),
(61, 'a', 60),
(62, 'a', 61),
(63, 'a', 62);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `teste`
--
ALTER TABLE `teste`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `teste`
--
ALTER TABLE `teste`
  MODIFY `id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
