-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 11, 2023 at 08:33 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_db7`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `bookable_rooms`
-- (See below for the actual view)
--
CREATE TABLE `bookable_rooms` (
`id` int(11)
,`building_id` int(11)
,`room_number` varchar(50)
,`room_type` varchar(50)
,`room_size` int(11)
,`floor_level` int(11)
,`bookable` tinyint(1)
,`location` varchar(255)
,`building_name` varchar(255)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `booked_rooms`
-- (See below for the actual view)
--
CREATE TABLE `booked_rooms` (
`id` int(11)
,`room_number` varchar(50)
,`floor_level` int(11)
,`location` varchar(255)
,`building_name` varchar(255)
,`start_time` datetime
,`end_time` datetime
);

-- --------------------------------------------------------

--
-- Table structure for table `building`
--

CREATE TABLE `building` (
  `id` int(11) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `building_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `building`
--

INSERT INTO `building` (`id`, `location`, `building_name`) VALUES
(1, 'Campus', 'Realfagsbygget'),
(2, 'Campus', 'Kjelhuset'),
(3, 'Campus', 'G-bygget'),
(4, 'Campus', 'Hovedbygget'),
(5, 'Campus', 'Sentralbygget'),
(6, 'Campus', 'M-bygget'),
(7, 'Campus', 'Gjøvik Gård'),
(8, 'Campus', 'Økonomibygget');

-- --------------------------------------------------------

--
-- Stand-in structure for view `contact_info`
-- (See below for the actual view)
--
CREATE TABLE `contact_info` (
`email` varchar(255)
,`phone` varchar(8)
,`university_member` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `number_of_students` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `code`, `name`, `number_of_students`, `teacher_id`, `start_date`, `end_date`) VALUES
(1, 'IT2201', 'Database Systems', 50, 11, '2023-09-01', '2023-12-15'),
(2, 'TDT4102', 'Object-Oriented Programming', 60, 12, '2023-09-01', '2023-12-15'),
(3, 'MAT1100', 'Calculus', 70, 13, '2023-09-01', '2023-12-15'),
(4, 'DAT320', 'Data Management and Database Systems', 40, 11, '2023-09-01', '2023-12-15'),
(5, 'TDT4140', 'Software Engineering', 55, 12, '2023-09-01', '2023-12-15'),
(6, 'MAT1110', 'Linear Algebra', 60, 13, '2023-09-01', '2023-12-15'),
(7, 'TDT4165', 'Programming Languages', 45, 12, '2023-09-01', '2023-12-15'),
(8, 'IT2805', 'Web Technologies', 50, 11, '2023-09-01', '2023-12-15'),
(9, 'MAT1120', 'Discrete Mathematics', 65, 13, '2023-09-01', '2023-12-15'),
(10, 'TDT4173', 'Machine Learning', 40, 11, '2023-09-01', '2023-12-15'),
(11, 'ELE1100', 'Introduction to Electronics', 55, 12, '2023-09-01', '2023-12-15'),
(12, 'BIO1000', 'Introduction to Biology', 70, 13, '2023-09-01', '2023-12-15'),
(13, 'TDT4180', 'Artificial Intelligence', 45, 11, '2023-09-01', '2023-12-15'),
(14, 'PHYS1110', 'Classical Mechanics', 60, 12, '2023-09-01', '2023-12-15'),
(15, 'TMA4100', 'Calculus 1', 75, 13, '2023-09-01', '2023-12-15'),
(16, 'TDT4195', 'Data Science', 40, 11, '2023-09-01', '2023-12-15'),
(17, 'STAT1101', 'Introduction to Statistics', 55, 12, '2023-09-01', '2023-12-15'),
(18, 'TDT4200', 'Parallel Computing', 50, 13, '2023-09-01', '2023-12-15'),
(19, 'PSY1010', 'Introduction to Psychology', 65, 11, '2023-09-01', '2023-12-15'),
(20, 'MEC2200', 'Mechanics and Materials', 70, 12, '2023-09-01', '2023-12-15'),
(21, 'TDT4300', 'Software Architecture', 45, 12, '2023-01-01', '2023-05-31'),
(22, 'INF2200', 'Algorithms and Data Structures', 60, 11, '2023-01-01', '2023-05-31'),
(23, 'MAT2300', 'Probability Theory', 55, 13, '2023-01-01', '2023-05-31'),
(24, 'TDT4145', 'Data Modeling, Databases and Database Management Systems', 40, 11, '2023-01-01', '2023-05-31'),
(25, 'MAT2310', 'Mathematical Statistics', 65, 13, '2023-01-01', '2023-05-31'),
(26, 'TDT4171', 'Cryptography and Network Security', 55, 12, '2023-01-01', '2023-05-31'),
(27, 'FYS1120', 'Electromagnetism', 50, 14, '2023-01-01', '2023-05-31'),
(28, 'STK1100', 'Introduction to Applied Statistics', 70, 15, '2023-01-01', '2023-05-31'),
(29, 'MEC2300', 'Thermodynamics', 75, 12, '2023-01-01', '2023-05-31'),
(30, 'SIF1002', 'International Relations', 60, 15, '2023-01-01', '2023-05-31'),
(31, 'TDT4320', 'Software Development for Large Systems', 40, 11, '2024-01-01', '2024-05-31'),
(32, 'TDT4120', 'Algorithms and Data Structures', 55, 12, '2024-01-01', '2024-05-31'),
(33, 'FYS1121', 'Mechanics', 65, 14, '2024-01-01', '2024-05-31'),
(34, 'STK2100', 'Statistical Methods and Data Analysis', 50, 15, '2024-01-01', '2024-05-31'),
(35, 'MEC2400', 'Fluid Mechanics', 55, 12, '2024-01-01', '2024-05-31'),
(36, 'SIF2002', 'Globalization and Development', 60, 15, '2024-01-01', '2024-05-31'),
(37, 'TDT4345', 'Secure Software Development', 40, 11, '2024-01-01', '2024-05-31'),
(38, 'TDT4105', 'Computer Science, Programming, and Data Analysis', 70, 12, '2024-01-01', '2024-05-31'),
(39, 'FYS1122', 'Waves and Oscillations', 75, 14, '2024-01-01', '2024-05-31'),
(40, 'STK3100', 'Design of Experiments and Regression Analysis', 65, 15, '2024-01-01', '2024-05-31'),
(41, 'PHY2001', 'Quantum Mechanics', 50, 11, '2024-01-15', '2024-05-30'),
(42, 'CHEM1002', 'Organic Chemistry', 60, 12, '2024-01-15', '2024-05-30'),
(43, 'BIO2001', 'Genetics', 70, 13, '2024-01-15', '2024-05-30'),
(44, 'MAT2002', 'Differential Equations', 40, 14, '2024-01-15', '2024-05-30'),
(45, 'SOC1002', 'Introduction to Sociology', 50, 15, '2024-01-15', '2024-05-30'),
(46, 'ART2001', 'Art History', 60, 11, '2024-01-15', '2024-05-30'),
(47, 'ECO1002', 'Microeconomics', 70, 12, '2024-01-15', '2024-05-30'),
(48, 'HIS2001', 'World History', 40, 13, '2024-01-15', '2024-05-30'),
(49, 'ENG2002', 'Advanced English Writing', 50, 14, '2024-01-15', '2024-05-30'),
(50, 'PSY2001', 'Cognitive Psychology', 60, 15, '2024-01-15', '2024-05-30'),
(51, 'MAT3001', 'Advanced Calculus', 50, 11, '2023-08-01', '2024-05-31'),
(52, 'PHY3002', 'Advanced Physics', 60, 12, '2023-08-01', '2024-05-31'),
(53, 'CHEM3001', 'Inorganic Chemistry', 70, 13, '2023-08-01', '2024-05-31'),
(54, 'BIO3002', 'Molecular Biology', 40, 14, '2023-08-01', '2024-05-31');

-- --------------------------------------------------------

--
-- Stand-in structure for view `course_schedules`
-- (See below for the actual view)
--
CREATE TABLE `course_schedules` (
`id` int(11)
,`name` varchar(255)
,`start_time` datetime
,`end_time` datetime
,`room_number` varchar(50)
,`floor_level` int(11)
,`location` varchar(255)
,`building_name` varchar(255)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `course_semester`
-- (See below for the actual view)
--
CREATE TABLE `course_semester` (
`course_id` int(11)
,`code` varchar(20)
,`name` varchar(255)
,`start_date` date
,`end_date` date
,`semester` varchar(33)
);

-- --------------------------------------------------------

--
-- Table structure for table `email`
--

CREATE TABLE `email` (
  `email` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `institute`
--

CREATE TABLE `institute` (
  `institute` varchar(255) NOT NULL,
  `faculty` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `institute`
--

INSERT INTO `institute` (`institute`, `faculty`) VALUES
('Department of Business Administration', 'Faculty of Economics and Management'),
('Department of Business and Economics', 'Faculty of Business and Economics'),
('Department of Computer Science', 'Faculty of Information Technology and Electrical Engineering'),
('Department of Engineering', 'Faculty of Engineering'),
('Department of History', 'Faculty of Humanities'),
('Department of Law', 'Faculty of Social and Educational Sciences'),
('Department of Mathematics', 'Faculty of Natural Sciences and Technology'),
('Department of Physics', 'Faculty of Science and Technology'),
('Institute', 'Faculty');

-- --------------------------------------------------------

--
-- Table structure for table `lecture`
--

CREATE TABLE `lecture` (
  `course_id` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `activity` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lecture`
--

INSERT INTO `lecture` (`course_id`, `booking_id`, `activity`) VALUES
(1, 20, 'Lecture'),
(2, 21, 'Practice'),
(3, 22, 'Lecture'),
(4, 23, 'Practice'),
(5, 24, 'Lecture'),
(6, 25, 'Practice'),
(7, 26, 'Lecture'),
(8, 27, 'Practice'),
(9, 28, 'Lecture'),
(10, 29, 'Practice'),
(11, 30, 'Lecture'),
(12, 20, 'Practice'),
(13, 21, 'Lecture'),
(14, 22, 'Practice'),
(15, 23, 'Lecture'),
(1, 24, 'Practice'),
(2, 25, 'Lecture'),
(3, 26, 'Practice'),
(4, 27, 'Lecture'),
(5, 28, 'Practice'),
(6, 29, 'Lecture'),
(7, 30, 'Practice'),
(8, 20, 'Lecture'),
(9, 21, 'Practice'),
(10, 22, 'Lecture'),
(11, 23, 'Practice'),
(12, 24, 'Lecture'),
(13, 25, 'Practice'),
(14, 26, 'Lecture'),
(15, 27, 'Practice');

-- --------------------------------------------------------

--
-- Table structure for table `phone`
--

CREATE TABLE `phone` (
  `phone` varchar(8) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `id` int(11) NOT NULL,
  `building_id` int(11) NOT NULL,
  `room_number` varchar(50) DEFAULT NULL,
  `room_type` varchar(50) DEFAULT NULL,
  `room_size` int(11) DEFAULT NULL,
  `floor_level` int(11) DEFAULT NULL,
  `bookable` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`id`, `building_id`, `room_number`, `room_type`, `room_size`, `floor_level`, `bookable`) VALUES
(1, 1, 'R101', 'Classroom', 50, 1, 1),
(2, 1, 'R102', 'Classroom', 60, 1, 1),
(3, 1, 'R103', 'Lab', 40, 1, 1),
(4, 2, 'K101', 'Classroom', 50, 1, 1),
(5, 2, 'K102', 'Classroom', 60, 1, 1),
(6, 2, 'K103', 'Lab', 40, 1, 1),
(7, 3, 'G101', 'Classroom', 50, 2, 1),
(8, 3, 'G102', 'Classroom', 60, 2, 1),
(9, 3, 'G103', 'Lab', 40, 2, 1),
(10, 4, 'H101', 'Classroom', 50, 2, 1),
(11, 4, 'H102', 'Classroom', 60, 2, 1),
(12, 4, 'H103', 'Lab', 40, 2, 1),
(13, 5, 'S101', 'Classroom', 50, 3, 1),
(14, 5, 'S102', 'Classroom', 60, 3, 1),
(15, 5, 'S103', 'Lab', 40, 3, 1),
(16, 6, 'M101', 'Classroom', 50, 3, 1),
(17, 6, 'M102', 'Classroom', 60, 3, 1),
(18, 6, 'M103', 'Lab', 40, 3, 1),
(19, 7, 'GG101', 'Classroom', 50, 1, 1),
(20, 8, 'Ø101', 'Classroom', 50, 1, 1),
(21, 1, 'R201', 'Classroom', 50, 2, 1),
(22, 1, 'R202', 'Classroom', 60, 2, 1),
(23, 1, 'R203', 'Lab', 40, 2, 1),
(24, 1, 'R204', 'Meeting Room', 30, 2, 1),
(25, 1, 'R205', 'Study Room', 20, 2, 1),
(26, 1, 'R206', NULL, NULL, 2, 1),
(27, 2, 'K201', 'Classroom', 50, 2, 1),
(28, 2, 'K202', 'Classroom', 60, 2, 1),
(29, 2, 'K203', 'Lab', 40, 2, 1),
(30, 2, 'K204', 'Auditorium', 100, 2, 1),
(31, 2, 'K205', NULL, 25, 2, 1),
(32, 3, 'G201', 'Classroom', 50, 3, 1),
(33, 3, 'G202', 'Classroom', 60, 3, 1),
(34, 3, 'G203', 'Lab', 40, 3, 1),
(35, 3, 'G204', 'Workshop', 35, 3, 1),
(36, 3, 'G205', NULL, 30, 3, 1),
(37, 4, 'H201', 'Classroom', 50, 3, 1),
(38, 4, 'H202', 'Classroom', 60, 3, 1),
(39, 4, 'H203', 'Lab', 40, 3, 1),
(40, 4, 'H204', 'Seminar Room', 50, 3, 1),
(41, 1, 'R301', 'Office', NULL, 3, 0),
(42, 1, 'R302', 'Office', NULL, 3, 0),
(43, 2, 'K301', 'Office', NULL, 3, 0),
(44, 2, 'K302', 'Office', NULL, 3, 0),
(45, 3, 'G301', 'Office', NULL, 4, 0),
(46, 3, 'G302', 'Office', NULL, 4, 0),
(47, 4, 'H301', 'Office', NULL, 4, 0),
(48, 4, 'H302', 'Office', NULL, 4, 0),
(49, 5, 'S301', 'Office', NULL, 5, 0),
(50, 5, 'S302', 'Office', NULL, 5, 0);

-- --------------------------------------------------------

--
-- Table structure for table `room_booking`
--

CREATE TABLE `room_booking` (
  `id` int(11) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `room_id` int(11) NOT NULL,
  `booker` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_booking`
--

INSERT INTO `room_booking` (`id`, `start_time`, `end_time`, `type`, `room_id`, `booker`) VALUES
(20, '2023-05-12 09:00:00', '2023-05-12 10:30:00', 'Meeting', 1, 5),
(21, '2023-06-05 14:30:00', '2023-06-05 16:00:00', 'Presentation', 2, 8),
(22, '2023-06-15 11:00:00', '2023-06-15 12:30:00', 'Class', 3, 3),
(23, '2023-07-08 10:30:00', '2023-07-08 12:00:00', 'Workshop', 4, 14),
(24, '2023-07-21 15:30:00', '2023-07-21 17:00:00', 'Meeting', 5, 7),
(25, '2023-08-02 13:00:00', '2023-08-02 14:30:00', 'Presentation', 6, 9),
(26, '2023-08-18 14:00:00', '2023-08-18 15:30:00', 'Class', 7, 12),
(27, '2023-08-28 16:30:00', '2023-08-28 18:00:00', 'Workshop', 8, 11),
(28, '2024-02-03 09:00:00', '2024-02-03 10:30:00', 'Meeting', 9, 1),
(29, '2024-02-15 11:30:00', '2024-02-15 13:00:00', 'Presentation', 10, 6),
(30, '2024-03-05 14:30:00', '2024-03-05 16:00:00', 'Class', 11, 2),
(31, '2024-03-19 15:00:00', '2024-03-19 16:30:00', 'Workshop', 12, 10),
(32, '2024-04-10 10:30:00', '2024-04-10 12:00:00', 'Meeting', 13, 4),
(33, '2024-04-21 13:30:00', '2024-04-21 15:00:00', 'Presentation', 14, 15),
(34, '2024-05-03 14:00:00', '2024-05-03 15:30:00', 'Class', 15, 13),
(35, '2024-05-15 16:30:00', '2024-05-15 18:00:00', 'Workshop', 16, 6),
(36, '2024-06-07 09:00:00', '2024-06-07 10:30:00', 'Meeting', 17, 5),
(37, '2024-06-20 11:30:00', '2024-06-20 13:00:00', 'Presentation', 18, 9),
(38, '2024-07-02 14:30:00', '2024-07-02 16:00:00', 'Class', 19, 7),
(39, '2023-08-12 09:00:00', '2023-08-12 10:30:00', 'Meeting', 1, 4),
(40, '2023-09-02 14:30:00', '2023-09-02 16:00:00', 'Presentation', 2, 13),
(41, '2023-09-15 11:00:00', '2023-09-15 12:30:00', 'Class', 3, 6),
(42, '2023-10-08 10:30:00', '2023-10-08 12:00:00', 'Workshop', 4, 10),
(43, '2023-10-21 15:30:00', '2023-10-21 17:00:00', 'Meeting', 5, 12),
(44, '2023-11-02 13:00:00', '2023-11-02 14:30:00', 'Presentation', 6, 2),
(45, '2023-11-18 14:00:00', '2023-11-18 15:30:00', 'Class', 7, 1),
(46, '2023-11-28 16:30:00', '2023-11-28 18:00:00', 'Workshop', 8, 8),
(47, '2024-02-14 09:00:00', '2024-02-14 10:30:00', 'Meeting', 9, 14),
(48, '2024-02-26 11:30:00', '2024-02-26 13:00:00', 'Presentation', 10, 3),
(49, '2024-03-16 14:30:00', '2024-03-16 16:00:00', 'Class', 11, 7),
(50, '2024-03-29 15:00:00', '2024-03-29 16:30:00', 'Workshop', 12, 15),
(51, '2024-04-20 10:30:00', '2024-04-20 12:00:00', 'Meeting', 13, 5),
(52, '2024-05-01 13:30:00', '2024-05-01 15:00:00', 'Presentation', 14, 11),
(53, '2024-05-14 14:00:00', '2024-05-14 15:30:00', 'Class', 15, 9);

-- --------------------------------------------------------

--
-- Stand-in structure for view `staff_contact`
-- (See below for the actual view)
--
CREATE TABLE `staff_contact` (
`university_id` int(11)
,`title` varchar(50)
,`name` varchar(50)
,`surname` varchar(50)
,`room_id` int(11)
,`room_number` varchar(50)
,`floor_level` int(11)
,`location` varchar(255)
,`building_name` varchar(255)
,`email` varchar(255)
,`phone` varchar(8)
);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `university_member` int(11) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `institute` varchar(255) NOT NULL,
  `office` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`university_member`, `title`, `institute`, `office`) VALUES
(11, 'Dr.', 'Department of Computer Science', 41),
(12, 'Prof.', 'Department of Engineering', 42),
(13, 'Dr.', 'Department of Mathematics', 43),
(14, 'Dr.', 'Department of Computer Science', 44),
(15, 'Prof.', 'Department of Engineering', 45);

-- --------------------------------------------------------

--
-- Table structure for table `university_member`
--

CREATE TABLE `university_member` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `university_member`
--

INSERT INTO `university_member` (`id`, `name`, `surname`) VALUES
(1, 'John', 'Doe'),
(2, 'Jane', 'Smith'),
(3, 'Michael', 'Johnson'),
(4, 'Emily', 'Williams'),
(5, 'Robert', 'Brown'),
(6, 'Sarah', 'Taylor'),
(7, 'David', 'Anderson'),
(8, 'Jennifer', 'Thomas'),
(9, 'Christopher', 'Martinez'),
(10, 'Jessica', 'Clark'),
(11, 'Robert', 'Johnson'),
(12, 'Emily', 'Anderson'),
(13, 'Michael', 'Clark'),
(14, 'Sarah', 'Smith'),
(15, 'David', 'Taylor');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15);

-- --------------------------------------------------------

--
-- Table structure for table `user_schedule`
--

CREATE TABLE `user_schedule` (
  `user_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_schedule`
--

INSERT INTO `user_schedule` (`user_id`, `course_id`) VALUES
(1, 1),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10);

-- --------------------------------------------------------

--
-- Stand-in structure for view `user_time_schedule`
-- (See below for the actual view)
--
CREATE TABLE `user_time_schedule` (
`user_id` int(11)
,`course_id` int(11)
,`code` varchar(20)
,`name` varchar(255)
,`activity` varchar(255)
,`start_time` datetime
,`end_time` datetime
,`room_number` varchar(50)
,`location` varchar(255)
,`building_name` varchar(255)
);

-- --------------------------------------------------------

--
-- Structure for view `bookable_rooms`
--
DROP TABLE IF EXISTS `bookable_rooms`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `bookable_rooms`  AS SELECT `room`.`id` AS `id`, `room`.`building_id` AS `building_id`, `room`.`room_number` AS `room_number`, `room`.`room_type` AS `room_type`, `room`.`room_size` AS `room_size`, `room`.`floor_level` AS `floor_level`, `room`.`bookable` AS `bookable`, `building`.`location` AS `location`, `building`.`building_name` AS `building_name` FROM (`room` left join `building` on(`room`.`building_id` = `building`.`id`)) WHERE `room`.`bookable` = 1111  ;

-- --------------------------------------------------------

--
-- Structure for view `booked_rooms`
--
DROP TABLE IF EXISTS `booked_rooms`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `booked_rooms`  AS SELECT `room`.`id` AS `id`, `room`.`room_number` AS `room_number`, `room`.`floor_level` AS `floor_level`, `building`.`location` AS `location`, `building`.`building_name` AS `building_name`, `room_booking`.`start_time` AS `start_time`, `room_booking`.`end_time` AS `end_time` FROM ((`room_booking` left join `room` on(`room_booking`.`room_id` = `room`.`id`)) left join `building` on(`room`.`building_id` = `building`.`id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `contact_info`
--
DROP TABLE IF EXISTS `contact_info`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `contact_info`  AS SELECT `email`.`email` AS `email`, `phone`.`phone` AS `phone`, `university_member`.`id` AS `university_member` FROM ((`university_member` left join `email` on(`university_member`.`id` = `email`.`user_id`)) left join `phone` on(`university_member`.`id` = `phone`.`user_id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `course_schedules`
--
DROP TABLE IF EXISTS `course_schedules`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `course_schedules`  AS SELECT `course`.`id` AS `id`, `course`.`name` AS `name`, `room_booking`.`start_time` AS `start_time`, `room_booking`.`end_time` AS `end_time`, `room`.`room_number` AS `room_number`, `room`.`floor_level` AS `floor_level`, `building`.`location` AS `location`, `building`.`building_name` AS `building_name` FROM ((((`course` left join `lecture` on(`course`.`id` = `lecture`.`course_id`)) left join `room_booking` on(`lecture`.`booking_id` = `room_booking`.`id`)) left join `room` on(`room_booking`.`room_id` = `room`.`id`)) left join `building` on(`room`.`building_id` = `building`.`id`))  ;

-- --------------------------------------------------------

--
-- Structure for view `course_semester`
--
DROP TABLE IF EXISTS `course_semester`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `course_semester`  AS SELECT DISTINCT `course`.`id` AS `course_id`, `course`.`code` AS `code`, `course`.`name` AS `name`, `course`.`start_date` AS `start_date`, `course`.`end_date` AS `end_date`, CASE WHEN year(`course`.`start_date`) = year(`course`.`end_date`) AND month(`course`.`start_date`) between '01' and '06' AND month(`course`.`end_date`) between '01' and '06' THEN concat('Vår ',year(`course`.`start_date`)) WHEN year(`course`.`start_date`) = year(`course`.`end_date`) AND month(`course`.`start_date`) between '07' and '12' AND month(`course`.`end_date`) between '07' and '12' THEN concat('Høst ',year(`course`.`start_date`)) WHEN year(`course`.`start_date`) < year(`course`.`end_date`) THEN concat('Høst ',year(`course`.`start_date`),' / Vår ',year(`course`.`end_date`)) ELSE 'Error, could not derive semester!' END AS `semester` FROM `course`  ;

-- --------------------------------------------------------

--
-- Structure for view `staff_contact`
--
DROP TABLE IF EXISTS `staff_contact`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `staff_contact`  AS SELECT `university_member`.`id` AS `university_id`, `teacher`.`title` AS `title`, `university_member`.`name` AS `name`, `university_member`.`surname` AS `surname`, `room`.`id` AS `room_id`, `room`.`room_number` AS `room_number`, `room`.`floor_level` AS `floor_level`, `building`.`location` AS `location`, `building`.`building_name` AS `building_name`, `contact_info`.`email` AS `email`, `contact_info`.`phone` AS `phone` FROM ((((`teacher` left join `room` on(`teacher`.`office` = `room`.`id`)) left join `building` on(`room`.`building_id` = `building`.`id`)) left join `university_member` on(`teacher`.`university_member` = `university_member`.`id`)) left join `contact_info` on(`university_member`.`id` = `contact_info`.`university_member`))  ;

-- --------------------------------------------------------

--
-- Structure for view `user_time_schedule`
--
DROP TABLE IF EXISTS `user_time_schedule`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `user_time_schedule`  AS SELECT `user`.`id` AS `user_id`, `course`.`id` AS `course_id`, `course`.`code` AS `code`, `course`.`name` AS `name`, `lecture`.`activity` AS `activity`, `room_booking`.`start_time` AS `start_time`, `room_booking`.`end_time` AS `end_time`, `room`.`room_number` AS `room_number`, `building`.`location` AS `location`, `building`.`building_name` AS `building_name` FROM ((((((`user` left join `user_schedule` on(`user`.`id` = `user_schedule`.`user_id`)) left join `course` on(`user_schedule`.`course_id` = `course`.`id`)) left join `lecture` on(`course`.`id` = `lecture`.`course_id`)) left join `room_booking` on(`lecture`.`booking_id` = `room_booking`.`id`)) left join `room` on(`room_booking`.`room_id` = `room`.`id`)) left join `building` on(`room`.`building_id` = `building`.`id`)) GROUP BY `user`.`id` ORDER BY `room_booking`.`start_time` ASC  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `building`
--
ALTER TABLE `building`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `email`
--
ALTER TABLE `email`
  ADD PRIMARY KEY (`email`,`user_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `institute`
--
ALTER TABLE `institute`
  ADD PRIMARY KEY (`institute`);

--
-- Indexes for table `lecture`
--
ALTER TABLE `lecture`
  ADD KEY `course_id` (`course_id`),
  ADD KEY `booking_id` (`booking_id`);

--
-- Indexes for table `phone`
--
ALTER TABLE `phone`
  ADD PRIMARY KEY (`phone`,`user_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id`),
  ADD KEY `building_id` (`building_id`);

--
-- Indexes for table `room_booking`
--
ALTER TABLE `room_booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`),
  ADD KEY `booker` (`booker`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`university_member`) USING BTREE,
  ADD KEY `institute` (`institute`),
  ADD KEY `office` (`office`);

--
-- Indexes for table `university_member`
--
ALTER TABLE `university_member`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_schedule`
--
ALTER TABLE `user_schedule`
  ADD KEY `user_id` (`user_id`),
  ADD KEY `course_id` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `building`
--
ALTER TABLE `building`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `room_booking`
--
ALTER TABLE `room_booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`university_member`);

--
-- Constraints for table `email`
--
ALTER TABLE `email`
  ADD CONSTRAINT `email_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `university_member` (`id`);

--
-- Constraints for table `lecture`
--
ALTER TABLE `lecture`
  ADD CONSTRAINT `lecture_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  ADD CONSTRAINT `lecture_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `room_booking` (`id`);

--
-- Constraints for table `phone`
--
ALTER TABLE `phone`
  ADD CONSTRAINT `phone_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `university_member` (`id`);

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`building_id`) REFERENCES `building` (`id`);

--
-- Constraints for table `room_booking`
--
ALTER TABLE `room_booking`
  ADD CONSTRAINT `room_booking_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`),
  ADD CONSTRAINT `room_booking_ibfk_2` FOREIGN KEY (`booker`) REFERENCES `university_member` (`id`);

--
-- Constraints for table `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`university_member`) REFERENCES `university_member` (`id`),
  ADD CONSTRAINT `teacher_ibfk_2` FOREIGN KEY (`institute`) REFERENCES `institute` (`institute`),
  ADD CONSTRAINT `teacher_ibfk_3` FOREIGN KEY (`office`) REFERENCES `room` (`id`);

--
-- Constraints for table `university_member`
--
ALTER TABLE `university_member`
  ADD CONSTRAINT `university_member_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user_schedule`
--
ALTER TABLE `user_schedule`
  ADD CONSTRAINT `user_schedule_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `user_schedule_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;