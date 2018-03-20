-- vim: ft=mysql
-- CREATE USER
CREATE USER IF NOT EXISTS '205CDE'@'localhost' IDENTIFIED BY 'EDC502';
-- GRANT Permission 
GRANT ALL ON `205CDE_Project`.* TO '205CDE'@'localhost';

-- Create DB
CREATE DATABASE IF NOT EXISTS 205CDE_Project;

-- USE DB
USE 205CDE_Project;


-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 20, 2018 at 06:06 AM
-- Server version: 10.1.22-MariaDB
-- PHP Version: 5.5.36

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205CDE_Project`
--

-- --------------------------------------------------------

--
-- Table structure for table `Appointment`
--

CREATE TABLE `Appointment` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `Timeslot_id` int(11) NOT NULL,
  `quota` int(11) NOT NULL DEFAULT '10',
  `actual_qty` int(11) NOT NULL,
  `Zone_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `AuditTrail`
--

CREATE TABLE `AuditTrail` (
  `id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `change_type` enum('INSERT','UPDATE','DELETE') NOT NULL,
  `row_id` int(11) NOT NULL,
  `table` varchar(32) NOT NULL,
  `column_name` varchar(255) NOT NULL,
  `oldValue` varchar(255) NOT NULL,
  `newValue` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `id` int(11) NOT NULL,
  `Title` enum('Mr','Ms','Mrs','Dr') NOT NULL,
  `FirstName` varchar(32) NOT NULL DEFAULT '',
  `LastName` varchar(32) NOT NULL DEFAULT '',
  `CompanyName` varchar(255) NOT NULL DEFAULT '',
  `Address` varchar(255) NOT NULL DEFAULT '',
  `phone` varchar(16) NOT NULL,
  `Created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customers`
--

INSERT INTO `Customers` (`id`, `Title`, `FirstName`, `LastName`, `CompanyName`, `Address`, `phone`, `Created_date`, `created_by`) VALUES
(1, 'Mr', 'Stewart ', 'Floyd', 'ABC', 'abc', '', '2017-11-16 19:03:00', 1),
(2, 'Mr', 'Morris ', 'Lowe', 'BCD', 'bcd', '', '2017-11-16 19:03:01', 1),
(3, 'Mr', 'Ernestine ', 'Cohen', 'CDE', 'cde', '', '2017-11-16 19:03:01', 1),
(4, 'Mr', 'David ', 'West', 'DEF', 'def', '', '2017-11-16 19:03:01', 1),
(5, 'Mr', 'Ralph ', 'Rose', 'EFG', 'efg', '', '2017-11-16 19:03:01', 1),
(6, 'Mr', 'Dana ', 'Phillips', 'FGH', 'fgh', '', '2017-11-16 19:03:02', 1),
(7, 'Mr', 'Lana ', 'Aguilar', 'GHI', 'ghi', '', '2017-11-16 19:03:02', 1),
(8, 'Mr', 'Gina ', 'Ramirez', 'HIJ', 'hij', '', '2017-11-16 19:03:02', 1),
(35, 'Mr', 'ABC', 'cbd', 'aaa', 'dfghjkds', '', '2017-11-17 07:52:53', 1);

-- --------------------------------------------------------

--
-- Table structure for table `LineItem`
--

CREATE TABLE `LineItem` (
  `id` int(11) NOT NULL,
  `Sales_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `sequenceNumber` int(11) NOT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `LineItem`
--

INSERT INTO `LineItem` (`id`, `Sales_id`, `Product_id`, `sequenceNumber`, `price`) VALUES
(1, 1, 1, 1, 10000),
(2, 2, 1, 1, 10000),
(3, 3, 1, 1, 10000),
(4, 3, 2, 2, 20000),
(5, 4, 1, 1, 10000),
(6, 4, 2, 2, 20000),
(7, 5, 2, 1, 20000),
(8, 6, 3, 1, 30000),
(9, 7, 1, 1, 10000),
(10, 7, 3, 2, 30000),
(11, 8, 1, 1, 10000),
(12, 8, 3, 2, 30000);

-- --------------------------------------------------------

--
-- Table structure for table `navigation`
--

CREATE TABLE `navigation` (
  `id` int(11) NOT NULL,
  `caption` varchar(64) NOT NULL,
  `href` varchar(64) NOT NULL,
  `bar` enum('shared','cms') NOT NULL DEFAULT 'shared',
  `position` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `navigation`
--

INSERT INTO `navigation` (`id`, `caption`, `href`, `bar`, `position`) VALUES
(4, 'Sales Order', 'sales.html', 'shared', 2),
(5, 'Shared Navbar', 'shared_navbar.html', 'cms', 0),
(6, 'Staff', 'staff.html', 'cms', 2),
(7, 'Service Order', 'services.html', 'shared', 3),
(8, 'CMS Navbar', 'cms_navbar.html', 'cms', 1),
(9, 'Customers', 'customers.html', 'shared', 1),
(10, 'Products', 'products.html', 'shared', 4),
(12, 'Audit Trail', 'audit_trail.html', 'shared', 5),
(13, 'Raise Error', 'raise_error.html', 'cms', 3);

-- --------------------------------------------------------

--
-- Table structure for table `PaymentMethod`
--

CREATE TABLE `PaymentMethod` (
  `id` int(11) NOT NULL,
  `payment` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `Category` varchar(255) NOT NULL DEFAULT '',
  `Price` float NOT NULL DEFAULT '10000',
  `rivalry` tinyint(1) NOT NULL DEFAULT '0',
  `image` varchar(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`id`, `name`, `description`, `Category`, `Price`, `rivalry`, `image`) VALUES
(1, 'FSBA', 'An application which aimed to provide an economic and business intelligence (BI) supported point-of-sales (POS) system without specific hardware.', 'POS', 10000, 0, 'fsba.jpeg'),
(2, 'BAFD_v1', 'BAFD version 1 ', 'BI Tool', 20000, 0, 'bi.png'),
(3, 'BAFD_v2', 'BAFD version 2 ', 'BI Tool', 30000, 0, 'bi2.png'),
(4, 'BAFD_v3', 'BAFD version 3 ', 'BI Tool', 40000, 0, 'bi3.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `SalesOrder`
--

CREATE TABLE `SalesOrder` (
  `id` int(11) NOT NULL,
  `Customer_id` int(11) NOT NULL DEFAULT '-1',
  `PrintStatus_id` enum('Printed','Not Printed') NOT NULL DEFAULT 'Printed',
  `OrderStatus_id` enum('Scheduled','Dispatched','Completed') NOT NULL DEFAULT 'Scheduled',
  `date` date NOT NULL,
  `date_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Product_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL DEFAULT '1',
  `price` float NOT NULL DEFAULT '0',
  `source` varchar(255) NOT NULL DEFAULT 'Ad',
  `PaymentMethod_id` enum('Cheque','Transfer','CreditCard') NOT NULL DEFAULT 'Transfer',
  `created_by` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `SalesOrder`
--

INSERT INTO `SalesOrder` (`id`, `Customer_id`, `PrintStatus_id`, `OrderStatus_id`, `date`, `date_created`, `last_updated`, `Product_id`, `qty`, `price`, `source`, `PaymentMethod_id`, `created_by`) VALUES
(1, 1, 'Printed', 'Completed', '2017-04-28', '2017-04-27 09:23:55', '2017-04-27 09:23:55', 1, 1, 10000, 'Recommended by others', 'Transfer', 1),
(2, 2, 'Printed', 'Completed', '2017-04-28', '2017-04-27 09:23:55', '2017-04-27 09:23:55', 1, 1, 10000, 'Advertisement', 'CreditCard', 1),
(3, 3, 'Printed', 'Completed', '2017-04-28', '2017-04-27 09:23:55', '2017-04-27 09:23:55', 3, 1, 30000, 'Advertisement', 'Cheque', 1),
(4, 4, 'Printed', 'Completed', '2017-04-28', '2017-04-27 09:23:55', '2017-04-27 09:23:55', 3, 1, 30000, 'Advertisement', 'Transfer', 1),
(5, 5, 'Printed', 'Completed', '2017-04-28', '2017-04-27 17:28:05', '2017-04-27 17:28:05', 2, 1, 20000, 'Recommended by others', 'CreditCard', 1),
(6, 6, 'Printed', 'Completed', '2017-04-28', '2017-04-27 17:31:18', '2017-04-27 17:31:18', 3, 1, 30000, 'Recommended by others', 'Cheque', 1),
(7, 7, 'Printed', 'Completed', '2017-04-28', '2017-04-27 17:37:15', '2017-04-27 17:37:15', 4, 1, 40000, 'Recommended by others', 'Transfer', 1),
(8, 8, 'Printed', 'Completed', '2017-04-28', '2017-04-27 17:43:15', '2017-04-27 17:43:15', 4, 1, 40000, 'Recommended by others', 'CreditCard', 1);

--
-- Triggers `SalesOrder`
--
DELIMITER $$
CREATE TRIGGER `SalesOrder_after_update` AFTER UPDATE ON `SalesOrder` FOR EACH ROW BEGIN
    IF NEW.qty != OLD.qty OR NEW.Product_id != OLD.Product_id THEN
        UPDATE Product SET qty = qty + OLD.qty WHERE id = OLD.Product_id AND rivalry = TRUE;
        UPDATE Product SET qty = qty - NEW.qty WHERE id = NEW.Product_id AND rivalry = TRUE;
    END IF; 
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `ServiceOrder`
--

CREATE TABLE `ServiceOrder` (
  `id` int(11) NOT NULL,
  `printStatus_id` int(11) NOT NULL DEFAULT '1',
  `OrderStatus_id` int(11) NOT NULL DEFAULT '1',
  `Zone_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `date_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Timeslot_id` int(11) NOT NULL,
  `price` float NOT NULL DEFAULT '0',
  `PaymentMethod_id` int(11) NOT NULL DEFAULT '1',
  `Customer_id` int(11) NOT NULL,
  `create_by` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `role` enum('user','manager','admin','') NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `username`, `password`, `firstname`, `lastname`, `email`, `role`) VALUES
(1, 'admin', 'admin', 'Leo', 'Sin', 'lfsin3-c@my.cityu.edu.hk', 'admin'),
(2, 'user', 'user', 'Abc', 'Def', 'test@abc.com', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `Timeslot`
--

CREATE TABLE `Timeslot` (
  `id` int(11) NOT NULL,
  `timeslot` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Zone`
--

CREATE TABLE `Zone` (
  `id` int(11) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Appointment`
--
ALTER TABLE `Appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Timeslot_id` (`Timeslot_id`),
  ADD KEY `Zone_id` (`Zone_id`);

--
-- Indexes for table `AuditTrail`
--
ALTER TABLE `AuditTrail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `created_by` (`created_by`);

--
-- Indexes for table `LineItem`
--
ALTER TABLE `LineItem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Sales_id` (`Sales_id`),
  ADD KEY `Product_id` (`Product_id`);

--
-- Indexes for table `navigation`
--
ALTER TABLE `navigation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PaymentMethod`
--
ALTER TABLE `PaymentMethod`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SalesOrder`
--
ALTER TABLE `SalesOrder`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Customer_id` (`Customer_id`),
  ADD KEY `PaymentMethod_id` (`PaymentMethod_id`),
  ADD KEY `created_by` (`created_by`),
  ADD KEY `Customer_id_2` (`Customer_id`,`date`,`date_created`,`last_updated`),
  ADD KEY `fk_product_id` (`Product_id`);

--
-- Indexes for table `ServiceOrder`
--
ALTER TABLE `ServiceOrder`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Customer_id` (`Customer_id`),
  ADD KEY `Zone_id` (`Zone_id`),
  ADD KEY `PaymentMethod_id` (`PaymentMethod_id`),
  ADD KEY `Timeslot_id` (`Timeslot_id`),
  ADD KEY `create_by` (`create_by`),
  ADD KEY `Product_id` (`Product_id`),
  ADD KEY `date` (`date`,`date_created`,`last_updated`,`price`,`Customer_id`,`Product_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Timeslot`
--
ALTER TABLE `Timeslot`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Zone`
--
ALTER TABLE `Zone`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Appointment`
--
ALTER TABLE `Appointment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `AuditTrail`
--
ALTER TABLE `AuditTrail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Customers`
--
ALTER TABLE `Customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
--
-- AUTO_INCREMENT for table `LineItem`
--
ALTER TABLE `LineItem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `navigation`
--
ALTER TABLE `navigation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `PaymentMethod`
--
ALTER TABLE `PaymentMethod`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `SalesOrder`
--
ALTER TABLE `SalesOrder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `ServiceOrder`
--
ALTER TABLE `ServiceOrder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `Timeslot`
--
ALTER TABLE `Timeslot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Zone`
--
ALTER TABLE `Zone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `SalesOrder`
--
ALTER TABLE `SalesOrder`
  ADD CONSTRAINT `fk_product_id` FOREIGN KEY (`Product_id`) REFERENCES `Product` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
