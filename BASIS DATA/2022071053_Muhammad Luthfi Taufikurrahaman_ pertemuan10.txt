CREATE DATABASE `2022071053`;

use `2022071053`;

/* pratikum 1 */   
CREATE table jurusan(
    Kode_jurusan VARCHAR(5) PRIMARY key,
    nama_jurusan varchar(50),
    ketua_jurusan varchar(100)
);

CREATE table biodata(
    no_mahasiswa varchar (10) primary key,
    Kode_jurusan varchar (5),
    nama_mahasiswa varchar(100),
    alamat varchar(50),
    IPK char(5),
    foreign key (Kode_jurusan) references jurusan(Kode_jurusan) ON DELETE CASCADE ON UPDATE CASCADE
);

insert into jurusan (Kode_jurusan,nama_jurusan,ketua_jurusan)
values
('KD01','Sistem Informasi','Harnaningrum,S.Si'),
('KD02','Teknik Informatika','EnnySela,S.kom,M.Kom'),
('KD03','Teknik Komputer','Berta Bednar,S.Si,M.T');

insert into biodata (no_mahasiswa,Kode_jurusan,nama_mahasiswa,alamat,ipk)
values
('210089','KD01','Rina Gunawan', 'Denpasar','3'),
('210090','KD03','Ganti Suprapto', 'Singaraja','3.5'),
('210012','KD02','Alexandra', 'Nusa Dua','3'),
('210099','KD02','Nadine', 'Gianyar','3.2'),
('210002','KD01','Rizal samurai', 'Denpasar','3.7');

INSERT into jurusan(Kode_Jurusan,nama_jurusan,ketua_jurusan)
values("KD04","Nama_jurusan","Nama_dosen");

INSERT into biodata(no_mahasiswa,Kode_jurusan,nama_mahasiswa,alamat,ipk)
values('210100','KD04',"Nama_mahasiswa",'jogja','3.5');/*tidak bisa dikarenakan tidak ada data KD05 pada tabel jurusuan */

UPDATE biodata set nama_mahasiswa = 'Rina gunawan Astuti' WHERE no_mahasiswa = '210089';

UPDATE jurusan set Kode_Jurusan = 'KM01' where Kode_Jurusan = 'KD01';

UPDATE biodata set no_mahasiswa = '210098' where no_mahasiswa = '210089';

UPDATE biodata set ipk='3.3' where ipk = '3';

UPDATE biodata set kode_jurusan = 'KD05' where kode_jurusan = 'KD03'; /* tidak bisa dikarenakan tidak ada data KD05 pada tabel jurusuan */

/* untuk mengupdate row yang memiliki foreign key pada child table perlu diperhatikan apakah data sudah ada pada parent table */

/* praktikum 2 */

SELECT biodata.no_mahasiswa,jurusan.nama_jurusan,jurusan.ketua_jurusan from biodata, jurusan;

SELECT biodata.nama_mahasiswa,biodata.ipk,jurusan.nama_jurusan,jurusan.ketua_jurusan from biodata INNER JOIN jurusan on jurusan.Kode_jurusan = biodata.Kode_jurusan;

SELECT biodata.nama_mahasiswa,biodata.ipk,jurusan.nama_jurusan,jurusan.ketua_jurusan from biodata LEFT JOIN jurusan on jurusan.Kode_jurusan = biodata.Kode_jurusan;

SELECT biodata.nama_mahasiswa,biodata.ipk,jurusan.nama_jurusan,jurusan.ketua_jurusan from biodata RIGHT JOIN jurusan on jurusan.Kode_jurusan = biodata.Kode_jurusan;

/* kesimpulan: pada left join, table yang ada terlebih dahulu atau asal akan bergabung dengan tabel tujuan.
pada right join, table yang menjadi tujuan akan bergabung dengan tabel yang menjadi awal */

/* praktikum 3 */
SELECT lower(nama_jurusan) as huruf_kecil from jurusan;
SELECT upper(nama_jurusan) as huruf_kecil from jurusan;
SELECT substring(nama_jurusan,4) as huruf_kecil from jurusan;
SELECT substring(nama_jurusan,4) as huruf_kecil from jurusan;
SELECT ltrim(nama_mahasiswa) as delete_spasi_awal from biodata;
SELECT rtrim(nama_mahasiswa) as delete_spasi_awal from biodata;
SELECT RIGHT(ipk,2) as dibelakang_koma from biodata;
SELECT LEFT(ipk,1) as dibelakang_koma from biodata;
SELECT nama_mahasiswa, length(nama_mahasiswa) as panjang from biodata;
SELECT nama_mahasiswa, reverse(nama_mahasiswa) as kebalik from biodata;
SELECT nama_mahasiswa, space(10) from biodata;

/*praktikum 4*/
SELECT * from biodata ORDER BY ipk asc;
SELECT avg(ipk) as ipk_rata2 from biodata;
SELECT count(*) as jumlah_data from biodata;
SELECT sum(ipk) as total_ipk from biodata;
SELECT max(ipk) as tertinggi_ipk from biodata;
SELECT min(ipk) as tertinggi_ipk from biodata;
SELECT nama_mahasiswa,Kode_jurusan from biodata GROUP BY Kode_jurusan;
SELECT nama_mahasiswa,Kode_jurusan from biodata GROUP BY Kode_jurusan having sum(IPK) > 3.5;
SELECT nama_mahasiswa,Kode_jurusan,IPK from biodata 
GROUP BY Kode_jurusan 
having sum(IPK) > 3.5
ORDER by IPK DESC;


/* praktikum 5 */
SELECT no_mahasiswa,kode_jurusan,ipk from biodata WHERE ipk > (SELECT avg(ipk) from biodata)
UNION
SELECT no_mahasiswa,kode_jurusan,ipk from biodata where ipk < 3.5;

SELECT biodata.no_mahasiswa,biodata.kode_jurusan,biodata.ipk,jurusan.nama_jurusan,jurusan.ketua_jurusan from biodata INNER join jurusan on jurusan.kode_jurusan = biodata.kode_jurusan
UNION
SELECT biodata.no_mahasiswa, biodata.kode_jurusan, biodata.ipk,jurusan.nama_jurusan,jurusan.ketua_jurusan
FROM biodata, jurusan 
where biodata.no_mahasiswa not in (SELECT biodata.no_mahasiswa from biodata where ipk > 3.3 );

/*kesimpulan perintah dari intersect mengambil irisan dari data yang sama sementara except mengambil data yang tidak sama.*/

/* praktikum 6 */

/* fungsi dari view adalah untuk mempermudah developer dalam melihat tabel dengan kondisi tertentu, mempercepat untuk melihat tabel dengan sturktur tertemtu*/

CREATE view IPK_tertinggi
as SELECT * from biodata where ipk = (SELECT max(ipk) from biodata);

SELECT * from IPK_tertinggi;

CREATE TEMPORARY TABLE Data_mahasiswa(
    id_mahasiswa varchar(5),
    nama_mahasiswa varchar(100),
    alamat varchar(255),
    nama_jurusan varchar(100),
    ipk char(5),
    sks int
);

SELECT id_mahasiswa,nama_mahasiswa,alamat,nama_jurusan,ipk,sks from Data_mahasiswa
UNION
SELECT biodata.no_mahasiswa,biodata.nama_mahasiswa,biodata.alamat,jurusan.nama_jurusan,biodata.ipk,
case
    when biodata.ipk >= 3  then 24 
    when biodata.ipk >= 2.5 and biodata.ipk <= 3 then 20
end as sks
from biodata,jurusan;


/* praktikum 7 */

DELIMITER //
CREATE procedure seluruh_mhs (
)
begin
    SELECT biodata.no_mahasiswa,biodata.nama_mahasiswa,biodata.alamat,biodata.ipk,jurusan.ketua_jurusan from biodata RIGHT join jurusan on jurusan.kode_jurusan = biodata.Kode_Jurusan ORDER BY jurusan.ketua_jurusan desc;
end // DELIMITER;

call seluruh_mhs;

delimiter //
create procedure nama_jurusan(in nama_ketua varchar(255))
BEGIN
    select * from jurusan where ketua_jurusan = nama_ketua;
end
// delimiter;

call nama_jurusan('nama_dosen');

create table biodata_backup(
    id_mahasiswa varchar(10),
    nama_mahasiswa varchar(100),
    alamat varchar(255),
    nama_jurusan varchar(100),
    ipk char(5)
);

delimiter //
Create trigger update_biodata
after insert on biodata for each row
begin
    insert into biodata_backup
    SELECT biodata.no_mahasiswa,biodata.nama_mahasiswa,biodata.alamat,jurusan.nama_jurusan,biodata.ipk from biodata RIGHT join jurusan on jurusan.kode_jurusan = biodata.Kode_Jurusan;
end // delimiter;

insert into biodata(no_mahasiswa,kode_jurusan,nama_mahasiswa,alamat,ipk)
values
("210889","KM01","luthfi","Tangsel",'3.33');

select * from biodata_backup;

/*perbedaan stored prosedur: tidak harus mengembalikan nilai 
function: harus mengembalikan nilai */