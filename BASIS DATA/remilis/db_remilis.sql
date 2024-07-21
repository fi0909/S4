create database remilis_db;

create table `remilis_db.user`(
	id_user varchar(5) primary key,
    nama varchar(50),
    username varchar(50),
	sandi varchar(16),
    status_user enum("aktif","non-aktif")
);
create table `remilis_ db.tugas`(
	id_tugas varchar(5) primary key,
    judul_tugas varchar(32),
    deskripsi text,
    tugas_date datetime,
    tugas_priority enum('high','mid','low'),
    status_tugas boolean,
    user varchar(5),
    FOREIGN KEY (user) REFERENCES remilis_db.user(id_user)

);
create table `remilis_db.reminder`(
    id_reminder VARCHAR(5) primary key,
    judul_reminder varchar(32),
    reminder_desk text,
    tanggal_mulai datetime,
    tanggal_selesai datetime,
    status_reminder boolean,
    user VARCHAR(5),
    tugas VARCHAR(5),
    FOREIGN key (user) REFERENCES remilis_db.user(id_user),
    FOREIGN KEY (tugas) REFERENCES remilis_db.tugas(id_tugas)
);
create table `remilis_db.goal` (
    id_goal VARCHAR(5) primary key,
    nama_target varchar(32),
    status_goal boolean,
    goal_category varchar(32),
    user varchar(5),
    FOREIGN KEY (user) REFERENCES remilis_db.user (id_user),
);
