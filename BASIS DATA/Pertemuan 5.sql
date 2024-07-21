/*DISABLE FOREIGN KEY CONSTRAINT CHECKING */
set FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE akademik;

CREATE TABLE akademik.dosen (
  Nip varchar(12) NOT NULL,
  Nama_Dosen varchar(25) NOT NULL,
  PRIMARY KEY (Nip)
);

CREATE TABLE akademik.mahasiswa (
  Nim varchar(9) NOT NULL,
  Nama_Mhs varchar(25) NOT NULL,
  Tgl_Lahir date NOT NULL,
  Alamat varchar(50) NOT NULL,
  Jenis_Kelamin enum('Laki-laki','Perempuan') NOT NULL,
  PRIMARY KEY (Nim)
);

CREATE TABLE akademik.matakuliah (
  Kode_MK varchar(6) NOT NULL,
  Nama_MK varchar(20) NOT NULL,
  Sks int(2) NOT NULL,
  PRIMARY KEY (Kode_MK)
); 

CREATE TABLE akademik.perkuliahan (
  Nim varchar(9) DEFAULT NULL,
  Kode_MK varchar(7) DEFAULT NULL,
  Nip varchar(12) DEFAULT NULL,
  Nilai char(1) NOT NULL,
  KEY Nip (Nip),
  KEY Nim (Nim),
  KEY Kode_MK (Kode_MK),
  CONSTRAINT perkuliahan_ibfk_1 FOREIGN KEY (Nip) REFERENCES dosen (Nip) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT perkuliahan_ibfk_2 FOREIGN KEY (Nim) REFERENCES mahasiswa (Nim) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT perkuliahan_ibfk_3 FOREIGN KEY (Kode_MK) REFERENCES matakuliah (Kode_MK) ON DELETE CASCADE ON UPDATE CASCADE
); 

DROP DATABASE akademik;
/* script berhasil dijalankan*/
/* Constraint digunakan untuk memberikan aturan khusus pada sebuah data sementara 'on delete cascade on update cascade' berarti data dari child akan terhapus jika data dari parent terupdate atau terhapus*/
/* Key digunakan untuk memberi indentitas pada row yang spesifik pada table
atau untuk mencari atau membuat relasi dengan table lain */


				/* TABLE DOSEN */
SELECT * FROM akademik.dosen;
SELECT * FROM akademik.dosen WHERE akademik.Nip = "0429038801"; /* ERROR Belum ada data*/
/*INSERT DATA*/
insert into akademik.dosen(Nip,Nama_Dosen)
Values("0429038801","Mariana, S.Kom.,MMSI.");
/*UPDATE DOSEN */
UPDATE akademik.dosen set akademik.Nama_dosen = ",S.kom.,MMSI."
WHERE akademik.ip = "0429038801";
/* Delete Dosen */
DELETE FROM akademik.dosen WHERE akademik.Nip = "0429038801";

/* Insert table lainya*/
INSERT INTO akademik.mahasiswa(Nim,Nama_Mhs,Tgl_lahir,Alamat,Jenis_kelamin)
values
("510010001","Firmanysyah","1990-03-09","JL. Watu Mujur No.10","Laki-Laki"),
("510010002","Rita Zahara","1989-03-08","Jl. Gebang Lor.NO.10","Perempuan");

INSERT INTO akademik.matakuliah (Kode_MK,Nama_MK,Sks)
values
("IF1101","Pemrograman Web",3),
("IF1102","Basis Data",3),
("IF1202","Matematika Diskrit",4),
("IF1401","Algoritma Pemrog",3),
("IF1402","Pemrograman Berorien",3);

insert into akademik.perkuliahan (Nim,Kode_mk,Nip,Nilai)
Values
("510010001","IF1101","0429038801",'A');

/* Update Table lainya*/
Update akademik.matakuliah set Nama_MK = "Algoritma Prog" where Kode_mk = "IF1401";
Update akademik.matakuliah set Nama_MK = "Pemrograman Objek" where Kode_mk = "IF1402";

Update akademik.mahasiswa set Nama_mhs = "Rendi" where Nim = "510010001";

Update akademik.perkuliahan set Nilai = 'B' where Nim = "510010001";

/* Delete Table lainya*/
Delete from akademik.matakuliah where Kode_mk = "IF1402";

Delete from akademik.mahasiswa where Nim = "510010001";

Delete from akademik.perkuliahan where Nim = "510010001";

/* alter table */
alter table akademik.mahasiswa
add column Status_mahasiswa varchar(12);

alter table akademik.dosen
add column Status_dosen varchar(12);

alter table akademik.matakuliah
add column semester int;

alter table akademik.perkuliahan
add column status_Perkuliahan varchar(12);

/* Update column yang telah di tambahkan */
update akademik.mahasiswa set Status_mahasiswa = "Aktif" where Nim is NOT NULL;
UPDATE akademik.dosen set Status_dosen = "Aktif" where Nip is NOT NULL;
UPDATE akademik.matakuliah set semester = 3 where Kode_MK = "IFA1402";
UPDATE akademik.perkuliahan set status_Perkuliahan = "Lulus" where nilai != 'd';
				/* CREATE PROCEDURE DOSEN*/
CREATE PROCEDURE SP_TAMBAH_DOSEN (IN Nomor_induk varchar(12),IN Nama varchar(25))
	BEGIN 
	 insert into akademik.dosen(Nip,Nama_Dosen)
	 values(Nomor_induk, nama);
	end;

create procedure SP_Query_Data_Dosen (in Nomor_induk varchar(12))
begin
select * from akademik.dosen where Nip = nomor_induk;
end;

create procedure SP_Update_Data_Dosen(IN Nomor_induk varchar(12))
begin
Update akademik.dosen set Nama_Dosen = "Gisna" where Nip = Nomor_induk;
end;

Create procedure SP_Delete_Dosen(IN Nomor_induk varchar(12))
begin
delete from akademik.dosen where Nip = Nomor_induk;
end;

/* Create Procedure mahasiswa */
CREATE PROCEDURE SP_TAMBAH_MAHASISWA (
  IN Nomor_induk varchar(12),
  IN Nama varchar(25),
  IN lahir DATE,
  IN almt varchar(50),
  IN Gender varchar(12),
  IN Status_siswa varchar(10)
)
	BEGIN 
	 insert into akademik.mahasiswa(Nim,Nama_Mhs,Tgl_Lahir,alamat,Jenis_Kelamin,Status_mahasiswa)
	 values(Nomor_induk, Nama, lahir, almt, Gender, Status_mahasiswa);
	end;

create procedure SP_Query_Data_Mahasiswa (in Nomor_induk varchar(12))
begin
select * from akademik.mahasiswa where Nim = nomor_induk;
end;

create procedure SP_Update_Data_Mahasiswa(IN Nomor_induk varchar(12))
begin
Update akademik.mahasiswa set Nama_Mhs = "Gisna" where Nim = Nomor_induk;
end;

Create procedure SP_Delete_Mahasiswa(IN Nomor_induk varchar(12))
begin
delete from akademik.mahasiswa where Nim = Nomor_induk;
end;

/* create procedure mata kuliah */

CREATE PROCEDURE SP_TAMBAH_MK(IN kode varchar(12),IN Nama varchar(25), IN sks int,IN smstr int)
	BEGIN 
	 insert into akademik.matakuliah(Kode_MK,Nama_MK,Sks,semester)
	 values(kode, Nama, Sks, smstr);
	end;

create procedure SP_Query_Data_MK (in kode varchar(12))
begin
select * from akademik.matakuliah where Kode_MK = kode;
end;

create procedure SP_Update_Data_MK (IN kode varchar(12))
begin
Update akademik.matakuliah set Nama_MK = "Pertemuan 5" where Kode_MK = kode;
end;

Create procedure SP_Delete_Nama_MK(IN kode varchar(12))
begin
delete from akademik.matakuliah where Nim = kode;
end;

/* Create procedure perkuliahan */
CREATE PROCEDURE SP_TAMBAH_PERKULIAHAN(IN NIM varchar(12),IN KODE varchar(25), IN NIP varchar(12),IN NILAI char(1), status_per varchar(12))
	BEGIN 
	 insert into akademik.perkuliahan(Nim,Kode_MK,Nip,Nilai,status_Perkuliahan)
	 values(NIM,KODE,NIP,NILAI,status_per);
	end;


create procedure SP_Query_Data_Perkuliahan (in kode varchar(12))
begin
select * from akademik.perkuliahan where Kode_MK = kode;
end;


create procedure SP_Update_Data_Perkuliahan (IN kode varchar(12))
begin
Update akademik.perkuliahan set Nilai = 'A' where Kode_MK = kode;
end;


Create procedure SP_Delete_Perkuliahan(IN kode varchar(12))
begin
delete from akademik.perkuliahan where Nim = kode;
end;
/* memangil procedure yang telah dibuat */
call SP_TAMBAH_DOSEN("12345678","ATENG");
call SP_Query_Data_Dosen ("12345678");
call SP_Update_Data_Dosen("12345678");
call SP_delete_Dosen("12345678");
call SP_TAMBAH_MAHASISWA("12345678","ATENG","2004-01-01","JL. Sukabakti NO.7","Laki-Laki","Aktif");
call SP_Query_Data_Mahasiswa ("12345678");
call SP_Update_Data_Mahasiswa ("12345678");
call SP_Delete_Mahasiswa("12345678");
call SP_TAMBAH_MK("IFA103","Pertemuan4",4,4);
call SP_Query_Data_MK ("IFA103");
call SP_Update_Data_MK ("IFA103");
call SP_Delete_Nama_MK ("IFA103");
call SP_TAMBAH_PERKULIAHAN ("12345678","IFA103","876543211",'B',"Lulus");
call SP_Query_Data_Perkuliahan ("IFA103");
call SP_Update_Data_Perkuliahan ("IFA103");
call SP_Delete_Perkuliahan ("IFA103");