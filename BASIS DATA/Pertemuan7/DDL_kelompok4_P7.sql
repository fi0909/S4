					/* project kelompok 4*/

create database project_db;

create table project_db.`user`(
	id_user varchar(5) primary key,
    nama varchar(32),
    gmail varchar(255),
    sandi varchar(32),
    `status` enum("active","not_active")
);

create table project_db.tugas(
	id_tugas varchar(5) primary key,
    nama_tugas varchar(32),
    deskripsi_tugas text,
    kategori varchar(32),
    prioritas enum("high","mid","low"),
    date_end datetime,
    status_tugas enum("done","not done"),
    `user` varchar(5),
    foreign key (`user`) references project_db.`user`(id_user)
);

create table project_db.pengingat(
	id_pengingat varchar(5) primary key,
    judul_pengingat varchar(32),
    deskripsi_pengingat text,
    prioritas_pengingat enum("high","mid","low"),
    kategori_pengingat varchar(32),
    date_end datetime,
    date_now datetime,
    id_tugas varchar(5),
    foreign key (id_tugas) references project_db.tugas (id_tugas)
);
create table project_db.goal(
	id_goal varchar(5) primary key,
    nama_goal varchar(32),
    status_goal enum("done","not yet"),
    kategori varchar(32),
    id_user varchar(5),
    foreign key (id_user) references project_db.`user` (id_user)
);

create table project_db.artikel(
	judul_artikel varchar(255) primary key,
    kategori_artikel varchar(32),
    link varchar(32)
);


/* pertemuan 7 */

alter table project_db.goal
modify column status_goal enum("complete","incomplete");



/* Create Procedure*/

DELIMITER //
CREATE PROCEDURE sp_validate_login(
    in_gmail varchar(255),
    in_sandi varchar(32)
)
BEGIN
    SELECT * FROM project_db.`user` WHERE gmail = in_gmail and sandi = in_sandi;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_validate_register(
    in_gmail varchar(255)
)
BEGIN
    SELECT * FROM project_db.`user` WHERE gmail = in_gmail;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE sp_tambah_user(
	in_id varchar(5),
    in_nama varchar(32),
    in_gmail varchar(255),
    in_sandi varchar(32),
    in_status enum("not_active")
)
BEGIN
	CALL sp_validate_register(in_gmail);
    INSERT INTO project_db.`user`(id_user, nama, gmail, sandi, `status`)
    VALUES (in_id, in_nama, in_gmail, in_sandi, in_status);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_update_password(
    in_gmail varchar(255),
    in_sandi varchar(32)
)
BEGIN
    UPDATE project_db.`user` SET sandi = in_sandi WHERE gmail = in_gmail;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_delete_tugas(
    in_status varchar(32)
)
BEGIN
    DELETE FROM project_db.tugas WHERE status_tugas = in_status;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_tambah_tugas(
    in_id_tugas varchar(5),
    in_nama_tugas varchar(32),
    in_deskripsi_tugas text,
    in_kategori varchar(32),
    in_prioritas enum("high","mid","low"),
    in_date_end datetime,
    in_user varchar(5)
)
BEGIN
    INSERT INTO project_db.tugas(id_tugas, nama_tugas, deskripsi_tugas, kategori, prioritas, date_end, `user`)
    VALUES (in_id_tugas, in_nama_tugas, in_deskripsi_tugas, in_kategori, in_prioritas, in_date_end, in_user);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_tambah_goal(
    in_id_goal varchar(5),
    in_nama_goal varchar(32),
    in_status_goal enum("done","not yet"),
    in_kategori varchar(32),
    in_id_user varchar(5)
)
BEGIN
    INSERT INTO project_db.goal(id_goal, nama_goal, status_goal, kategori, id_user)
    VALUES (in_id_goal, in_nama_goal, in_status_goal, in_kategori, in_id_user);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_tambah_pengingat(
    in_id_pengingat varchar(5),
    in_judul_pengingat varchar(32),
    in_deskripsi_pengingat text,
    in_prioritas_pengingat enum("high","mid","low"),
    in_kategori_pengingat varchar(32),
    in_date_end datetime,
    in_date_now datetime,
    in_id_tugas varchar(5)
)
BEGIN
    INSERT INTO project_db.pengingat(id_pengingat, judul_pengingat, deskripsi_pengingat, prioritas_pengingat, kategori_pengingat, date_end, date_now, id_tugas)
    VALUES (in_id_pengingat, in_judul_pengingat, in_deskripsi_pengingat, in_prioritas_pengingat, in_kategori_pengingat, in_date_end, in_date_now, in_id_tugas);
END //
DELIMITER ;

