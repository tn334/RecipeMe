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
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `ingredient_id` int unsigned NOT NULL AUTO_INCREMENT,
  `ingredient_name` varchar(90) NOT NULL,
  PRIMARY KEY (`ingredient_id`),
  UNIQUE KEY `ingredient_id_UNIQUE` (`ingredient_id`),
  UNIQUE KEY `ingredient_name_UNIQUE` (`ingredient_name`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (32,'all-purpose flour'),(45,'baby spinach leaves'),(12,'broccoli rabe'),(26,'bulk Italian sausage'),(31,'butter'),(44,'chickpeas'),(29,'chopped fresh parsley'),(38,'chopped yellow onion'),(47,'coarsely chopped toasted cashews'),(49,'cooked rice'),(50,'cornstarch'),(19,'crushed red pepper flakes'),(16,'diced tomatoes'),(30,'elbow macaroni'),(23,'finely minced onion'),(48,'fresh cilantro for garnish'),(46,'fresh lime juice'),(15,'garlic cloves'),(37,'grapeseed oil'),(39,'grated fresh ginger'),(18,'grated Parmesan cheese'),(53,'ground black pepper'),(34,'ground black pepper to taste'),(28,'heavy cream'),(13,'hot Italian sausage'),(43,'kosher salt'),(35,'milk'),(25,'minced garlic'),(20,'olive oil'),(24,'orange bell pepper'),(51,'reduced-sodium soy sauce'),(33,'salt'),(17,'salt and ground black pepper to taste'),(14,'sausage drippings'),(36,'shredded Cheddar cheese'),(54,'skinless boneless chicken thighs'),(27,'stewed tomatoes'),(40,'Thai red curry paste'),(21,'uncooked pasta shells'),(41,'unsweetened coconut milk'),(42,'vegetable broth'),(22,'vegetable oil'),(11,'whole wheat rotini pasta'),(52,'wine');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
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
