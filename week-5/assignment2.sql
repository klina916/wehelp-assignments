CREATE TABLE `member`( 
	`id` BIGINT AUTO_INCREMENT, 
	`name` VARCHAR(255) NOT NULL, 
	`username` VARCHAR(255) NOT NULL, 
	`password` VARCHAR(255) NOT NULL, 
	`follower_count` INT DEFAULT 0 NOT NULL, 
	`time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY(id)
);
