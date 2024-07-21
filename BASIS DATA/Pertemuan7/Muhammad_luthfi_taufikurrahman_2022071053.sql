Create DATABASE pertemuan7;
delete set priority_level;

select @priority_level from akademik.mahasiswa;
Create TABLE pertemuan7.mahasiswa(
    id int primary key AUTO_INCREMENT

);

alter table pertemuan7.mahasiswa
add  nama varchar(50);

alter table pertemuan7.mahasiswa
change nama nama_lengkap varchar(50);

alter table pertemuan7.mahasiswa
rename to pertemuan7.mhs;

drop database pertemuan7;
drop table pertemuan7.mhs;
drop index 123 on id;