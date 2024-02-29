/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE IF NOT EXISTS `population` (
  `PopulationCode` varchar(255) NOT NULL,
  `PopulationName` varchar(255) DEFAULT NULL,
  `SuperpopulationCode` varchar(50) DEFAULT NULL,
  `SuperpopulationName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PopulationCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `population` (`PopulationCode`, `PopulationName`, `SuperpopulationCode`, `SuperpopulationName`) VALUES
	('', 'Balochi', '', 'Central South Asia (HGDP)'),
	('ACB', 'African Caribbean', 'AFR', 'African Ancestry'),
	('ASW', 'African Ancestry SW', 'AFR', 'African Ancestry'),
	('BEB', 'Bengali', 'SAS', 'South Asian Ancestry'),
	('CDX', 'Dai Chinese', 'EAS', 'East Asian Ancestry'),
	('CEU', 'CEPH', 'EUR', 'European Ancestry'),
	('CHB', 'Han Chinese', 'EAS', 'East Asian Ancestry'),
	('CHS', 'Southern Han Chinese', 'EAS', 'East Asian Ancestry'),
	('CLM', 'Colombian', 'AMR', 'American Ancestry'),
	('ESN', 'Esan', 'AFR', 'African Ancestry'),
	('FIN', 'Finnish', 'EUR', 'European Ancestry'),
	('GBR', 'British', 'EUR', 'European Ancestry'),
	('GIH', 'Gujarati', 'SAS', 'South Asian Ancestry'),
	('GWD', 'Gambian Mandinka', 'AFR', 'African Ancestry'),
	('GWF', 'Gambian Fula', 'AFR', 'African Ancestry'),
	('GWJ', 'Gambian Jola', 'AFR', 'African Ancestry'),
	('GWW', 'Gambian Wolof', 'AFR', 'African Ancestry'),
	('IBS', 'Iberian', 'EUR', 'European Ancestry'),
	('ITU', 'Telugu', 'SAS', 'South Asian Ancestry'),
	('JPT', 'Japanese', 'EAS', 'East Asian Ancestry'),
	('KHV', 'Kinh Vietnamese', 'EAS', 'East Asian Ancestry'),
	('LWK', 'Luhya', 'AFR', 'African Ancestry'),
	('MKK', 'Masai', '', 'Africa (SGDP)'),
	('MSL', 'Mende', 'AFR', 'African Ancestry'),
	('MXL', 'Mexican Ancestry', 'AMR', 'American Ancestry'),
	('PEL', 'Peruvian', 'AMR', 'American Ancestry'),
	('PJL', 'Punjabi', 'SAS', 'South Asian Ancestry'),
	('PUR', 'Puerto Rican', 'AMR', 'American Ancestry'),
	('SIB', 'Siberian', NULL, NULL),
	('STU', 'Tamil', 'SAS', 'South Asian Ancestry'),
	('TSI', 'Toscani', 'EUR', 'European Ancestry'),
	('YRI', 'Yoruba', 'AFR', 'African Ancestry');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
