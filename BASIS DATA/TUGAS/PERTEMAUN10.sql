CREATE DATABASE PERTEMUAN10;

use PERTEMUAN10;

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
    foreign key (Kode_jurusan) references jurusan(Kode_jurusan)
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


insert into jurusan (Kode_jurusan,nama_jurusan,ketua_jurusan)
values ('KD04','jurusan_coba','nama_dosen');

UPDATE biodata set nama_mahasiswa = 'Rina gunawan' WHERE no_mahasiswa = '210089';

UPDATE jurusan set Kode_Jurusan = 'KM01' where Kode_Jurusan = 'KD01';

alter table biodata
drop foreign key biodata_ibfk_1;

ALTER table biodata
add constraint FK_kode_jurusan
    foreign key (Kode_Jurusan) references jurusan(Kode_Jurusan) on delete cascade on update cascade; 

UPDATE biodata set no_mahasiswa = '210098' where no_mahasiswa = '210089';

UPDATE biodata set ipk = '3.3' where no_mahasiswa = '210012';

update jurusan set Kode_Jurusan = 'KD05' where Kode_Jurusan = 'KD03';


/* kesimpulan: untuk melakukan perubahan atau penambahan pada child row diperlukan memerhatikan bagian parents row apakah child row yang akan di isi sudah ada pada parents row. jika ingin melakukan perubahan pada parents row maka diperlukan perintah on delete cascade on delete updata pada foreign key tersebut */