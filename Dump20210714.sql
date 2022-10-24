-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: test_db
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `chercher`
--

DROP TABLE IF EXISTS `chercher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chercher` (
  `Ename` varchar(20) DEFAULT NULL,
  `userId` int DEFAULT NULL,
  KEY `FK_KEY2` (`Ename`),
  KEY `FK_KEY3` (`userId`),
  CONSTRAINT `FK_KEY2` FOREIGN KEY (`Ename`) REFERENCES `entreprise` (`Ename`) ON DELETE CASCADE,
  CONSTRAINT `FK_KEY3` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chercher`
--

LOCK TABLES `chercher` WRITE;
/*!40000 ALTER TABLE `chercher` DISABLE KEYS */;
/*!40000 ALTER TABLE `chercher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_data`
--

DROP TABLE IF EXISTS `company_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_data` (
  `company` varchar(20) NOT NULL,
  `pos` float DEFAULT NULL,
  `neg` float DEFAULT NULL,
  `S_words` varchar(255) DEFAULT NULL,
  `S_frequincies` varchar(255) DEFAULT NULL,
  `S_likes_T` varchar(255) DEFAULT NULL,
  `S_retweets_T` varchar(255) DEFAULT NULL,
  `max_L` int DEFAULT NULL,
  `max_R` int DEFAULT NULL,
  `S_dates` varchar(6000) DEFAULT NULL,
  `id_M` varchar(255) DEFAULT NULL,
  `Timing` date DEFAULT NULL,
  PRIMARY KEY (`company`),
  CONSTRAINT `FK_KEY6` FOREIGN KEY (`company`) REFERENCES `entreprise` (`Ename`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_data`
--

LOCK TABLES `company_data` WRITE;
/*!40000 ALTER TABLE `company_data` DISABLE KEYS */;
INSERT INTO `company_data` VALUES ('ferrari',58,42,'ferrari, rt, restaurant, cavallino, new, lunch, scuderia, past, present, begins, era, friends, drivers, got, hungry, car, don, know, scaloneta, born','36, 26, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 5, 5, 4, 4, 4, 4, 4','0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0','0, 7, 0, 0, 0, 2, 28, 0, 33, 0, 20, 8, 794, 0, 0, 6, 0, 0, 0, 33, 33, 0, 0, 7, 22, 0, 794, 33, 794, 0, 5423, 0, 5423, 4, 5423, 0, 0, 0, 794, 0, 33, 33, 0, 5423, 25, 0, 33, 0, 0, 7',1,5423,'2021-07-13 18:14:58, 2021-07-13 18:14:53, 2021-07-13 18:14:49, 2021-07-13 18:14:47, 2021-07-13 18:14:37, 2021-07-13 18:14:36, 2021-07-13 18:14:36, 2021-07-13 18:14:34, 2021-07-13 18:14:22, 2021-07-13 18:14:21, 2021-07-13 18:14:12, 2021-07-13 18:14:11, 2021-07-13 18:14:08, 2021-07-13 18:14:06, 2021-07-13 18:14:04, 2021-07-13 18:14:01, 2021-07-13 18:13:59, 2021-07-13 18:13:51, 2021-07-13 18:13:45, 2021-07-13 18:13:43, 2021-07-13 18:13:38, 2021-07-13 18:13:34, 2021-07-13 18:13:22, 2021-07-13 18:13:15, 2021-07-13 18:13:12, 2021-07-13 18:13:12, 2021-07-13 18:13:09, 2021-07-13 18:12:58, 2021-07-13 18:12:52, 2021-07-13 18:12:51, 2021-07-13 18:12:49, 2021-07-13 18:12:45, 2021-07-13 18:12:42, 2021-07-13 18:12:16, 2021-07-13 18:12:14, 2021-07-13 18:12:06, 2021-07-13 18:12:03, 2021-07-13 18:11:59, 2021-07-13 18:11:58, 2021-07-13 18:11:56, 2021-07-13 18:11:56, 2021-07-13 18:11:55, 2021-07-13 18:11:54, 2021-07-13 18:11:54, 2021-07-13 18:11:47, 2021-07-13 18:11:45, 2021-07-13 18:11:44, 2021-07-13 18:11:44, 2021-07-13 18:11:43, 2021-07-13 18:11:42','1415011346190671874','2021-07-13'),('maroc telecom',52,48,'telecom, _telecom, maroc, _ana, morocco, rt, alslam, almrjo, mn, launches, gabon, alkhas, 4g, ott, lt, hello, follow, dm, good, fy','21, 17, 13, 7, 6, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2','0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0','0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1',4,256,'2021-07-07 09:22:22, 2021-07-07 10:06:18, 2021-07-07 10:10:18, 2021-07-07 10:18:03, 2021-07-07 12:50:33, 2021-07-07 12:59:34, 2021-07-07 13:46:42, 2021-07-07 13:49:29, 2021-07-07 13:56:37, 2021-07-07 14:15:37, 2021-07-07 14:44:18, 2021-07-07 15:34:30, 2021-07-07 15:43:17, 2021-07-07 15:45:53, 2021-07-07 16:36:57, 2021-07-07 17:14:42, 2021-07-07 19:52:32, 2021-07-07 23:16:21, 2021-07-07 23:40:41, 2021-07-07 23:41:14, 2021-07-07 23:42:53, 2021-07-08 04:30:01, 2021-07-08 08:16:17, 2021-07-08 09:35:04, 2021-07-08 09:40:38, 2021-07-08 10:08:32, 2021-07-08 10:28:56, 2021-07-08 10:29:23, 2021-07-08 10:31:34, 2021-07-08 10:33:22, 2021-07-08 10:48:51, 2021-07-08 11:26:07, 2021-07-08 11:27:24, 2021-07-08 11:52:52, 2021-07-08 11:55:13, 2021-07-08 12:19:06, 2021-07-08 12:23:36, 2021-07-08 12:42:18, 2021-07-08 12:50:39, 2021-07-08 13:10:03, 2021-07-08 13:58:55, 2021-07-08 14:00:25, 2021-07-08 14:38:00, 2021-07-08 14:40:03, 2021-07-08 14:50:10, 2021-07-08 14:52:32, 2021-07-08 15:01:02, 2021-07-08 15:11:36, 2021-07-08 16:28:48, 2021-07-08 16:33:15','1412862113291419650','2021-07-08'),('nike',90,10,'nike, rt, gt, avenatti, michael, dunk, sentencing, new, away, look, liverpool, available, air, adidas, shoes, https, judge, live, lead, designer','42, 33, 8, 7, 6, 6, 6, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3','0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0','59, 0, 72, 0, 85, 85, 0, 0, 0, 925, 69, 60, 0, 2, 449, 2813, 0, 0, 60, 84, 7424, 21, 177, 0, 2813, 0, 0, 0, 1, 128, 0, 2813, 399, 2, 78, 0, 2, 118, 85, 2, 14, 0, 0, 1, 1, 128, 0, 0, 925, 0',1,7424,'2021-07-08 18:11:38, 2021-07-08 18:11:39, 2021-07-08 18:11:39, 2021-07-08 18:11:40, 2021-07-08 18:11:41, 2021-07-08 18:11:42, 2021-07-08 18:11:46, 2021-07-08 18:11:48, 2021-07-08 18:11:49, 2021-07-08 18:11:51, 2021-07-08 18:11:51, 2021-07-08 18:11:52, 2021-07-08 18:11:53, 2021-07-08 18:11:54, 2021-07-08 18:11:57, 2021-07-08 18:11:58, 2021-07-08 18:11:58, 2021-07-08 18:11:59, 2021-07-08 18:11:59, 2021-07-08 18:12:02, 2021-07-08 18:12:03, 2021-07-08 18:12:03, 2021-07-08 18:12:03, 2021-07-08 18:12:04, 2021-07-08 18:12:05, 2021-07-08 18:12:05, 2021-07-08 18:12:06, 2021-07-08 18:12:10, 2021-07-08 18:12:11, 2021-07-08 18:12:12, 2021-07-08 18:12:14, 2021-07-08 18:12:15, 2021-07-08 18:12:18, 2021-07-08 18:12:19, 2021-07-08 18:12:19, 2021-07-08 18:12:20, 2021-07-08 18:12:26, 2021-07-08 18:12:30, 2021-07-08 18:12:30, 2021-07-08 18:12:30, 2021-07-08 18:12:32, 2021-07-08 18:12:36, 2021-07-08 18:12:37, 2021-07-08 18:12:39, 2021-07-08 18:12:39, 2021-07-08 18:12:40, 2021-07-08 18:12:40, 2021-07-08 18:12:42, 2021-07-08 18:12:43, 2021-07-08 18:12:47','1413199253611061248','2021-07-08');
/*!40000 ALTER TABLE `company_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e_proposer`
--

DROP TABLE IF EXISTS `e_proposer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_proposer` (
  `EPname` varchar(20) NOT NULL,
  `Id_gerant` int DEFAULT NULL,
  PRIMARY KEY (`EPname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_proposer`
--

LOCK TABLES `e_proposer` WRITE;
/*!40000 ALTER TABLE `e_proposer` DISABLE KEYS */;
INSERT INTO `e_proposer` VALUES ('celio',NULL),('ferrari',NULL),('kichoix',NULL),('microsoft ',NULL),('nike ',NULL);
/*!40000 ALTER TABLE `e_proposer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entreprise`
--

DROP TABLE IF EXISTS `entreprise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entreprise` (
  `Ename` varchar(20) NOT NULL,
  `Id_gerant` int DEFAULT '1',
  PRIMARY KEY (`Ename`),
  KEY `FK_KEY1` (`Id_gerant`),
  CONSTRAINT `FK_KEY1` FOREIGN KEY (`Id_gerant`) REFERENCES `gerant` (`Id_gerant`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entreprise`
--

LOCK TABLES `entreprise` WRITE;
/*!40000 ALTER TABLE `entreprise` DISABLE KEYS */;
INSERT INTO `entreprise` VALUES ('celio',1),('ferrari',1),('maroc telecom',1),('microsoft',1),('nike',1);
/*!40000 ALTER TABLE `entreprise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gerant`
--

DROP TABLE IF EXISTS `gerant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gerant` (
  `manager_name` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Id_gerant` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Id_gerant`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gerant`
--

LOCK TABLES `gerant` WRITE;
/*!40000 ALTER TABLE `gerant` DISABLE KEYS */;
INSERT INTO `gerant` VALUES ('Manager','123',1);
/*!40000 ALTER TABLE `gerant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proposer`
--

DROP TABLE IF EXISTS `proposer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proposer` (
  `EPname` varchar(20) DEFAULT NULL,
  `userId` int DEFAULT NULL,
  KEY `FK_KEY4` (`EPname`),
  KEY `FK_KEY5` (`userId`),
  CONSTRAINT `FK_KEY4` FOREIGN KEY (`EPname`) REFERENCES `e_proposer` (`EPname`) ON DELETE CASCADE,
  CONSTRAINT `FK_KEY5` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proposer`
--

LOCK TABLES `proposer` WRITE;
/*!40000 ALTER TABLE `proposer` DISABLE KEYS */;
INSERT INTO `proposer` VALUES ('microsoft ',1);
/*!40000 ALTER TABLE `proposer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `userId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('anouar','ano',1),('Ilham','ilh',4),('flow','123',5);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-14 17:00:04
