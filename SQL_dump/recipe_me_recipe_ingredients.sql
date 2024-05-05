-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recipe_me
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipe_ingredients`
--

DROP TABLE IF EXISTS `recipe_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_ingredients` (
  `quantity` varchar(45) NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  `calling_recipe` int unsigned NOT NULL,
  `called_ingredient` int unsigned NOT NULL,
  PRIMARY KEY (`calling_recipe`,`called_ingredient`),
  KEY `called_ingredient` (`called_ingredient`),
  CONSTRAINT `recipe_ingredients_ibfk_1` FOREIGN KEY (`calling_recipe`) REFERENCES `recipe` (`recipe_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `recipe_ingredients_ibfk_2` FOREIGN KEY (`called_ingredient`) REFERENCES `ingredient` (`ingredient_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_ingredients`
--

LOCK TABLES `recipe_ingredients` WRITE;
/*!40000 ALTER TABLE `recipe_ingredients` DISABLE KEYS */;
INSERT INTO `recipe_ingredients` VALUES ('8 ounces','',8,11),('3 bunches',' trimmed',8,12),('4 (4 ounce) links',' cut into 1 inch pieces',8,13),('1 tablespoon','',8,14),('2',' chopped',8,15),('1 (14.5 ounce) can','',8,16),('N/A','',8,17),('½ cup','',8,18),('¼ teaspoon','',8,19),('1 teaspoon',' or to taste',8,20),('1 cup','',9,18),('1 (16 ounce) package','',9,21),('1 tablespoon','',9,22),('½ tablespoon','',9,23),('1',' thinly sliced',9,24),('1 teaspoon','',9,25),('1 pound','',9,26),('1 (14.5 ounce) can','',9,27),('1 cup','',9,28),('1 tablespoon','',9,29),('1 (8 ounce) box','',10,30),('¼ cup','',10,31),('¼ cup','',10,32),('½ teaspoon','',10,33),('N/A','',10,34),('2 cups','',10,35),('2 cups','',10,36),('1 tablespoon','',11,25),('2 tablespoons','',11,37),('½ cup','',11,38),('1 tablespoon','',11,39),('2 tablespoons','',11,40),('1 (13.5 ounce) can',' well-shaken (such as Thai Kitchen)',11,41),('1 cup','',11,42),('½ teaspoon','',11,43),('2 (15 ounce) cans',' rinsed and drained',11,44),('3 cups','',11,45),('1 tablespoon','',11,46),('½ cup','',11,47),('N/A','',11,48),('2 cups','',11,49),('1/4 cup','',12,50),('1 tablespoon','',12,51),('1 tablespoon','',12,52),('1 teaspoon','',12,53),('1 pound',' cut into 1-inch pieces',12,54);
/*!40000 ALTER TABLE `recipe_ingredients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-05 10:39:20
