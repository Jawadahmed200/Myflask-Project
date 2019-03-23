-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2019 at 08:26 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coding`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `mes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `phone`, `mes`) VALUES
(1, 'jawad', 'jawad200@yahoo.com', '0303648455', 'how are you '),
(2, 'ali', 'adhsj', '4', ''),
(3, 'ali', 'adilaziz36', '54542154', 'djsfjdjs'),
(4, 'kamran', 'kamrangggg@dash.com', '5478545', 'hi this is kamran'),
(5, 'kamran', 'kamrangggg@dash.com', '5478545', 'hi this is kamran');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `slug` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sno`, `title`, `content`, `date`, `slug`) VALUES
(3, 'this is third post', 'The stock (also capital stock) of a corporation is all of the shares into which ownership of the corporation is divided.[1] In American English, the shares are commonly called stocks.[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares.', '2019-02-24 11:35:19', 'third-post'),
(4, '4th post', 'The stock (also capital stock) of a corporation is all of the shares into which ownership of the corporation is divided.[1] In American English, the shares are commonly called stocks.[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares.', '2019-02-24 11:50:46', '4th-post'),
(6, '6th post', 'The stock (also capital stock) of a corporation is all of the shares into which ownership of the corporation is divided.[1] In American English, the shares are commonly called stocks.[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares.', '2019-02-24 11:51:41', '6th-post');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
