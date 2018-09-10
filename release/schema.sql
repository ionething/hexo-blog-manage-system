create table setting
(
	id Integer not null
		primary key
		 autoincrement,
	setting_key text,
	setting_value text,
	setting_name text,
	setting_index int default 1
)
;

create unique index setting_setting_key_uindex
	on setting (setting_key)
;

create table user
(
	id INTEGER
		primary key
		 autoincrement,
	username TEXT not null
		unique,
	password TEXT not null
)
;

INSERT INTO user (id, username, password) VALUES (1, 'admin', 'admin');

INSERT INTO setting (id, setting_key, setting_value, setting_name, setting_index) VALUES (1, 'blog.dir', '/home/dir', '目录', 1);
