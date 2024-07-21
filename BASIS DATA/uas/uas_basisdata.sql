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
/* INDEX */
CREATE index idx_user on user(id_user); 
CREATE index idx_tugas on tugas(id_tugas);
CREATE index idx_goal on goal(id_goal);
CREATE index idx_artikel on artikel(judul_artikel);
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
set autocommit = 0;
start transaction;
call sp_tambah_user("A0001","Ibu Maya","maya@gmail.com","123",1);
call sp_validate_login("maya@gmail.com","123");
commit;
start transaction;
delete from `user` where `status` = 2;
rollback;
select * from user_view;

/* CRUD TABLE TUGAS */
start transaction;
select * from tugas;
call sp_tambah_tugas("T1","Memberi makan anak","Memberi makan anak pertama","Keluarga",2,'2024-3-25 16:0:0',"A0001");
call sp_update_status_tugas("T1","A0001",1);
commit;
start transaction;
delete from tugas where status_tugas = 2;
rollback;
select * from tugas_view;

/* CRUD TABLE GOAL */
start transaction;
select * from goal;
call sp_tambah_goal("G1","Liburan Bersama Keluarga",2,"Keluarga","A0001");
update goal set status_goal = 1 where id_user = "A0001" and id_goal = "G1";
commit;
start transaction;
call sp_hapus_goal("G1","A0001");
rollback;
select * from goal_view;
/* CRUD TABLE ARTIKEL */
start transaction;
select * from artikel;
insert into artikel (judul_artikel,kategori_artikel,link)
values("5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak","anak","https://www.sasa.co.id/articles/tips-trick/5-resep-makanan-sehat-dan-bergizi-cocok-untuk-anak");
update artikel set kategori_artikel = "keluarga" where judul_artikel = "5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak";
start transaction;
delete from artikel where judul_artikel = "5 Resep Makanan Sehat dan Bergizi, Cocok untuk Anak";
rollback;

/*user akses*/
create user 'user1'@'localhost' identified by "123";

grant insert,select,update on project_db.user to 'user'@'localhost' with grant option;
grant insert,select,update on project_db.tugas to 'user'@'localhost' with grant option;
grant insert,select,update on project_db.goal to 'user'@'localhost' with grant option;
