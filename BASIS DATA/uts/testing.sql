/* data testing */
SET sql_safe_updates = 0;
call sp_validate_register("A0001","Ibu Maya","maya@gmail.com","123",1);
call sp_validate_login("maya@gmail.com","123");
call sp_tambah_tugas(
    "T1",
    "memberi makan anak",
    "memberi makan anak pertama",
    "keluarga",
    1,
    '2024-3-25 16:0:0',
    "A0001");
call sp_update_status_tugas("T1","A0001",1); /* tugas akan terhapus setelah ada update pada user table */
call sp_tambah_goal(
    "G1",
    "Liburan bersama Keluarga",
    2,
    "Keluarga",
    "A0001"
);
call sp_hapus_goal("G1","A0001");
call sp_logout("A0001");






select * from user;
SELECT * from tugas;
SELECT * from goal;
SELECT * from tugas_view;
SELECT * from goal_view;
select * from user_view;
drop database project_db;
drop table artikel;
