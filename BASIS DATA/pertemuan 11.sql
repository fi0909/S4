CREATE DATABASE modul2;

use modul2;

                    -- praktikum 8--
CREATE TABLE jurusan(
    kd_jurusan INT,
    nama_jurusan VARCHAR(20),
    primary key(kd_jurusan)
);

DROP TABLE jurusan;

INSERT into jurusan(kd, nama_jurusan)
values(1,"Teknik Rlektro");

UPDATE jurusan set nama_jurusan="Teknik Informatika" WHERE kd_jurusan = 1;

SELECT kd_jurusan, nama_jurusan from jurusan;

CREATE table matakuliah(
    kode_mk VARCHAR(10) PRIMARY key,
    nama_mk varchar(100),
    sks int,
    semester int
);

INSERT INTO matakuliah (kode_mk, nama_mk, sks, semester)
VALUES
  ('PT1447', 'Praktikum Basis Data', 1, 3),
  ('TIK342', 'Praktikum Basis Data', 1, 3),
  ('PT1333', 'Basis Data Terdistribusi', 3, 5),
  ('TIK123', 'Jaringan Komputer', 2, 5),
  ('TIK333', 'Sistem Operasi', 3, 5),
  ('PT1123', 'Grafika Multimedia', 3, 5),
  ('PT1777', 'Sistem Informasi', 2, 3);

SELECT * from matakuliah where sks = 3;
SELECT * from matakuliah where sks = 2 and semester = 3;
SELECT * from matakuliah where sks <= 2 ;
SELECT * from matakuliah where nama_mk like "%sistem%" ;
SELECT * from matakuliah where nama_mk like "%data%" ;
SELECT * from matakuliah where nama_mk like "%basis%" ;
SELECT * from matakuliah order BY nama_mk;
SELECT * from matakuliah order BY sks desc;

                    --partikum 9 --
CREATE table biodata2(
    no_mahasiswa varchar (10) primary key,
    Kode_jurusan varchar (5),
    nama_mahasiswa varchar(100),
    alamat varchar(50),
    IPK char(5)
);

INSERT biodata2 select * from pertemuan10.biodata;

SELECT * from matakuliah where sks = 2 or sks = 1;

SELECT * from matakuliah where nama_mk not like '%Praktikum%';


                    --praktikum 10--

CREATE TABLE mahasiswa_nim (
  nim VARCHAR(20) NOT NULL PRIMARY KEY,
  nama VARCHAR(50) NOT NULL,
  jenis_kelamin VARCHAR(10) NOT NULL,
  tempat_lahir VARCHAR(50) NOT NULL,
  tanggal_lahir DATE NOT NULL,
  alamat VARCHAR(255) NOT NULL
);

INSERT INTO mahasiswa_nim (nim, nama, jenis_kelamin, tempat_lahir, tanggal_lahir, alamat)
VALUES
  ('140533601613', 'Cintya', 'Perempuan', 'Batam', '1998-09-07', 'Jalan Apel'),
  ('140533606464', 'Lugas', 'Laki-Laki', 'Batu', '1995-04-19', 'Jalan Mangga'),
  ('160533608100', 'Dera', 'Laki-Laki', 'Surabaya', '1997-05-17', 'Jalan Melon'),
  ('160533608101', 'Budi', 'Laki-Laki', 'Medan', '1998-10-29', 'Jalan Apel'),
  ('160533608135', 'Fahmi', 'Laki-Laki', 'Jombang', '1999-06-01', 'Jalan Sirsat'),
  ('160533608158', 'Dona', 'Perempuan', 'Bandung', '1998-05-16', 'Jalan Jeruk'),
  ('160533608189', 'Erni', 'Perempuan', 'Lampung', '1997-04-10', 'Jalan Anggur'),
  ('160533608203', 'Dewi', 'Perempuan', 'Jogjakarta', '1998-04-18', 'Jalan Markisa');

SELECT * from mahasiswa_nim where left(nim,2) = '16';
SELECT * from mahasiswa_nim where RIGHT(left(nim,4),2) = '05' and jenis_kelamin like "%laki-laki%" order by nim desc;
SELECT nim,nama,jenis_kelamin,alamat from mahasiswa_nim where left(nim,2) = '14' and alamat not like '%jalan mangga%';
select nim,nama,tanggal_lahir,2024-left(tanggal_lahir,4) as umur from mahasiswa_nim;

                    --praktikum 11 --

CREATE DATABASE db_latihan_1;
use db_latihan_1;
CREATE table mhs(
    nim char(8) NOT null primary key,
    nama varchar(60) not null,
    alamat varchar(100) not null
);
DESCRIBE mhs;

                    --pratikum 12 --
create user 'mahasiswa'@'localhost';

grant select,insert,update on db_latihan_1.mhs
to 'mahasiswa'@"localhost";
                    -- praktikum 13 --
-- latihan praktikum 1--
CREATE database komik_coba1;
CREATE database komik_cobalagi;

show databases;

drop database komik_cobalagi;
use komik_coba1;
show tables from komik_coba1;

-- latihan soal --
CREATE DATABASE db_jualan;

CREATE DATABASE db_jualan: -- Tidak bisa karena sudah ada database --

show databases;

use db_jualan;

CREATE TABLE pedagang (
  id_pedagang CHAR(5) PRIMARY KEY,
  Nama_pedagang VARCHAR(35),
  Ins_kelamin VARCHAR(10),
  Alamat VARCHAR(50),
  No_telp VARCHAR(18),
  Tgl_table DATE
);

CREATE TABLE barang (
  Id_barang CHAR(5) PRIMARY KEY,
  Nama_barang VARCHAR(35),
  Ukuran VARCHAR(10),
  Warna VARCHAR(15)
);
show tables from db_jualan;

ALTER TABLE barang
drop primary key;

ALTER table barang
add column harga int(10);

ALTER table pedagang
rename to pedagang03;

ALTER TABLE barang
add constraint PK_id_barang primary key (Id_barang);

DESCRIBE barang;

ALTER TABLE pedagang03
add column no_hp varchar(20);

ALTER TABLE barang
rename column warna to wrn;
ALTER Table barang
modify column wrn varchar(20);

                        -- praktikum 14--
CREATE DATABASE db_latihan_dml;

use db_latihan_dml;

CREATE TABLE buku(
    id_buku CHAR(4) primary key,
    judul_buku varchar(45),
    penulis varchar(25),
    thn_terbit year(4),
    penerbit varchar(45)
);

DESCRIBE buku;

INSERT INTO buku (id_buku, judul_buku, penulis, thn_terbit, penerbit)
VALUES ('BK01', 'Perahu Kertas', 'Dewi Lestari', '2007', 'Abadi Jaya'),
       ('BK02', 'Laskar Pelangi', 'Andrea Hirata', '2004', 'Abadi Jaya'),
       ('BK03', 'Sang Pemimpi', 'Andrea Hirata', '2005', 'Abadi Jaya'),
       ('BK04', 'Harry Potter 4', 'J.K.Rowling', '2003', 'Indo Karya'),
       ('BK05', 'Warnet SQL', 'DR. Nena', '2009', 'Wacana Ria');

SELECT * from buku;

SELECT * from buku where penerbit = "Abadi Jaya";

SELECT * from buku GROUP BY penerbit;
-- perlu menjalankan:
SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT * from buku ORDER BY penerbit ASC;


SELECT judul_buku,penulis,thn_terbit from buku;

SELECT * from buku where left(penerbit,1) like 'A';
SELECT * from buku where thn_terbit < 2005;
SELECT * from buku where judul_buku like '%sql%';

SELECT judul_buku,penulis from buku ORDER BY penulis;
SELECT judul_buku,penulis from buku ORDER BY penulis DESC;

SELECT judul_buku,penulis,thn_terbit from buku where thn_terbit < 2005;
SELECT judul_buku,penulis,thn_terbit,penerbit from buku where thn_terbit < 2005;
SELECT judul_buku,penulis,thn_terbit,penerbit from buku where penulis = "Andrea Hirata" ORDER BY judul_buku;



