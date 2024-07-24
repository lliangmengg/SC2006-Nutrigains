-- MySQL dump 10.13  Distrib 8.3.0, for macos13.6 (arm64)
--
-- Host: localhost    Database: nutrigains
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Favourites`
--

DROP TABLE IF EXISTS `Favourites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Favourites` (
  `user_email` varchar(255) NOT NULL,
  `meal_id` int NOT NULL,
  PRIMARY KEY (`user_email`,`meal_id`),
  KEY `meal_id` (`meal_id`),
  CONSTRAINT `favourites_ibfk_1` FOREIGN KEY (`user_email`) REFERENCES `Users` (`email`),
  CONSTRAINT `favourites_ibfk_2` FOREIGN KEY (`meal_id`) REFERENCES `Meals` (`mealId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Favourites`
--

LOCK TABLES `Favourites` WRITE;
/*!40000 ALTER TABLE `Favourites` DISABLE KEYS */;
INSERT INTO `Favourites` VALUES ('ansh300304@gmail.com',640311),('ansh300304@gmail.com',654959),('ansh300304@gmail.com',663804);
/*!40000 ALTER TABLE `Favourites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MealHistory`
--

DROP TABLE IF EXISTS `MealHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MealHistory` (
  `user_email` varchar(255) NOT NULL,
  `date_time` datetime NOT NULL,
  `meal_id` int DEFAULT NULL,
  PRIMARY KEY (`user_email`,`date_time`),
  KEY `meal_id` (`meal_id`),
  CONSTRAINT `mealhistory_ibfk_1` FOREIGN KEY (`user_email`) REFERENCES `Users` (`email`),
  CONSTRAINT `mealhistory_ibfk_2` FOREIGN KEY (`meal_id`) REFERENCES `Meals` (`mealId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MealHistory`
--

LOCK TABLES `MealHistory` WRITE;
/*!40000 ALTER TABLE `MealHistory` DISABLE KEYS */;
INSERT INTO `MealHistory` VALUES ('ansh300304@gmail.com','2024-04-15 08:52:01',632821),('ansh300304@gmail.com','2024-04-08 12:40:00',635964),('ansh300304@gmail.com','2024-04-09 17:50:00',635964),('ansh300304@gmail.com','2024-04-11 06:53:00',635964),('ansh300304@gmail.com','2024-04-12 00:13:00',635964),('ansh300304@gmail.com','2024-04-14 09:03:00',635964),('ansh300304@gmail.com','2024-04-07 02:11:00',640311),('ansh300304@gmail.com','2024-04-08 21:37:00',640311),('ansh300304@gmail.com','2024-04-09 11:36:00',640311),('ansh300304@gmail.com','2024-04-05 23:47:00',643933),('ansh300304@gmail.com','2024-04-08 20:15:00',643933),('ansh300304@gmail.com','2024-04-09 06:31:00',643933),('ansh300304@gmail.com','2024-04-10 19:38:00',643933),('ansh300304@gmail.com','2024-04-11 22:24:00',643933),('ansh300304@gmail.com','2024-04-12 04:44:00',643933),('ansh300304@gmail.com','2024-04-13 08:58:00',643933),('ansh300304@gmail.com','2024-04-14 02:36:00',643933),('ansh300304@gmail.com','2024-04-15 07:45:41',643933),('ansh300304@gmail.com','2024-04-15 11:22:48',649343),('ansh300304@gmail.com','2024-04-05 07:04:00',654959),('ansh300304@gmail.com','2024-04-08 00:22:00',654959),('ansh300304@gmail.com','2024-04-09 01:49:00',654959),('ansh300304@gmail.com','2024-04-12 14:05:00',654959),('ansh300304@gmail.com','2024-04-08 01:13:00',663804),('ansh300304@gmail.com','2024-04-09 19:06:00',663804),('ansh300304@gmail.com','2024-04-10 21:09:00',663804),('ansh300304@gmail.com','2024-04-11 00:22:00',663804),('ansh300304@gmail.com','2024-04-12 21:13:00',663804),('ansh300304@gmail.com','2024-04-14 13:53:00',663804),('ansh300304@gmail.com','2024-04-15 07:45:25',663804),('ansh300304@gmail.com','2024-04-09 21:28:00',715491),('ansh300304@gmail.com','2024-04-13 15:52:00',715491),('ansh300304@gmail.com','2024-04-06 23:43:00',1697759),('ansh300304@gmail.com','2024-04-08 18:49:00',1697759);
/*!40000 ALTER TABLE `MealHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Meals`
--

DROP TABLE IF EXISTS `Meals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Meals` (
  `mealId` int NOT NULL,
  `mealName` varchar(255) DEFAULT NULL,
  `calories` float DEFAULT NULL,
  `carbs` float DEFAULT NULL,
  `proteins` float DEFAULT NULL,
  `fats` float DEFAULT NULL,
  `ingredients` text,
  `recipeInstructions` text,
  `img_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mealId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Meals`
--

LOCK TABLES `Meals` WRITE;
/*!40000 ALTER TABLE `Meals` DISABLE KEYS */;
INSERT INTO `Meals` VALUES (632821,'Asian Chicken Salad',182.82,8.45,14.82,9.41,'chicken: 0.38 cups;slivered almonds: 0.03 cup;pineapple tidbits: 0.13 cup;green onions: 0.25 tablespoons;water chestnuts: 0.63 oz;cream: 0.09 cup;ground ginger: 0.13 teaspoon;salt: 0.06 teaspoon;pepper: 0.13 Dash','Combine and chill first 5 ingredients. Blend sour cream, ginger, salt and pepper; add to chicken mixture. Toss lightly.;Serve with toasted almonds.;Serves 6-8.;','https://img.spoonacular.com/recipes/632821-312x231.jpg'),(633132,'Avocado Chicken Salad',665.19,10.65,21.13,57.48,'avocados: 1.0 ;cherry tomatoes: 5.0 g;extra virgin olive oil: 25.0 ml;limes: 1.0 ;mayonnaise: 1.0 servings;pepper: 0.5 dash;salad: 50.0 g;chicken breast: 75.0 g','Season chicken breast with a little salt and pepper then place in a pot of boiling water until cooked. Leave to cool and cut into cubes, set aside.;Cut avocados into cubes.;Place mixed salad in a large bowl and add olive oil and lime juice, toss well and divide mixed salad into two serving bowls.;Place avocados, chicken meat and cherry tomatoes evenly on top of salad.;Drizzle mayonaise  and a dash of black pepper over salad and serve.;','https://img.spoonacular.com/recipes/633132-312x231.jpg'),(635964,'Bread Omlette',824.68,85.54,44.6,30.27,'bread crumbs: 1.0 cup;eggs: 4.0 ;milk: 1.0 cup;pch salt: 1.0 ','Pahile, pan garma garam kijiye....phir ek murga ka anda laiye....use sohlaiye.....phir chamach layiye....phir ande se sorry kahiye.....phir usko phod dijiye ..phir brad laiye .....use katiye aur uspar fevikol lagaiye aur ande se chipka dijiye .....phir palat dijiye ............phir bina plate mein rakhe..apne jaha man kare waha dal dijiye.........aur message kijiy.e;','https://img.spoonacular.com/recipes/635964-312x231.jpg'),(638649,'Chinese Chicken Salad With Creamy Soy Dressing',321.11,9.04,50.49,6.97,'bell pepper: 0.13 cup;bell pepper: 0.13 cup;carrot: 0.13 cup;mayonnaise: 0.13 cup;ginger root: 0.5 teaspoon;green onions: 1.0 ;soy sauce: 0.25 tablespoon;chicken breast: 1.5 cups;snow peas: 0.25 cup;torn spinach leaves: 1.0 cups','Whisk mayonnaise, soy sauce and ginger together in a large bowl until blended.;Add chicken, snow peas, peppers, carrots and green onion; toss to mix and coat.;Serve over torn spinach leaves.;','https://img.spoonacular.com/recipes/638649-312x231.jpg'),(640311,'Crab Salad in Avocado Boats',413.62,4.82,23.38,31.31,'onion: 0.17 cup;mayonnaise: 1.5 tablespoons;hot sauce such as sriracha: 0.25 teaspoon;cilantro: 1.0 tablespoons;lime juice: 1.5 teaspoons;ground cumin: 0.25 teaspoon;lime zest: 0.25 teaspoon;lump crab meat: 4.0 ounces;avocado: 0.5 large','Stir red onion, mayonnaise, hot sauce, cilantro, 2 teaspoons lime juice, cumin and lime zest in medium bowl to blend.;Mix in crab meat. Season salad with salt and pepper.;Brush each avocado with the remaining 1 teaspoon lime juice to prevent avocado from browning.;Mound crab salad on each avocado half.;Serve salad with lime wedges.;','https://img.spoonacular.com/recipes/640311-312x231.jpg'),(643933,'Fruid Salad Dressing',120.93,28.84,0.87,0.2,'flour: 0.42 teaspoons;fruit: 1.0 servings;honey: 0.25 tablespoons;lemon juice: 0.17 tablespoons;orange juice: 0.08 cup;pineapple juice: 0.5 ounces;sugar: 0.02 cup','In a saucepan, combine the first six ingredients. Bring to a boil; cook and stir until thickened and bubbly (2-5 minutes). Cool.;Serve over fruit. Leftover dressing may be refrigerated for up to 1 week.NOTES: The dressing will easily cover a fruit salad made from 5 lbs of assorted fruit. I used a cantaloupe, strawberries, grapes, a handful of blueberries and the pineapple reserved from the 20 oz can from which I used the pineapple juice.;','https://img.spoonacular.com/recipes/643933-312x231.jpg'),(645733,'Grilled Ham and Swiss Sandwich',290.25,23.94,14.56,14.46,'pats of butter: 2.0 ;ham: 3.0 Pieces;swiss cheese: 2.0 Slices;bread: 2.0 Slices','Melt butter in skillet.Stack sandwich like so: bread, ham, ham, ham, swiss, bread.;Place sandwich in skillet, let brown.  Adjust heat as needed.;Remove the sandwich briefly from the skillet, add the other piece of butter and let it melt.Flip sandwich over and brown. Cook until cheese is melted.Eat hot.;','https://img.spoonacular.com/recipes/645733-312x231.jpg'),(649343,'Layered Chicken Salad With Couscous',431.65,25.05,41.93,15.43,'avocado optional: 0.25 slices;chicken breast: 4.0 ounces;couscous: 0.17 cup;cucumber: 0.25 ;parsley: 0.06 cup;green onions: 1.25 ;chicken broth: 0.25 cup;mayonnaise: 0.5 tablespoons;salt and pepper: 1.0 servings;tomato: 0.25 medium','Let stand 5 minutes. Uncover; fluff couscous with fork. Cool slightly.;Remove both ends from an empty food can (about 3 inches in diameter and 3 inches tall) to make a hollow cylinder. Wash and dry can thoroughly.In bowl, combine couscous, tomato, and parsley; set aside.In another bowl, mix chicken, onions, cucumber, mayonnaise, and seasoning.;Place can on plate; spoon in one-fourth of couscous mixture. Gently press with back of spoon.Top couscous with one-fourth of chicken salad mixture, pressing with spoon, slowly lift off can. Repeat with remaining 3 salads.;Serve with fresh fruit.;','https://img.spoonacular.com/recipes/649343-312x231.jpg'),(650378,'Curry Chicken Salad',682.54,13.62,34.64,52.87,'chicken: 1.0 cans;carrot: 0.5 ;celery: 0.5 Stalk;cucumber: 0.25 ;madras curry powder: 1.0 teaspoons;mayonnaise: 0.25 cup;grapes: 0.5 handful;salad greens: 1.0 servings;turmeric powder: 0.5 teaspoon','Strain the water from the cans of chicken and place the chicken in large mixing bowl.;Add mayonnaise. You can use more or less based on how moist you like your chicken salad.Season with salt and pepper to taste, go easy on the seasoning at this point because the main seasoning will occur at the end when you add the spices. Drop in the diced celery, carrot, cucumber and grapes and mix well. Once all the ingredients have been combined, add additional mayonnaise if you prefer a wetter consistency to the salad.Once the consistency is right, add in curry powder and turmeric powder. These are they key ingredients, so make sure you are using high quality spices. Start with a small amount of each spice and gradually add to taste - the measurements here are just recommendations, you should taste test as you go along. If possible, pop your mixing bowl into the fridge for an hour to let the flavors marry.;Serve of the Curry Chicken Salad on top of salad greens, no dressing necessary.;','https://img.spoonacular.com/recipes/650378-312x231.jpg'),(654959,'Pasta With Tuna',422.67,52.44,24.32,10.32,'flour: 0.5 tablespoons;green onions: 0.25 cup;non-fat milk: 0.31 cups;olive oil: 0.5 tablespoons;onion: 0.5 tablespoons;parmesan cheese: 0.06 cup;parsley: 0.25 cup;tubular pasta: 2.0 ounces;peas: 0.25 cup;dsh pepper sauce: 0.25 ;water-packed tuna: 1.63 ounces','Cook pasta in a large pot of boiling water until al dente.;Drain and return to warm pot. Put olive oil in saucepan and add onion.;Saute until transparent. Stir in flour and cook for a few seconds and then whisk in milk. Stir constantly until this thickens.;Add peas, tuna (shredded into chunks,) parsley, green onions, cheese and hot pepper sauce.;Pour over pasta and stir gently to mix.;Serve at once.;','https://img.spoonacular.com/recipes/654959-312x231.jpg'),(663804,'Tricolor Fried Rava Idli',63.2,11.55,2.01,0.41,'baking powder: 0.13 teaspoons;butter: 0.08 teaspoon;chilies: 0.25 ;onion: 0.08 ;chili powder: 0.02 teaspoon;salt: 1.0 servings;spinach paste: 0.17 tablespoons;tomato puree: 0.17 tablespoons;yoghurt: 0.17 tablespoons;soozi): 0.08 cup','Divide one cup soozi/rava/semolina into three equal portions in three separate containers.;Mix yoghurt with little water and beat for 2-3 minutes.In the first container of soozi, add tomato puree, salt and 1/2 tsp baking powder. The batter should be to the consitency of neither too thin nor too thick.In the second container, add yoghurt, salt and 1/2 tsp baking powder.;Mix well.In the third container, add spinach paste, salt and 1/2 tsp baking powder.;Mix well.All the three batters should be of the same consistency.Meanwhile mix finely chopped onions, green chilis, red chili powder and salt.Lightly oil Idli trays with spray cooking oil or extra virgin olive oil.Prepare idli steamer by preheating water to a boil ( i prefer using stove-top idli maker. );Pour half teaspoon from each batter side by side carefully into the idli mold. Now put half teaspoon of onion mixture for the stuffing in the centre of the mold. Again repeat the process of pouring each batter to cover the stuffing in the respective manner.This process of making idlis will take a little more time and effort.As soon as you finish filling all the molds, put the idli stand into the steamer.;Place a tight lid on the steamer and steam idlis for 15 minutes on medium heat.;Remove idlis from the trays by scooping them out with a spoon.;Heat a flat skillet on medium heat and apply butter. One by one place idlis on the skillet so that only the center portion of the idli touches the skillet.;Heat for 2-3 minutes.The beautiful stuffed idlis are ready.;Serve hot with chutney or ketchup.;','https://img.spoonacular.com/recipes/663804-312x231.jpg'),(715491,'Sugared Pecans Gift Idea & Silhouette America Promotion',653.86,36.55,7.49,54.55,'egg white: 0.17 ;ground cinnamon: 0.08 tsp;pecan halves: 0.17 pound;salt: 0.13 tsp;water: 0.17 Tbsp;sugar: 0.17 cup','Heat your oven up to 250 degrees.In a small bowl add the egg white and water and whisk until frothy.;Pour in pecans and stir to coat them all evenly.In a separate bowl add sugar, cinnamon, and salt.;Mix well.;Pour sugar mixture into pecan mixture and mix well until pecans are coated.;Place on a non stick sheet or prepare a cookie sheet and then spread out the pecans evenly.;Place in the oven for 1 hour, turning the pecans every 15 minutes.;','https://img.spoonacular.com/recipes/715491-312x231.jpg'),(1697759,'Buffalo Chicken Dip - Enough Said',741.07,8.04,32.4,64.48,'chicken thighs: 3.33 oz;butter: 0.33 Tbsp;favorite hot sauce: 0.17 cup;philadelphia cream cheese: 2.67 oz;cheddar cheese: 0.33 cup;ranch dressing: 0.17 cup;salt & pepper: 1.0 servings','Trim fat off chicken thighs and cut&nbsp; into small pieces...no need to shred.&nbsp; Season with salt &amp; pepper.;In a pan, melt butter over medium heat.&nbsp;;Add the chicken when the butter starts to sizzle but doesn’t turn brown yet.;Add your favorite hot sauce and cook until the chicken is cooked through.&nbsp;;Reduce heat and add cream cheese, cheddar cheese, and ranch dressing.;Let the low heat work its magic until everything is melted into the perfect, spicy, tangy deliciousness.;Serve with chips, celery, bread, or crackers.;','https://img.spoonacular.com/recipes/1697759-312x231.jpg');
/*!40000 ALTER TABLE `Meals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NutritionHistory`
--

DROP TABLE IF EXISTS `NutritionHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NutritionHistory` (
  `user_email` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `calories` decimal(10,2) DEFAULT NULL,
  `carbs` decimal(10,2) DEFAULT NULL,
  `proteins` decimal(10,2) DEFAULT NULL,
  `fats` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`user_email`,`date`),
  CONSTRAINT `nutritionhistory_ibfk_1` FOREIGN KEY (`user_email`) REFERENCES `Users` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NutritionHistory`
--

LOCK TABLES `NutritionHistory` WRITE;
/*!40000 ALTER TABLE `NutritionHistory` DISABLE KEYS */;
INSERT INTO `NutritionHistory` VALUES ('ansh300304@gmail.com','2024-04-15',798.60,73.89,59.63,25.45);
/*!40000 ALTER TABLE `NutritionHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `otp`
--

DROP TABLE IF EXISTS `otp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otp` (
  `user_email` varchar(255) NOT NULL,
  `otp` int DEFAULT NULL,
  `expiry_time` datetime DEFAULT NULL,
  PRIMARY KEY (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otp`
--

LOCK TABLES `otp` WRITE;
/*!40000 ALTER TABLE `otp` DISABLE KEYS */;
INSERT INTO `otp` VALUES (', nk bnk n',518179,'2024-04-15 05:56:58'),('adithya.samudrala@gmail.com',692770,'2024-04-15 11:12:29'),('ansh300304@gmail.com',890442,'2024-04-15 06:23:51');
/*!40000 ALTER TABLE `otp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `email` varchar(255) NOT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `goal` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `activity_level` varchar(255) DEFAULT NULL,
  `cals` decimal(10,2) DEFAULT NULL,
  `carbs` decimal(10,2) DEFAULT NULL,
  `protein` decimal(10,2) DEFAULT NULL,
  `fats` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('adithya.samudrala@gmail.com','adithya','adithya','2004-07-11',191,81,'gain_muscle','male','moderately_active',2001.50,250.19,100.07,66.72),('ansh300304@gmail.com','ansh','ansh','2004-11-11',180,70,'gain_muscle','male','very_active',1795.80,224.48,89.79,59.86);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-15 19:25:12
