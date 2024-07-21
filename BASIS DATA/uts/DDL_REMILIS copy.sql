					/* project kelompok 4*/
SET sql_safe_updates = 0;
create database project_db;
use project_db;

create table project_db.`user`(
	id_user varchar(5) primary key,
    nama varchar(32),
    gmail varchar(255),
    sandi varchar(32),
    `status` enum("active","not_active"),
    constraint chck_status CHECK (`status` = "active" or `status` = "not_active")
);

create table project_db.tugas(
	id_tugas varchar(5) primary key,
    nama_tugas varchar(32),
    deskripsi_tugas text,
    kategori varchar(32),
    prioritas enum("high","mid","low"),
    date_end datetime,
    status_tugas enum("done","not done"),
    `user_id` varchar(5),
    foreign key (`user_id`) references project_db.`user`(id_user),
    constraint chck_priority CHECK (prioritas = 'high' or prioritas = 'mid' or prioritas = 'low')
);

create table project_db.goal(
	id_goal varchar(5) primary key,
    nama_goal varchar(32),
    status_goal enum("completed","uncompleted"),
    kategori varchar(32),
    id_user varchar(5),
    foreign key (id_user) references project_db.`user` (id_user),
    constraint chck_goal_status CHECK (status_goal = 'completed' or status_goal = 'uncompleted')
);

create table project_db.artikel(
	judul_artikel varchar(255) primary key,
    kategori_artikel varchar(32),
    link varchar(255)
);

/* Create Procedure table user*/

delimiter //
CREATE PROCEDURE sp_update_login(
    in_gmail varchar(255),
    in_sandi varchar(32)
)
begin
    update project_db.user set `status` = 1 where gmail = in_gmail and sandi = in_sandi;
END
// delimiter;
 
delimiter //
CREATE PROCEDURE sp_validate_login(
    in_gmail varchar(255),
    in_sandi varchar(32)
)
BEGIN
   declare user_count int;
   SELECT count(*) into user_count from user where gmail = in_gmail and sandi = in_sandi;
   if user_count > 0 then 
        call sp_update_login(in_gmail,in_sandi);
	else 
		select 'email atau password salah'; 
    end if;
END
// delimiter;

delimiter //
Create PROCEDURE sp_logout(
    in_id varchar(5)
)
begin
    update user set `status` = 2 where id_user = in_id;
end
// delimiter;

delimiter //
CREATE PROCEDURE sp_validate_register(
    in_id varchar(5),
    in_nama varchar(32),
    in_gmail varchar(255),
    in_sandi varchar(32),
    in_status enum("not_active")
)
BEGIN
    declare user_count int;
    SELECT count(*) into user_count from user where gmail = in_gmail;
    if user_count = 0 then 
        call sp_tambah_user(in_id,in_nama,in_gmail,in_sandi,in_status);
    else 
        select 'error gmail have been used';
    end if;
END
// delimiter;


delimiter // 
CREATE PROCEDURE sp_tambah_user(
	in_id varchar(5),
    in_nama varchar(32),
    in_gmail varchar(255),
    in_sandi varchar(32),
    in_status enum("not_active")
)
BEGIN
    INSERT INTO project_db.`user`(id_user, nama, gmail, sandi, `status`)
    VALUES (in_id, in_nama, in_gmail, in_sandi, in_status);
END
// delimiter;


delimiter // 
CREATE PROCEDURE sp_update_password(
    in_gmail varchar(255),
    in_sandi varchar(32)
)
BEGIN
    UPDATE project_db.`user` SET sandi = in_sandi WHERE gmail = in_gmail;
END
//delimiter;

/* create procedure tugas */

delimiter //
CREATE trigger after_task_done
after update on user
for each row
BEGIN
    delete from project_db.tugas where status_tugas = "done";
end
// delimiter;

delimiter //
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
    INSERT INTO project_db.tugas(id_tugas, nama_tugas, deskripsi_tugas, kategori, prioritas, date_end,status_tugas, `user_id`)
    VALUES (in_id_tugas, in_nama_tugas, in_deskripsi_tugas, in_kategori, in_prioritas, in_date_end,2, in_user);
END
// delimiter ;

delimiter //
CREATE procedure sp_update_status_tugas(
    in_id_tugas varchar(5),
    in_user_id varchar(5),
    in_status int
)
begin
    update tugas set tugas.status_tugas = in_status where id_tugas = in_id_tugas and tugas.user_id = in_user_id;
end
//delimiter ;

/* create procedure goal */
delimiter //
CREATE PROCEDURE sp_tambah_goal(
    in_id_goal varchar(5),
    in_nama_goal varchar(32),
    in_status_goal enum("completed","uncompleted"),
    in_kategori varchar(32),
    in_id_user varchar(5)
)
BEGIN
    INSERT INTO project_db.goal(id_goal, nama_goal, status_goal, kategori, id_user)
    VALUES (in_id_goal, in_nama_goal, in_status_goal, in_kategori, in_id_user);
END
//delimiter ;

delimiter //
CREATE PROCEDURE sp_hapus_goal(
    in_id_goal varchar(5),
    in_id_user varchar(5)
)
begin
    delete from goal where id_goal = in_id_goal and id_user = in_id_user;
end
//delimiter ;

/* create user view */
CREATE VIEW tugas_view as
select 
nama_tugas,
deskripsi_tugas,
kategori,
prioritas,
date_end,
status_tugas 
from project_db.tugas, project_db.user where tugas.user_id = (SELECT id_user from user where user.status = 'active');

create view goal_view as
SELECT
nama_goal,
status_goal,
kategori
from goal, user where goal.id_user = (SELECT id_user from user where user.status = 'active');

create view user_view as
select
nama,
gmail,
sandi
from project_db.user where user.status = "active";

/* CRUD TABLE USER */
select * from project_db.user;
insert into `user`(id_user,nama,gmail,sandi,`status`)
values("A0001","Ibu Maya","maya@gmail.com","123",1);
update `user` set `status` = 2 where id_user = "A0001";
delete from `user` where `status` = 2;

/* CRUD TABLE TUGAS */
select * from tugas;
insert into tugas (id_tugas,nama_tugas,deskripsi_tugas,kategori,prioritas,date_end,status_tugas,user_id)
values("T1","Memberi makan anak","Memberi makan anak pertama","Keluarga",1,'2024-3-25 16:0:0',2,"A0001");
update tugas set status_tugas = 1 where user_id = "A0001" and id_tugas = "T1";
delete from tugas where status_tugas = 2;

/* CRUD TABLE GOAL */
select * from goal;
insert into goal (id_goal,nama_goal,status_goal,kategori,id_user)
values("G1","Liburan Bersama Keluarga",2,"Keluarga","A0001");
update goal set status_goal = 1 where id_user = "A0001" and id_goal = "G1";
delete from goal where status_goal = 1;

/* CRUD TABLE ARTIKEL */
select * from artikel;
insert into artikel (judul_artikel,kategori_artikel,link)
values("5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak","anak","https://www.sasa.co.id/articles/tips-trick/5-resep-makanan-sehat-dan-bergizi-cocok-untuk-anak");
update artikel set kategori_artikel = "keluarga" where judul_artikel = "5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak";
delete from artikel where judul_artikel = "5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak";
