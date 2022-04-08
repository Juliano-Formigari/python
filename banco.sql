-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 08-Abr-2022 às 02:41
-- Versão do servidor: 8.0.27
-- versão do PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banco`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `conta_corrente`
--

CREATE TABLE `conta_corrente` (
  `id_conta_corrente` int NOT NULL,
  `numero_conta_corrente` varchar(5) NOT NULL,
  `saldo_conta_corrente` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `conta_poupanca`
--

CREATE TABLE `conta_poupanca` (
  `id_conta_poupanca` int NOT NULL,
  `numero_conta_poupanca` varchar(5) NOT NULL,
  `saldo_conta_poupanca` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `conta_salario`
--

CREATE TABLE `conta_salario` (
  `id_conta_salario` int NOT NULL,
  `numero_conta_salario` varchar(5) NOT NULL,
  `saldo_conta_salario` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `conta_corrente`
--
ALTER TABLE `conta_corrente`
  ADD PRIMARY KEY (`id_conta_corrente`);

--
-- Índices para tabela `conta_poupanca`
--
ALTER TABLE `conta_poupanca`
  ADD PRIMARY KEY (`id_conta_poupanca`);

--
-- Índices para tabela `conta_salario`
--
ALTER TABLE `conta_salario`
  ADD PRIMARY KEY (`id_conta_salario`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `conta_corrente`
--
ALTER TABLE `conta_corrente`
  MODIFY `id_conta_corrente` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `conta_poupanca`
--
ALTER TABLE `conta_poupanca`
  MODIFY `id_conta_poupanca` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `conta_salario`
--
ALTER TABLE `conta_salario`
  MODIFY `id_conta_salario` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
