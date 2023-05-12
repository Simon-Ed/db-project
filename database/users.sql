USE `project_db`;

CREATE USER `general_public`@`%`;
CREATE USER `student`@`%`;
CREATE USER `lecturer`@`%`;
CREATE USER `admin`@`%`;
# Privileges for admin@%

GRANT SELECT, INSERT, UPDATE, DELETE ON * TO `admin`@`%`;

# Privileges for general_public@%

GRANT SELECT ON `building` TO `general_public`@`%`;
GRANT SELECT ON `course` TO `general_public`@`%`;
GRANT SELECT ON `institute` TO `general_public`@`%`;
GRANT SELECT ON `lecture` TO `general_public`@`%`;
GRANT SELECT ON `room` TO `general_public`@`%`;
GRANT SELECT ON `room_booking` TO `general_public`@`%`;
GRANT SELECT ON `teacher` TO `general_public`@`%`;
GRANT SELECT ON `university_member` TO `general_public`@`%`;
GRANT SELECT ON `project_db`.`user` TO `general_public`@`%`;
GRANT SELECT ON `user_schedule` TO `general_public`@`%`;


GRANT SELECT ON `bookable_rooms` TO `general_public`@`%`;
GRANT SELECT ON `booked_rooms` TO `general_public`@`%`;
GRANT SELECT ON `contact_info` TO `general_public`@`%`;
GRANT SELECT ON `course_schedules` TO `general_public`@`%`;
GRANT SELECT ON `course_semester` TO `general_public`@`%`;
GRANT SELECT ON `user_time_schedule` TO `general_public`@`%`;

GRANT INSERT ON `project_db`.`user` TO `general_public`@`%`;
GRANT INSERT ON `user_schedule` TO `general_public`@`%`;

# Privileges for student@%

GRANT SELECT ON * TO `student`@`%`;
 
GRANT INSERT ON `project_db`.`user` TO `student`@`%`;
GRANT INSERT ON user_schedule TO `student`@`%`;
GRANT INSERT ON room_booking TO `student`@`%`;

# Privileges FOR lecturer@%

GRANT SELECT ON * TO `lecturer`@`%`;

GRANT INSERT ON `project_db`.`user` TO `lecturer`@`%`;
GRANT INSERT ON  user_schedule TO `lecturer`@`%`;
GRANT INSERT ON  room_booking TO `lecturer`@`%`;

GRANT UPDATE ON course TO `lecturer`@`%`;
GRANT UPDATE ON lecture TO `lecturer`@`%`;
GRANT UPDATE ON room_booking TO `lecturer`@`%`;
