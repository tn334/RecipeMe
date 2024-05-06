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
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `recipe_id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(750) DEFAULT NULL,
  `origin_url` varchar(150) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `steps` text NOT NULL,
  PRIMARY KEY (`recipe_id`),
  UNIQUE KEY `recipe_id_UNIQUE` (`recipe_id`),
  UNIQUE KEY `origin_UNIQUE` (`origin_url`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (8,'Spicy Sausage Broccoli Rabe Parmesan','Simple, quick, inexpensive, and a little spicy. Delicious!!!\n Prep time: 10 mins\n Active time: \n Cook time: 20 mins\n Yield: 4 servings','https://www.allrecipes.com/recipe/218054/spicy-sausage-broccoli-rabe-parmesan/','DMarie','Step 1: Fill a large pot with lightly salted water and bring to a rolling boil over high heat. Once the water is boiling, stir in the rotini, and return to a boil. Cook uncovered, stirring occasionally, until the pasta has cooked through, but is still firm to the bite, about 6 minutes. Drain well in a colander set in the sink.\nStep 2: While the pasta is cooking, place a steamer insert into a saucepan, and fill with water to just below the bottom of the steamer. Cover, and bring the water to a boil over high heat. Add the broccoli rabe, recover, and steam until just tender, about 2 minutes depending on thickness.\nStep 3: At the same time, place the Italian sausage into a large skillet over medium heat, and cook until browned and no longer pink inside, about 5 minutes. Remove sausage from pan and set aside; drain excess grease, leaving about 1 tablespoon of sausage drippings in the pan. Sprinkle in the garlic, and cook until it starts to brown, about 1 minute.\nStep 4: Stir in 1/2 of the broccoli rabe. Cook and stir until the rabe has wilted, then add remaining rabe and diced tomatoes. Cook until rabe is tender, about 5 minutes; sprinkle with salt and black pepper.\nStep 5: Return sausage to the skillet, and cook just until the meat is hot; sprinkle with Parmesan cheese, crushed red pepper flakes, and a drizzle of olive oil. Serve over hot rotini.\n'),(9,'Cheesy Sausage Pasta','This delicious cheesy sausage pasta dish has a tomato cream sauce. It\'s like macaroni for grown-ups!\n Prep time: 10 mins\n Active time: \n Cook time: 25 mins\n Yield: ','https://www.allrecipes.com/recipe/188824/cheesy-sausage-pasta/','DoughertyDA','Step 1: Fill a large pot with lightly salted water and bring to a rolling boil over high heat. Stir in pasta and return to a boil. Cook, stirring occasionally, until cooked through but still firm to the bite, about 13 minutes; drain.\nStep 2: Meanwhile, heat vegetable oil in a large skillet over medium-high heat. Add onion, orange pepper, and garlic; cook and stir until tender, about 5 minutes. Stir in Italian sausage; cook and stir until browned and cooked through, about 8 minutes. Stir in undrained tomatoes and heavy cream; reduce heat to medium-low and cook 5 minutes more.\nStep 3: Mix pasta into sauce; stir in the Parmesan cheese and garnish with fresh parsley.\n'),(10,'Simple Macaroni and Cheese','Quick, easy, and tasty macaroni and cheese dish. Fancy, designer mac and cheese often costs forty or fifty dollars to prepare when you have so many expensive cheeses, but they aren\'t always the best tasting. This simple recipe is cheap and tasty.\n Prep time: 10 mins\n Active time: \n Cook time: 15 mins\n Yield: 4 servings','https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/','g0dluvsugly','Step 1: Bring a large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally until cooked through but firm to the bite, 8 minutes.\nStep 2: At the same time, melt butter in a saucepan over medium heat.\nStep 3: Add flour, salt, and pepper and stir until smooth, about 5 minutes.\nStep 4: Pour in milk slowly, while stirring continuously. Continue to cook and stir until mixture is smooth and bubbling, about 5 minutes, making sure the milk doesn\'t burn.\nStep 5: Add Cheddar cheese and stir until melted, 2 to 4 minutes.\nStep 6: Drain macaroni and fold into cheese sauce until coated.\nStep 7: Serve hot and enjoy!\n'),(11,'Coconut Chickpea Curry','A delicious vegetarian curry that is spicy, but savory and delightful in all the best ways. You can adjust the amount of curry paste to your personal paste.\n Prep time: \n Active time: 15 mins\n Cook time: 20 mins\n Yield: ','https://www.allrecipes.com/recipe/8527854/coconut-chickpea-curry/','Julia Levy','Step 1: Heat oil in a large high-sided skillet over medium. Add onion and cook, stirring often, until softened, about 4 minutes. Add garlic and ginger; cook, stirring constantly, until fragrant, about 1 minute.\nStep 2: Add red curry paste and cook, stirring constantly, until lightly darkened and vegetables are coated, about 1 minute.\nStep 3: Stir in coconut milk, broth, and salt; bring to a boil over medium-high. Stir in chickpeas.\nStep 4: Reduce heat to medium to maintain a simmer and simmer, stirring occasionally, until thickened slightly, 15 to 20 minutes.\nStep 5: Remove from heat and stir in spinach; stir until wilted, about 1 minute. Stir in lime juice. Serve with cashews, cilantro, and rice.\n'),(12,'Black Pepper Chicken','This black pepper chicken tastes just like the Chinese takeout favorite, golden-fried chicken in a soy, wine, and black pepper sauce, and served over white rice.\n Prep time: 15 mins\n Active time: \n Cook time: 15 mins\n Yield: ','https://www.allrecipes.com/black-pepper-chicken-recipe-8382732','Barrett Heald','Step 1: Gather Ingredients.\nStep 2: For Chicken Coating, whisk together cornstarch, soy sauce, Shaoxing wine, and pepper in a large bowl. Mixture will be quite thick. Add chicken pieces to bowl; stir to coat chicken. Let stand at room temperature for 15 minutes.\nStep 3: Meanwhile, for Black Pepper Sauce, whisk together chicken broth, oyster sauce, Shaoxing wine, soy sauce, water, cornstarch, and pepper in a medium bowl.\nStep 4: Heat 2 tablespoons vegetable oil in a 12-inch skillet over medium-high heat. Add half the chicken. Cook and stir until lightly browned and no longer pink, about 5 minutes. Transfer chicken to a plate; set aside. Repeat with remaining chicken. Remove chicken from skillet.\nStep 5: Add remaining 1 tablespoon vegetable oil to skillet. Stir in minced garlic and ginger. Cook and stir until fragrant, about 30 seconds. Stir in bell pepper and onion. Cook and stir until crisp-tender, 2 to 3 minutes.\nStep 6: Pour in Black Pepper Sauce and cook until sauce has thickened, 2 to 3 minutes. Return cooked chicken to skillet. Cook and stir until all ingredients are coated with sauce. Serve immediately over cooked white rice.\n');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
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
