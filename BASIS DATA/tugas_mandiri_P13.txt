/*praktikum 14*/

CREATE DATABASE db_latihan_dml;

use db_latihan_dml;

CREATE table buku(
    id_buku char(4) primary key,
    Judul_buku varchar(45),
    Penulis Varchar(25),
    thn_terbit Year,
    Penerbit varchar(45)
);

INSERT INTO buku (Id_buku, Judul_buku, Penulis, thn_terbit, Penerbit)
VALUES
  ('BK01', 'Perahu Kertas', 'Dewi Lestari', '2007', 'Abadi Jaya'),
  ('BK02', 'Laskar Pelangi', 'Andrea Hirata', '2004', 'Abadi Jaya'),
  ('BK03', 'Sang Pemimpi', 'Andrea Hirata', '2005', 'Abadi Jaya'),
  ('BK04', 'Harry Potter 4', 'J.K. Rowling', '2003', 'Indo Karya'),
  ('BK05', 'Warnet SQL', 'DR. Nena', '2009', 'Wacana Ria');

SELECT * from buku;
SELECT * from buku where penerbit = 'abadi Jaya';
SELECT @@sql_mode;
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY','')); /*menonaktifkan sql_mode = only_full_group_by*/
SELECT * from buku GROUP BY penerbit;
SELECT * from buku ORDER BY penerbit;
SELECT judul_buku,penulis,thn_terbit from buku;
SELECT * from buku where penulis like "A%";
SELECT * from buku where thn_terbit < 2005;
SELECT * from buku where judul_buku like "%sql%";
SELECT * from buku where penulis = "Dewi Lestari";
SELECT judul_buku,penulis from buku ORDER BY penulis DESC;
SELECT judul_buku,penulis,thn_terbit,penerbit FROM buku where thn_terbit < 2005 ORDER BY thn_terbit desc;
SELECT judul_buku,penulis,penerbit FROM buku where penulis = "Andrea Hirata" ORDER BY judul_buku;

/* praktikum 15 */

CREATE DATABASE db_toko;

show databases;

use db_toko;
CREATE TABLE barang (
  kode_brg Char(4) PRIMARY KEY,
  nama_brg Varchar(40),
  harga_brg Int(10),
  thn_pembuat Year,
  stok Int(3)
);

DESCRIBE barang;
INSERT INTO barang (Kode_brg, Nama_brg, Harga_brg, Thn_pembuat, Stok)
VALUES
('BR01', 'Clame Plate', 40000, 2005, 100),
('BR02', 'CF Diafram', 35000, 2001, 250),
('BR03', 'Press Cover', 65000, 2002, 300),
('BR04', 'Terminal', 15000, 2000, 57),
('BR05', 'Alumunium Solt', 27000, 2006, 410);
SELECT kode_brg,nama_brg,stok from barang ORDER BY nama_brg ASC;
SELECT * from barang where nama_brg like "%Terminal%";
SELECT * from barang where nama_brg like "c%";
SELECT kode_brg,nama_brg,harga_brg,stok from barang where stok < 200;
SELECT * from barang where thn_pembuat BETWEEN 2002 and 2006;
SELECT * From barang limit 3;
SELECT * from barang where thn_pembuat = 2000 and stok < 200;
SELECT * From barang ORDER by kode_brg limit 3;
SELECT * From barang where kode_brg != "BR05";

/* praktikum 17 */
CREATE DATABASE 2022071053_bab5;

SHOW databases;

use 2022071053_bab5;

CREATE TABLE buku (
  Kode_buku CHAR(4) PRIMARY KEY,
  Judul VARCHAR(55),
  Pengarang VARCHAR(50),
  Penerbit VARCHAR(35),
  Harga INT(10)
);

DESCRIBE buku;

INSERT INTO buku (Kode_buku, Judul, Pengarang, Penerbit, Harga)
VALUES
('BK01', 'Rancangan ERD', 'Joko Susilo', 'Graha Pustaka', 65000),
('BK02', 'Diagram UML', 'Ahmad Sandi', 'Komunikatika', 40000),
('BK03', 'Web Programming', 'Rio Budiman', 'Graha Pustaka', 35000),
('BK04', 'Dasar Pemrograman', 'Artifa Ningrum', 'Tekno Press', 35000),
('BK05', 'Testing Program', 'Ria Kusumah', 'Ilmu Pustaka', 45000);


SELECT * from buku ORDER BY Harga desc;
SELECT SUM(Harga)as total_harga from buku;
SELECT *  from buku where harga = (SELECT min(harga) from buku);
SELECT *  from buku ORDER BY Harga asc limit 1;
CREATE view bk as SELECT Judul,penerbit,harga from buku;
SELECT * from bk;

SELECT count(*) as jumlah_data from buku;
update buku set judul = "UML Dasar" where judul = "Diagram UML";
insert into buku(Kode_buku, Judul, Pengarang, Penerbit, Harga)
VALUES
("BK06","Algoritma Lanjut","Raden Kraton","Graha Pustaka",40000);
delete from buku where Kode_buku = "BK05";






