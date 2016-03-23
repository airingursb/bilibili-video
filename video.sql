# ************************************************************
# Sequel Pro SQL dump
# Version 4135
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.1.63)
# Database: python
# Generation Time: 2016-03-23 04:37:40 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table video
# ------------------------------------------------------------

CREATE TABLE `video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `av` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `title` varchar(150) DEFAULT NULL,
  `tminfo` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `click` int(11) DEFAULT NULL,
  `danmu` int(11) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `favourites` int(11) DEFAULT NULL,
  `duration` varchar(45) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `tag1` varchar(45) DEFAULT NULL,
  `tag2` varchar(45) DEFAULT NULL,
  `tag3` varchar(45) DEFAULT NULL,
  `common` int(11) DEFAULT NULL,
  `honor_click` int(11) DEFAULT NULL,
  `honor_coins` int(11) DEFAULT NULL,
  `honor_favourites` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
