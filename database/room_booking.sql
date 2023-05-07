-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2023 at 11:43 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

USE db;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `room_bookings`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `number_of_students` int(11) DEFAULT NULL,
  `teacher_id` varchar(20) DEFAULT NULL,
  `semester_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `name`, `number_of_students`, `teacher_id`, `semester_id`) VALUES
('IDATG2001', 'Databaser 1', 70, '0123456789', 2),
('IDATG2002', 'Databaser 2', 60, '1234567890', 1),
('IDATG4001', 'Webprogrammering', 30, '9012345678', 2),
('IDATT1001', 'Programmering 1', 120, '7890123456', 1),
('IDATT1002', 'Programmering 2', 90, '8901234567', 1),
('IDATT1003', 'Programmering 3', 80, '9012345678', 2),
('IDATT3001', 'Programvarearkitektur', 50, '7890123456', 2),
('IDATT3002', 'Programmeringsspråk', 40, '8901234567', 1);

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
('Department of Computer Science', 'Faculty of Information Technology and Electrical Engineering'),
('Department of History', 'Faculty of Humanities'),
('Department of Law', 'Faculty of Social and Educational Sciences'),
('Department of Mathematics', 'Faculty of Natural Sciences and Technology');

-- --------------------------------------------------------

--
-- Table structure for table `lecture`
--

CREATE TABLE `lecture` (
  `course_id` varchar(20) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `activity` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lecture`
--

INSERT INTO `lecture` (`course_id`, `booking_id`, `activity`) VALUES
('IDATT1001', 1, 'Lecture'),
('IDATT1001', 2, 'Lab'),
('IDATT1002', 3, 'Lecture'),
('IDATT1002', 4, 'Lab'),
('IDATT1003', 5, 'Lecture'),
('IDATT1003', 6, 'Lab'),
('IDATG2001', 7, 'Lecture'),
('IDATG2001', 8, 'Lab'),
('IDATG2002', 9, 'Lecture'),
('IDATG2002', 10, 'Lab'),
('IDATT3001', 11, 'Lecture'),
('IDATT3001', 12, 'Lab'),
('IDATT3002', 13, 'Lecture'),
('IDATT3002', 14, 'Lab'),
('IDATG4001', 15, 'Lecture'),
('IDATG4001', 16, 'Lab'),
('IDATT1001', 17, 'Lecture'),
('IDATT1001', 18, 'Lab'),
('IDATT1002', 19, 'Lecture'),
('IDATT1002', 20, 'Lab'),
('IDATT1003', 21, 'Lecture'),
('IDATT1003', 22, 'Lab'),
('IDATG2001', 23, 'Lecture'),
('IDATG2001', 24, 'Lab'),
('IDATG2002', 25, 'Lecture'),
('IDATG2002', 26, 'Lab'),
('IDATT3001', 27, 'Lecture'),
('IDATT3001', 28, 'Lab'),
('IDATT3002', 29, 'Lecture'),
('IDATT3002', 30, 'Lab');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_id` int(11) NOT NULL,
  `room_number` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `room_type` varchar(50) DEFAULT NULL,
  `room_size` int(11) DEFAULT NULL,
  `floor_level` int(11) DEFAULT NULL,
  `building_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_id`, `room_number`, `location`, `room_type`, `room_size`, `floor_level`, `building_name`) VALUES
(1, 'A101', 'Trondheim', 'Lecture Hall', 200, 1, 'Abel Building'),
(2, 'A102', 'Trondheim', 'Lecture Hall', 150, 1, 'Abel Building'),
(3, 'A103', 'Trondheim', 'Seminar Room', 30, 1, 'Abel Building'),
(4, 'B201', 'Trondheim', 'Lecture Hall', 180, 2, 'Bolt Building'),
(5, 'B202', 'Trondheim', 'Seminar Room', 25, 2, 'Bolt Building'),
(6, 'B203', 'Trondheim', 'Seminar Room', 20, 2, 'Bolt Building'),
(7, 'C301', 'Trondheim', 'Lecture Hall', 220, 3, 'Curie Building'),
(8, 'C302', 'Trondheim', 'Seminar Room', 40, 3, 'Curie Building'),
(9, 'C303', 'Trondheim', 'Seminar Room', 35, 3, 'Curie Building'),
(10, 'D401', 'Trondheim', 'Lecture Hall', 190, 4, 'Darwin Building'),
(11, 'D402', 'Trondheim', 'Seminar Room', 30, 4, 'Darwin Building'),
(12, 'A101', 'Gjøvik', 'Lecture Hall', 250, 1, 'Elton Building'),
(13, 'A102', 'Gjøvik', 'Seminar Room', 35, 1, 'Elton Building'),
(14, 'A103', 'Gjøvik', 'Seminar Room', 30, 1, 'Elton Building'),
(15, 'A101', 'Ålesund', 'Lecture Hall', 180, 1, 'Gunn Building'),
(16, 'A102', 'Ålesund', 'Seminar Room', 20, 1, 'Gunn Building'),
(17, 'A103', 'Ålesund', 'Seminar Room', 15, 1, 'Gunn Building'),
(18, 'B201', 'Ålesund', 'Lecture Hall', 220, 2, 'Gunn Building'),
(19, 'B202', 'Ålesund', 'Seminar Room', 30, 2, 'Gunn Building'),
(20, 'B203', 'Ålesund', 'Seminar Room', 25, 2, 'Gunn Building'),
(21, 'A201', 'Trondheim', 'Office Room', 10, 2, 'Abel Building'),
(22, 'B301', 'Trondheim', 'Office Room', 12, 3, 'Bolt Building'),
(23, 'C401', 'Gjøvik', 'Office Room', 15, 4, 'Curie Building'),
(24, 'D501', 'Gjøvik', 'Office Room', 8, 5, 'Darwin Building'),
(25, 'E601', 'Ålesund', 'Office Room', 6, 6, 'Elton Building');

-- --------------------------------------------------------

--
-- Table structure for table `room_booking`
--

CREATE TABLE `room_booking` (
  `booking_id` int(11) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `room_id` int(11) NOT NULL,
  `booker` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_booking`
--

INSERT INTO `room_booking` (`booking_id`, `start_time`, `end_time`, `type`, `room_id`, `booker`) VALUES
(1, '2023-06-08 09:00:00', '2023-06-08 11:00:00', 'Lecture', 1, 19),
(2, '2023-06-08 11:15:00', '2023-06-08 13:15:00', 'Seminar', 2, 20),
(3, '2023-06-09 10:30:00', '2023-06-09 12:30:00', 'Meeting', 3, 1),
(4, '2023-06-09 13:00:00', '2023-06-09 15:00:00', 'Lecture', 4, 2),
(5, '2023-06-10 12:15:00', '2023-06-10 14:15:00', 'Lecture', 5, 3),
(6, '2023-06-10 14:30:00', '2023-06-10 16:30:00', 'Seminar', 6, 4),
(7, '2023-06-11 08:45:00', '2023-06-11 10:45:00', 'Meeting', 7, 5),
(8, '2023-06-11 11:00:00', '2023-06-11 13:00:00', 'Lecture', 8, 6),
(9, '2023-06-12 14:15:00', '2023-06-12 16:15:00', 'Lecture', 9, 7),
(10, '2023-06-12 16:30:00', '2023-06-12 18:30:00', 'Seminar', 10, 8),
(11, '2023-05-15 08:00:00', '2023-05-15 10:00:00', 'Lecture', 11, 9),
(12, '2023-05-15 10:15:00', '2023-05-15 12:15:00', 'Seminar', 12, 10),
(13, '2023-05-16 09:30:00', '2023-05-16 11:30:00', 'Meeting', 13, 11),
(14, '2023-05-16 12:00:00', '2023-05-16 14:00:00', 'Lecture', 14, 12),
(15, '2023-05-17 13:15:00', '2023-05-17 15:15:00', 'Lecture', 15, 13),
(16, '2023-05-17 15:30:00', '2023-05-17 17:30:00', 'Seminar', 16, 14),
(17, '2023-05-18 10:45:00', '2023-05-18 12:45:00', 'Meeting', 17, 15),
(18, '2023-05-18 13:00:00', '2023-05-18 15:00:00', 'Lecture', 18, 16),
(19, '2023-05-19 14:45:00', '2023-05-19 16:45:00', 'Lecture', 19, 17),
(20, '2023-05-19 17:00:00', '2023-05-19 19:00:00', 'Seminar', 20, 18),
(21, '2023-08-01 09:00:00', '2023-08-01 11:00:00', 'Lecture', 1, 19),
(22, '2023-08-01 11:15:00', '2023-08-01 13:15:00', 'Seminar', 2, 20),
(23, '2023-08-02 10:30:00', '2023-08-02 12:30:00', 'Meeting', 3, 1),
(24, '2023-08-02 13:00:00', '2023-08-02 15:00:00', 'Lecture', 4, 2),
(25, '2023-08-03 12:15:00', '2023-08-03 14:15:00', 'Lecture', 5, 3),
(26, '2023-08-03 14:30:00', '2023-08-03 16:30:00', 'Seminar', 6, 4),
(27, '2023-08-04 08:45:00', '2023-08-04 10:45:00', 'Meeting', 7, 5),
(28, '2023-08-04 11:00:00', '2023-08-04 13:00:00', 'Lecture', 8, 6),
(29, '2023-08-05 14:15:00', '2023-08-05 16:15:00', 'Lecture', 9, 7),
(30, '2023-08-05 16:30:00', '2023-08-05 18:30:00', 'Seminar', 10, 8);

-- --------------------------------------------------------

--
-- Table structure for table `semester`
--

CREATE TABLE `semester` (
  `semester_id` int(11) NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester`
--

INSERT INTO `semester` (`semester_id`, `start_time`, `end_time`, `name`) VALUES
(1, '2023-01-01 00:00:00', '2023-06-30 00:00:00', 'SPRING2023'),
(2, '2023-07-01 00:00:00', '2023-12-31 00:00:00', 'AUTUMN2023'),
(3, '2024-01-01 00:00:00', '2024-06-30 00:00:00', 'SPRING2024');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `personal_id` varchar(20) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `institute` varchar(255) NOT NULL,
  `office` int(11) NOT NULL,
  `university_member` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`personal_id`, `title`, `institute`, `office`, `university_member`) VALUES
('0123456789', 'Professor', 'Department of History', 24, 10),
('1234567890', 'Associate Professor', 'Department of Business Administration', 25, 11),
('7890123456', 'Professor', 'Department of Mathematics', 21, 7),
('8901234567', 'Associate Professor', 'Department of Law', 22, 8),
('9012345678', 'Assistant Professor', 'Department of Computer Science', 23, 9);

-- --------------------------------------------------------

--
-- Table structure for table `university_member`
--

CREATE TABLE `university_member` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `university_member`
--

INSERT INTO `university_member` (`id`, `name`, `surname`, `email`, `phone`) VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '12345678'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '23456789'),
(3, 'Peter', 'Parker', 'peter.parker@example.com', '34567890'),
(4, 'Mary', 'Johnson', 'mary.johnson@example.com', '45678901'),
(5, 'Michael', 'Brown', 'michael.brown@example.com', '56789012'),
(6, 'Olivia', 'Davis', 'olivia.davis@example.com', '67890123'),
(7, 'William', 'Wilson', 'william.wilson@example.com', '78901234'),
(8, 'Elizabeth', 'Taylor', 'elizabeth.taylor@example.com', '89012345'),
(9, 'Christopher', 'Lee', 'christopher.lee@example.com', '90123456'),
(10, 'Sarah', 'Thompson', 'sarah.thompson@example.com', '01234567'),
(11, 'Emily', 'Harris', 'emily.harris@example.com', '12345678'),
(12, 'Daniel', 'Clark', 'daniel.clark@example.com', '23456789'),
(13, 'Emma', 'Walker', 'emma.walker@example.com', '34567890'),
(14, 'Alexander', 'Allen', 'alexander.allen@example.com', '45678901'),
(15, 'Ava', 'Green', 'ava.green@example.com', '56789012'),
(16, 'Ethan', 'King', 'ethan.king@example.com', '67890123'),
(17, 'Sophia', 'Wright', 'sophia.wright@example.com', '78901234'),
(18, 'Michael', 'Scott', 'michael.scott@example.com', '89012345'),
(19, 'Isabella', 'Hall', 'isabella.hall@example.com', '90123456'),
(20, 'David', 'Lee', 'david.lee@example.com', '01234567');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `teacher_id` (`teacher_id`),
  ADD KEY `semester_id` (`semester_id`);

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
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_id`);

--
-- Indexes for table `room_booking`
--
ALTER TABLE `room_booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `room_id` (`room_id`),
  ADD KEY `booker` (`booker`);

--
-- Indexes for table `semester`
--
ALTER TABLE `semester`
  ADD PRIMARY KEY (`semester_id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`personal_id`),
  ADD KEY `institute` (`institute`),
  ADD KEY `office` (`office`),
  ADD KEY `university_member` (`university_member`);

--
-- Indexes for table `university_member`
--
ALTER TABLE `university_member`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `room_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `room_booking`
--
ALTER TABLE `room_booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `semester`
--
ALTER TABLE `semester`
  MODIFY `semester_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `university_member`
--
ALTER TABLE `university_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`personal_id`),
  ADD CONSTRAINT `course_ibfk_2` FOREIGN KEY (`semester_id`) REFERENCES `semester` (`semester_id`);

--
-- Constraints for table `lecture`
--
ALTER TABLE `lecture`
  ADD CONSTRAINT `lecture_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `lecture_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `room_booking` (`booking_id`);

--
-- Constraints for table `room_booking`
--
ALTER TABLE `room_booking`
  ADD CONSTRAINT `room_booking_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`),
  ADD CONSTRAINT `room_booking_ibfk_2` FOREIGN KEY (`booker`) REFERENCES `university_member` (`id`);

--
-- Constraints for table `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`institute`) REFERENCES `institute` (`institute`),
  ADD CONSTRAINT `teacher_ibfk_2` FOREIGN KEY (`office`) REFERENCES `room` (`room_id`),
  ADD CONSTRAINT `teacher_ibfk_3` FOREIGN KEY (`university_member`) REFERENCES `university_member` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
