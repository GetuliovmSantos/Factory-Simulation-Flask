-- MySQL Script generated by MySQL Workbench
-- Tue Oct 22 08:30:34 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Fabrica
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Fabrica` ;

-- -----------------------------------------------------
-- Schema Fabrica
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Fabrica` DEFAULT CHARACTER SET utf8 ;
USE `Fabrica` ;

-- -----------------------------------------------------
-- Table `Fabrica`.`produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Fabrica`.`produtos` (
  `idprodutos` INT NOT NULL,
  `nomeProduto` VARCHAR(45) NULL,
  `quantidade` INT NULL,
  `lote` INT NULL,
  `dataValidade` DATE NULL,
  `area` CHAR(1) NULL,
  PRIMARY KEY (`idprodutos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Fabrica`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Fabrica`.`usuarios` (
  `idUsuarios` INT NOT NULL,
  `nomeUsuario` VARCHAR(45) NULL,
  `funcao` ENUM("lojista", "Gerente") NULL,
  `senha` CHAR(6) NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Fabrica`.`vendas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Fabrica`.`vendas` (
  `idvendas` INT NOT NULL AUTO_INCREMENT,
  `data_hora` DATETIME NULL,
  `quantidade` INT NULL,
  `destino` VARCHAR(45) NULL,
  `idprodutos` INT NOT NULL,
  PRIMARY KEY (`idvendas`),
    FOREIGN KEY (`idprodutos`)
    REFERENCES `Fabrica`.`produtos` (`idprodutos`)
    )
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
